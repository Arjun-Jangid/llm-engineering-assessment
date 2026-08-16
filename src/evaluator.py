import json
from retriever import retrieve


def load_json(path):
    with open(path) as file:
        return json.load(file)


def evaluate(eval_data, records):
    correct = 0
    total = len(eval_data)

    results = []

    for item in eval_data:
        retrieved_record, score = retrieve(
            item["question"],
            records
        )

        is_correct = (
            retrieved_record
            and retrieved_record["record_id"] == item["record_id"]
        )

        if is_correct:
            correct += 1

        results.append({
            "question": item["question"],
            "expected": item["record_id"],
            "retrieved": (
                retrieved_record["record_id"]
                if retrieved_record else None
            ),
            "score": score,
            "correct": is_correct,
        })

    with open("outputs/baseline_eval_output.json", "w") as file:
        json.dump(results, file, indent=2)

    accuracy = correct / total

    return accuracy, results



if __name__ == "__main__":

    eval_data = load_json("data/eval_set.json")
    records = load_json("data/inventory.json")

    accuracy, results = evaluate(
        eval_data,
        records
    )

    print(f"Accuracy: {accuracy:.2f}")