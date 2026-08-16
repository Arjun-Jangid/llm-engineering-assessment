from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer("all-MiniLM-L6-v2")


def record_to_text(record):
    return (
        f"{record['supplier']} "
        f"{record['date']} "
        f"{record['movement']} "
        f"{record['quantity']}"
    )


def create_embeddings(records):
    texts = [
        record_to_text(record)
        for record in records
    ]

    return model.encode(
        texts,
        normalize_embeddings=True
    )


def exact_match_score(question, record):
    score = 0

    question = question.lower()

    if record["supplier"].lower() in question:
        score += 3

    if record["date"] in question:
        score += 5

    if str(record["quantity"]) in question:
        score += 5

    if record["movement"] in question:
        score += 2

    return score


def retrieve(question, records, embeddings):

    question_embedding = model.encode(
        question,
        normalize_embeddings=True
    )

    similarities = cosine_similarity(
        [question_embedding],
        embeddings
    )[0]


    # top_indices = similarities.argsort()[-5:][::-1]
    # top_indices = similarities.argsort()[-10:][::-1]
    top_indices = similarities.argsort()[-20:][::-1]


    best_record = None
    best_score = -1


    for index in top_indices:

        record = records[index]

        final_score = (
            similarities[index] * 10
            +
            exact_match_score(question, record)
        )

        if final_score > best_score:
            best_score = final_score
            best_record = record


    return best_record, best_score