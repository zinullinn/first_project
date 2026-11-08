-- Search any part of the username or phone, case-insensitively for names.
CREATE OR REPLACE FUNCTION search_contacts(p_pattern TEXT)
RETURNS TABLE(id BIGINT, username TEXT, phone TEXT)
LANGUAGE sql STABLE AS $$
    SELECT c.id, c.username, c.phone
    FROM contacts AS c
    WHERE c.username ILIKE '%' || COALESCE(p_pattern, '') || '%'
       OR c.phone ILIKE '%' || COALESCE(p_pattern, '') || '%'
    ORDER BY c.username, c.id
$$;

-- Return a stable page; page numbers start at 1.
CREATE OR REPLACE FUNCTION get_contacts_page(p_limit INTEGER, p_offset INTEGER)
RETURNS TABLE(id BIGINT, username TEXT, phone TEXT)
LANGUAGE plpgsql STABLE AS $$
BEGIN
    IF p_limit IS NULL OR p_limit < 1 OR p_limit > 500 THEN
        RAISE EXCEPTION 'limit must be between 1 and 500';
    END IF;
    IF p_offset IS NULL OR p_offset < 0 THEN
        RAISE EXCEPTION 'offset must be zero or greater';
    END IF;
    RETURN QUERY
        SELECT c.id, c.username, c.phone
        FROM contacts AS c
        ORDER BY c.username, c.id
        LIMIT p_limit OFFSET p_offset;
END;
$$;
