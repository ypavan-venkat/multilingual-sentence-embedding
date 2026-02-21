# Multilingual Sentence Embedding & Similarity

## Overview
This project demonstrates multilingual semantic similarity using Sentence Transformers.
It generates contextual embeddings for sentences across English and Indian languages
and computes semantic similarity using cosine similarity.

## Objective
To understand how multilingual transformer-based models generate embeddings
that capture semantic meaning across languages.

## Model Used
paraphrase-multilingual-MiniLM-L12-v2  
(Sentence Transformers - HuggingFace)

## Features
- Generates multilingual sentence embeddings
- Supports English, Hindi, Telugu (extendable)
- Computes cosine similarity between sentence pairs
- Demonstrates cross-lingual semantic alignment

## Example Sentences Used
- "I love artificial intelligence."
- "मुझे कृत्रिम बुद्धिमत्ता पसंद है।"
- "నాకు కృత్రిమ మేధస్సు ఇష్టం."
- "I play cricket every day."

## How It Works
1. Load multilingual transformer model
2. Encode sentences into dense vector embeddings
3. Compute cosine similarity matrix
4. Analyze semantic similarity scores

## Applications
- Multilingual search engines
- Cross-lingual NLP systems
- Low-resource language modeling
- Semantic similarity analysis

## Tech Stack
- Python
- Sentence Transformers
- Scikit-learn
- PyTorch

## Future Improvements
- Add visualization (heatmap)
- Deploy using Streamlit
- Extend to more Indian languages
- Implement contrastive fine-tuning

---
