---
lecture: Lecture8
lecture_title: Building a Custom Tokenizer
duration: 15 min
---

## 00:00 – Hook (30 s)
> "What if you could build your own tokenizer tailored to your dataset? Let’s do it!"

## 00:30 – Learning goals
- Train a Byte Pair Encoding (BPE) tokenizer ✅
- Save and load a custom tokenizer ✅
- Compare vocabularies ✅

## 01:00 – Demo setup
_(Switch to notebook cell 1)_

- Import `tokenizers` library.
- Load a small text dataset.
- Initialize a BPE tokenizer.

## 05:00 – Training the tokenizer
- Train the tokenizer on the dataset.
- Save the tokenizer to disk.

## 10:00 – Using the custom tokenizer
- Load the tokenizer.
- Tokenize a sample sentence.
- Compare the vocabulary with a pre-trained tokenizer.

## 14:30 – Take-aways
"Custom tokenizers give you control over vocab size and token splits—perfect for domain-specific tasks."

## Call-to-Action
"Train a tokenizer on your own dataset and share the vocab size and token splits in the course repo."
