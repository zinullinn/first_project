"""Extract structured fields from a plain-text receipt using regular expressions."""

from __future__ import annotations

import json
import re
from pathlib import Path


# Supports e.g. 1250, 1,250.00, 1 250,00, and optional currency markers.
PRICE_RE = re.compile(
    r"(?<![\w.])(?:[-+]?\s*)?(?:[$€£₸]\s*)?"
    r"(\d{1,3}(?:[ ,.]\d{3})*(?:[.,]\d{2})|\d+)(?:\s*(?:KZT|USD|EUR|GBP))?",
    re.IGNORECASE,
)
DATE_RE = re.compile(r"\b(\d{4}-\d{2}-\d{2}|\d{1,2}[/. -]\d{1,2}[/. -]\d{2,4})\b")
TIME_RE = re.compile(r"\b([01]?\d|2[0-3]):[0-5]\d(?::[0-5]\d)?\s*(?:AM|PM)?\b", re.IGNORECASE)
PAYMENT_RE = re.compile(
    r"\b(?:payment\s*(?:method)?|paid\s*by)\s*:?\s*(.+?)\s*$",
    re.IGNORECASE | re.MULTILINE,
)
TOTAL_RE = re.compile(r"^\s*(?:grand\s+)?total\s*:?\s*([^\r\n]+)", re.IGNORECASE | re.MULTILINE)


def parse_amount(text: str) -> float:
    """Convert common receipt number formats to a float."""
    value = re.sub(r"[^\d,.]", "", text)
    if "," in value and "." in value:
        decimal = "," if value.rfind(",") > value.rfind(".") else "."
        thousands = "." if decimal == "," else ","
        value = value.replace(thousands, "").replace(decimal, ".")
    elif "," in value:
        tail = value.rsplit(",", 1)[1]
        value = value.replace(",", ".") if len(tail) == 2 else value.replace(",", "")
    elif value.count(".") > 1:
        head, tail = value.rsplit(".", 1)
        value = head.replace(".", "") + "." + tail
    return float(value)


def parse_receipt(text: str) -> dict[str, object]:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    prices: list[float] = []
    products: list[dict[str, object]] = []

    for line in lines:
        match = PRICE_RE.search(line)
        if not match:
            continue
        amount = parse_amount(match.group(1))
        prices.append(amount)
        label = line[: match.start()].strip(" :-\t")
        # Keep item lines only; totals and adjustments are reported separately.
        if label and not re.search(r"\b(?:subtotal|total|tax|discount|change|cash|paid)\b", label, re.I):
            products.append({"name": label, "price": amount})

    total_match = TOTAL_RE.search(text)
    total = parse_amount(total_match.group(1)) if total_match else None
    date_match = DATE_RE.search(text)
    time_match = TIME_RE.search(text)
    payment_match = PAYMENT_RE.search(text)

    return {
        "prices": prices,
        "products": products,
        "calculated_total": round(sum(item["price"] for item in products), 2),
        "receipt_total": total,
        "date": date_match.group(1) if date_match else None,
        "time": time_match.group(0).strip() if time_match else None,
        "payment_method": payment_match.group(1).strip() if payment_match else None,
    }


def main() -> None:
    receipt_path = Path(__file__).with_name("raw.txt")
    result = parse_receipt(receipt_path.read_text(encoding="utf-8"))
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
