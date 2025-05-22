---
lecture: Lecture7
lecture_title: Tokenization Deep Dive
duration: 15 min
---

## 00:00 – Hook (30 s)
> "What’s the magic behind tokenization? Let’s break down how your text becomes numbers."

## 00:30 – Learning goals
- Understand BPE tokenization ✅
- Explore attention masks ✅
- Tokenize a French sentence ✅

## 01:00 – Demo setup
_(Switch to notebook cell 1)_

- Import `AutoTokenizer` from `transformers`.
- Load a tokenizer (e.g., `bert-base-uncased`).
- Tokenize a simple English sentence.

## 05:00 – BPE mechanics
- Explain Byte Pair Encoding (BPE).
    Byte Pair Encoding (BPE) is a simple data compression and tokenization algorithm. In natural language processing (NLP), BPE is used to split words into subword units, which helps handle rare or unknown words.

    How BPE works:

    Start with a list of all characters in your text as the initial vocabulary.
    Find the most frequent pair of adjacent symbols (characters or subwords).
    Merge this pair into a new symbol.
    Repeat steps 2–3 for a set number of merges or until no pairs remain.
    Why use BPE in NLP?

    It reduces the vocabulary size.
    It allows models to handle out-of-vocabulary words by breaking them into known subwords.
    It balances between character-level and word-level representations.
    Example: Suppose you have the words: low, lower, newest, widest.

    After several BPE merges, you might get subwords like: low, er, new, est, wid, est.

- Visualize token splits for a complex word.
    - Pick a complex word (e.g., "unbelievable").
    - Use the tokenizer to encode the word and display the resulting tokens.
    - Show both the token IDs and their corresponding subword strings.
    - Discuss how BPE splits the word into meaningful subword units.
- Example:
    ```python
    word = "unbelievable"
    tokens = tokenizer.tokenize(word)
    token_ids = tokenizer.convert_tokens_to_ids(tokens)
    print("Tokens:", tokens)
    print("Token IDs:", token_ids)
    ```
- Show the output and highlight how the word is broken down.

## 08:00 – Attention masks
- Show how attention masks are generated.
- Explain their role in handling padding.

## 12:00 – Multilingual example
- Tokenize a French sentence.
- Compare tokenization results across different models.

## 14:30 – Take-aways
"Tokenization is the first step in NLP magic—understanding it helps you debug and optimize your pipelines."

## Call-to-Action
"Try tokenizing a sentence in your native language and share your findings in the course repo."
