# LLM Engineering Assessment

## Overview

This project implements an inventory retrieval system that answers questions over structured inventory movement records.

The project includes:

- A baseline token-overlap retriever
- An improved hybrid retriever using SentenceTransformer embeddings with field-aware reranking
- Evaluation pipeline
- Retriever tests

---

## Project Structure

```text
llm-engineering-assessment/
│
├── data/
│   ├── inventory.json
│   └── eval_set.json
│
├── src/
│   ├── retriever.py
│   ├── hybrid_retriever.py
│   ├── evaluator.py
│   ├── data_generator.py
│   └── eval_generator.py
│
├── tests/
│   └── test_retriever.py
│
├── outputs/
│
├── REPORT.md
├── requirements.txt
└── README.md
```

---

## Setup

Create virtual environment:
```bash
python -m venv .venv

```

Activate:
source .venv/bin/activate

Install dependencies:
pip install -r requirements.txt

---

## Run Evaluation

python src/evaluator.py

---

## Run Tests

pytest tests -q

Expected:
3 passed
