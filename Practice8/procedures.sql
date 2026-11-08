-- Insert a user, or replace the phone number(s) for an existing username.
CREATE OR REPLACE PROCEDURE upsert_contact(p_username TEXT, p_phone TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    IF p_username IS NULL OR BTRIM(p_username) = '' THEN
        RAISE EXCEPTION 'username is required';
    END IF;
    IF p_phone IS NULL OR BTRIM(p_phone) = '' THEN
        RAISE EXCEPTION 'phone is required';
    END IF;

    IF EXISTS (SELECT 1 FROM contacts WHERE username = BTRIM(p_username)) THEN
        UPDATE contacts SET phone = BTRIM(p_phone)
        WHERE username = BTRIM(p_username);
    ELSE
        INSERT INTO contacts(username, phone)
        VALUES (BTRIM(p_username), BTRIM(p_phone));
    END IF;
END;
$$;

-- Supply parallel arrays. p_invalid is returned as JSON array with source index,
-- name, phone, and reason for each rejected row. Valid rows are inserted/upserted.
CREATE OR REPLACE PROCEDURE bulk_upsert_contacts(
    IN p_usernames TEXT[],
    IN p_phones TEXT[],
    INOUT p_invalid JSONB DEFAULT '[]'::JSONB
)
LANGUAGE plpgsql AS $$
DECLARE
    i INTEGER;
    row_count INTEGER;
    invalid_rows JSONB := '[]'::JSONB;
    current_name TEXT;
    current_phone TEXT;
    reason TEXT;
BEGIN
    IF COALESCE(array_length(p_usernames, 1), 0) <> COALESCE(array_length(p_phones, 1), 0) THEN
        RAISE EXCEPTION 'username and phone arrays must have equal length';
    END IF;

    row_count := COALESCE(array_length(p_usernames, 1), 0);
    FOR i IN 1..row_count LOOP
        current_name := BTRIM(COALESCE(p_usernames[i], ''));
        current_phone := BTRIM(COALESCE(p_phones[i], ''));
        reason := NULL;

        IF current_name = '' THEN
            reason := 'username is required';
        ELSIF current_phone !~ '^\+?[0-9][0-9(). -]{5,19}$' THEN
            reason := 'phone must contain 6-20 digits and may use +, spaces, parentheses, dots, or hyphens';
        END IF;

        IF reason IS NOT NULL THEN
            invalid_rows := invalid_rows || jsonb_build_array(jsonb_build_object(
                'index', i, 'username', p_usernames[i], 'phone', p_phones[i], 'reason', reason
            ));
        ELSIF EXISTS (SELECT 1 FROM contacts WHERE username = current_name) THEN
            UPDATE contacts SET phone = current_phone WHERE username = current_name;
        ELSE
            INSERT INTO contacts(username, phone) VALUES (current_name, current_phone);
        END IF;
    END LOOP;

    p_invalid := invalid_rows;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_contacts(
    IN p_username TEXT DEFAULT NULL,
    IN p_phone TEXT DEFAULT NULL
)
LANGUAGE plpgsql AS $$
BEGIN
    IF (p_username IS NULL) = (p_phone IS NULL) THEN
        RAISE EXCEPTION 'specify exactly one of username or phone';
    END IF;
    IF p_username IS NOT NULL THEN
        DELETE FROM contacts WHERE username = p_username;
    ELSE
        DELETE FROM contacts WHERE phone = p_phone;
    END IF;
END;
$$;
