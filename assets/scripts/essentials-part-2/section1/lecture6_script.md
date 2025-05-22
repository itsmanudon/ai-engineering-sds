---
lecture: Lecture6
lecture_title: Loading Models with `from_pretrained`
duration: 12 min
---

## 00:00 – Hook (30 s)
> "Ever wondered what *actually* happens when you run one line of code—`from_pretrained`—and a 3 GB model just ‘appears’?"

## 00:30 – Learning goals
- Pull a model ✅
- Peek inside config & weights ✅
- Understand cache & resume ✅

## 01:00 – Demo setup
_(Switch to notebook cell 1)_

- Import `transformers` library.
- Use `from_pretrained` to load a model (e.g., `bert-base-uncased`).
- Explore the model's configuration and weights.

## 06:00 – Cache management
- Explain where models are cached locally.
- Demonstrate how to clear or resume downloads.

## 10:00 – Device mapping
- Show how to map models to CPU/GPU devices.

## 11:20 – Take-aways
"`from_pretrained` is just `requests.get` + smart cache management—now you can script, automate, or swap endpoints at will."

## Call-to-Action
"Fork today’s notebook, change the model ID to your native language, and post results on the course repo."