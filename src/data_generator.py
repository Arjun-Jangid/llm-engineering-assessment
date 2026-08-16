import json
import random
from datetime import datetime, timedelta
from pathlib import Path


SUPPLIERS = [
    "Meridian Supplies",
    "ABC Traders",
    "Global Warehouse",
    "Tech Parts Ltd",
    "Prime Logistics"
]


def generate_inventory_records(num_records=350):
    random.seed(42)

    records = []
    stock = 1000
    start_date = datetime(2026, 1, 1)

    for i in range(1, num_records + 1):

        date = start_date + timedelta(
            days=random.randint(0, 180)
        )

        supplier = random.choice(SUPPLIERS)

        movement = random.choice(["in", "out"])

        quantity = random.choice(
            [50, 100, 200, 300, 450, 500]
        )

        if movement == "in":
            stock += quantity
        else:
            if stock - quantity >= 0:
                stock -= quantity
            else:
                movement = "in"
                stock += quantity

        record = {
            "record_id": f"R{i:05d}",
            "date": date.strftime("%Y-%m-%d"),
            "supplier": supplier,
            "movement": movement,
            "quantity": quantity,
            "stock_after": stock
        }

        records.append(record)

    return records


if __name__ == "__main__":

    output_path = Path("data/inventory.json")
    data = generate_inventory_records()

    output_path.parent.mkdir(
        exist_ok=True
    )

    with open(output_path, "w") as file:
        json.dump(
            data,
            file,
            indent=2
        )

    print(f"{len(data)} records generated successfully at {output_path}")