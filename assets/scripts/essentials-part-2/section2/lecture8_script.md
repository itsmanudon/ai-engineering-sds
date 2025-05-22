---
lecture: Lecture8
lecture_title: HF Datasets in Practice
duration: 15 min
---

## 00:00 – Hook (30 s)
> "Ever tried to download a dataset and watched your computer freeze? There’s a better way! In this session, you’ll learn how to stream, filter, and transform huge datasets efficiently—so you can focus on building, not babysitting your RAM."

## 00:30 – Learning goals
- Load datasets from the Hugging Face Hub ✅
- Stream and filter large datasets efficiently ✅
- Apply memory-safe transforms and batching ✅

## 01:00 – Demo setup
_(Switch to notebook cell 1)_

- Import the `datasets` library.
- Load a sample dataset (e.g., `imdb` or `ag_news`).
- Show the dataset structure and basic info.

## 04:00 – Streaming and filtering
- Load a dataset in streaming mode (no full download).
- Filter for specific labels or keywords.
- Show how streaming lets you work with huge datasets on limited hardware.

## 08:00 – Memory-safe transforms
- Use `.map()` to apply a transformation (e.g., lowercase text, remove punctuation).
- Demonstrate that transforms can be lazy and memory-efficient.

## 11:00 – Batching and iteration
- Batch examples for efficient processing.
- Iterate over batches and show how to use them in a training loop.

## 13:30 – Take-aways
"Hugging Face Datasets make it easy to work with massive datasets—stream, filter, and transform without breaking your RAM."

## Call-to-Action
"Try streaming a dataset from the Hub, apply a filter or transform, and share your code snippet in the course repo!"
