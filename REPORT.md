# LLM Engineering Assessment Report

## 1. Overview

This project implements an inventory retrieval system for answering questions over structured inventory movement records.

The system was built in two stages:

1. A baseline token-overlap retriever was implemented to establish initial retrieval performance.
2. A hybrid retriever was developed using SentenceTransformer embeddings with field-aware reranking to improve retrieval accuracy.

## 2. Dataset

A synthetic inventory dataset was generated containing 350 inventory movement records.

Each record contains:

- record_id
- date
- supplier
- movement (in/out)
- quantity
- stock_after

An evaluation dataset containing 100 questions was created to measure retrieval performance.

## 3. Baseline Retriever

The baseline retriever uses a simple token-overlap approach.

Approach:

- Convert the user query into tokens.
- Convert inventory records into searchable text.
- Compare overlapping tokens between the query and records.
- Return the record with the highest matching score.

Baseline result:

| Retriever              | Accuracy |
| ---------------------- | -------- |
| Token Overlap Baseline | 0.84     |

## 4. Improvements

To improve retrieval quality, a hybrid retrieval approach was implemented.

Improvements:

- Added SentenceTransformer embeddings to capture semantic similarity.
- Added field-aware reranking using exact matches.
- Prioritized structured fields:
  - supplier
  - date
  - quantity
  - movement

The hybrid approach first retrieves semantically similar candidates and then reranks them using exact field matching.

Results:

| Retriever        | Accuracy |
| ---------------- | -------- |
| Baseline         | 0.84     |
| Hybrid Retriever | 0.97     |

## 5. Evaluation

The system was evaluated using a fixed evaluation dataset.

Testing:

Three pytest cases were added:

1. Correct retrieval
   - Verifies that the system retrieves the expected record.

2. Ambiguous records
   - Tests whether the retriever can distinguish similar records using important fields.

3. No useful signal query
   - Ensures the retriever handles unrelated queries without crashing.

## 6. Limitations

Current limitations:

- Synthetic dataset
- Limited query types
- No large-scale production testing

## 7. Reasoning Answers

### How would you handle ambiguous user queries?

For ambiguous queries, I would retrieve multiple candidate records first and apply additional ranking based on important fields such as date, quantity, supplier, and movement type.
