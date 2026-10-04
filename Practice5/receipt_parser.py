"""Extract structured fields from the EUROPHARMA receipt with regular expressions."""

from __future__ import annotations

import json
import re
from pathlib import Path


ITEM_RE = re.compile(
    r"^\s*(\d+)\.\s*\r?\n"
    r"(.*?)\r?\n"
    r"([\d ]+,\d{2})\s*x\s*([\d ]+,\d{2})\s*\r?\n"
    r"([\d ]+,\d{2})\s*\r?\nСтоимость\s*\r?\n([\d ]+,\d{2})",
    re.MULTILINE,
)
DATE_TIME_RE = re.compile(
    r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})",
    re.IGNORECASE,
)
TOTAL_RE = re.compile(r"ИТОГО\s*:\s*([\d ]+,\d{2})", re.IGNORECASE)
PAYMENT_RE = re.compile(r"Банковская карта\s*:\s*\r?\n\s*([\d ]+,\d{2})", re.IGNORECASE)


def parse_amount(value: str) -> float:
    """Parse Russian receipt amounts such as ``18 009,00``."""
    return float(value.replace(" ", "").replace(",", "."))


def parse_receipt(text: str) -> dict[str, object]:
    products: list[dict[str, object]] = []
    for match in ITEM_RE.finditer(text):
        number, name, quantity, unit_price, line_amount, _cost = match.groups()
        products.append(
            {
                "number": int(number),
                "name": " ".join(name.split()),
                "quantity": parse_amount(quantity),
                "unit_price": parse_amount(unit_price),
                "price": parse_amount(line_amount),
            }
        )

    date_time = DATE_TIME_RE.search(text)
    total_match = TOTAL_RE.search(text)
    payment_match = PAYMENT_RE.search(text)
    prices = [item["price"] for item in products]

    return {
        "prices": prices,
        "products": products,
        "calculated_total": round(sum(prices), 2),
        "receipt_total": parse_amount(total_match.group(1)) if total_match else None,
        "date": date_time.group(1) if date_time else None,
        "time": date_time.group(2) if date_time else None,
        "payment_method": "Банковская карта" if payment_match else None,
        "payment_amount": parse_amount(payment_match.group(1)) if payment_match else None,
    }


def main() -> None:
    receipt_path = Path(__file__).with_name("raw.txt")
    result = parse_receipt(receipt_path.read_text(encoding="utf-8-sig"))
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
