import re


def tokenize(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return set(text.split())


def record_to_text(record):
    return (
        f"{record['record_id']} "
        f"{record['date']} "
        f"{record['supplier']} "
        f"{record['movement']} "
        f"{record['quantity']} "
        f"{record['stock_after']}"
    )


def calculate_score(question, record):
    question_tokens = tokenize(question)
    record_tokens = tokenize(record_to_text(record))

    common_tokens = question_tokens.intersection(record_tokens)

    return len(common_tokens)


def retrieve(question, records):
    best_record = None
    best_score = 0

    for record in records:
        score = calculate_score(question, record)

        if score > best_score:
            best_score = score
            best_record = record

    return best_record, best_score