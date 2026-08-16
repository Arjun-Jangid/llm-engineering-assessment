import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from hybrid_retriever import create_embeddings, retrieve


def test_correct_retrieval():
    records = [
        {
            "record_id": "R001",
            "date": "2026-05-12",
            "supplier": "Prime Logistics",
            "movement": "in",
            "quantity": 300,
            "stock_after": 3150
        }
    ]

    embeddings = create_embeddings(records)

    question = (
        "What was the stock level after the "
        "300-unit shipment from Prime Logistics on 2026-05-12?"
    )

    result, score = retrieve(
        question,
        records,
        embeddings
    )

    assert result["record_id"] == "R001"


def test_ambiguous_records():
    records = [
        {
            "record_id": "R001",
            "date": "2026-05-12",
            "supplier": "Prime Logistics",
            "movement": "in",
            "quantity": 300,
            "stock_after": 3150
        },
        {
            "record_id": "R002",
            "date": "2026-06-12",
            "supplier": "ABC Traders",
            "movement": "in",
            "quantity": 300,
            "stock_after": 5000
        }
    ]

    embeddings = create_embeddings(records)

    question = (
        "What was the stock level after the "
        "300-unit shipment from Prime Logistics on 2026-05-12?"
    )

    result, score = retrieve(
        question,
        records,
        embeddings
    )

    assert result["record_id"] == "R001"


def test_no_useful_signal_does_not_crash():
    records = [
        {
            "record_id": "R001",
            "date": "2026-05-12",
            "supplier": "Prime Logistics",
            "movement": "in",
            "quantity": 300,
            "stock_after": 3150
        }
    ]

    embeddings = create_embeddings(records)

    question = "Tell me something about the warehouse"

    result, score = retrieve(
        question,
        records,
        embeddings
    )

    assert result is not None