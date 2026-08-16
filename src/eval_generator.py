import json
import random
from pathlib import Path


def load_inventory():
    with open("data/inventory.json", "r") as file:
        return json.load(file)


def generate_atomic_questions(records, count=100):
    random.seed(42)
    selected_records = random.sample(records, count)
    eval_data = []

    for record in selected_records:
        question = (
            f"What was the stock level after the "
            f"{record['quantity']}-unit shipment from "
            f"{record['supplier']} on {record['date']}?"
        )

        eval_data.append(
            {
                "question": question,
                "answer": record["stock_after"],
                "record_id": record["record_id"],
                "type": "atomic"
            }
        )

    return eval_data


if __name__ == "__main__":

    records = load_inventory()
    eval_set = generate_atomic_questions(records)
    output_path = Path("data/eval_set.json")

    with open(output_path, "w") as file:
        json.dump(
            eval_set,
            file,
            indent=2
        )

    print(f"{len(eval_set)} evaluation questions generated successfully.")