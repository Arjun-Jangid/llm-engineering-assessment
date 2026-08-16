from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer("all-MiniLM-L6-v2")


def record_to_text(record):
    return (
        f"Record id {record['record_id']}. "
        f"Date {record['date']}. "
        f"Supplier {record['supplier']}. "
        f"Movement {record['movement']}. "
        f"Quantity {record['quantity']}."
    )


def create_embeddings(records):
    texts = [
        record_to_text(record)
        for record in records
    ]

    embeddings = model.encode(
        texts,
        normalize_embeddings=True
    )

    return embeddings


def retrieve(question, records, record_embeddings):
    question_embedding = model.encode(
        question,
        normalize_embeddings=True
    )

    similarities = cosine_similarity(
        [question_embedding],
        record_embeddings
    )[0]

    best_index = similarities.argmax()

    return (
        records[best_index],
        float(similarities[best_index])
    )