import json
from retriever import retrieve


with open("data/inventory.json") as file:
    records = json.load(file)


question = (
    "What was the stock level after the "
    "300-unit shipment from Meridian Supplies on 2026-06-17?"
)

result, score = retrieve(question, records)


print("Score:", score)
print("Retrieved Record:")
print(result)