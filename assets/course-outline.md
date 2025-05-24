# AI Engineering Curriculum – Master Syllabus

---

## AI Engineering Essentials – Part 1

### Section 1 · Getting Started & Local LLMs

| # | Lecture Title                    | Scope                                                           |
| - | -------------------------------- | --------------------------------------------------------------- |
| 1 | Introduction                     | Course goals, prerequisites, and the rapid-prototyping mindset. |
| 2 | Download an LLM Locally (Ollama) | Install Ollama and fetch your first open-source model.          |
| 3 | Using an LLM Locally             | Prompting, basic config, and token streaming in the terminal.   |
| 4 | Comparing Model Responses        | Side-by-side evaluation of two models on identical prompts.     |
| 5 | Course Outline Walk-through      | Big-picture tour of Sections 1–4 and the mini-project.          |

```paths
nb_root:   AI-Engineering-Essentials/Part1/section1/
script_root: assets/scripts/essentials-part-1/section1/
```

### Section 2 · Environment Setup & Secrets

| #  | Lecture Title              | Scope                                              |
| -- | -------------------------- | -------------------------------------------------- |
| 6  | Setting Up the Course Repo | Fork/clone workflow, branching, and Git etiquette. |
| 7  | Python Virtual Envs        | Create and isolate `venv` environments.            |
| 8  | Conda Virtual Envs         | Conda vs `venv`, handling GPU builds.              |
| 9  | `.env` Files               | Store secrets without committing them.             |
| 10 | OpenAI API Key             | Generate, export, and rotate keys safely.          |
| 11 | Anthropic API Key          | Same flow for Claude; rate-limit caveats.          |
| 12 | Hugging Face API Key       | Access tokens, scopes, and HF Hub uploads.         |

```paths
nb_root:   AI-Engineering-Essentials/Part1/section2/
script_root: assets/scripts/essentials-part-1/section2/
```

### Section 3 · Model Choices & Cost Awareness

| #  | Lecture Title                  | Scope                                                        |
| -- | ------------------------------ | ------------------------------------------------------------ |
| 13 | Navigating API Costs           | Compute, token, and storage cost drivers with live examples. |
| 14 | Frontier Models vs Open Source | Capability, latency, and IP trade-offs.                      |
| 15 | OpenAI Platform vs ChatGPT     | Why API ≠ UI; sandbox vs production keys.                    |
| 16 | Coding with OpenAI             | Python SDK, streaming, retries, and error handling.          |
| 17 | Anthropic Console vs Claude    | Prompt-IDE demo, system vs user roles.                       |
| 18 | Coding with Claude             | Call the Claude API in Python; JSON mode demo.               |
| 19 | Other Frontier Models          | Quick tour of Gemini, Mixtral, Groq-hosted Llama, etc.       |

```paths
nb_root:   AI-Engineering-Essentials/Part1/section3/
script_root: assets/scripts/essentials-part-1/section3/
```

### Section 4 · Applied Mini-Project

| #  | Lecture Title                           | Scope                                                |
| -- | --------------------------------------- | ---------------------------------------------------- |
| 20 | Searching the Web with LLMs             | Build a browser-search tool; legal/ethical scraping. |
| 21 | Social Media Post Generator *(Project)* | Prompt-chained builder, milestones, deliverables.    |

```paths
nb_root:   AI-Engineering-Essentials/Part1/section4/
script_root: assets/scripts/essentials-part-1/section4/
```

---

## AI Engineering Essentials – Part 2

### Section 1 · Hugging Face Workflow Basics

| # | Lecture Title                         | Scope                                               |
| - | ------------------------------------- | --------------------------------------------------- |
| 1 | HF Ecosystem Overview                 | Hub, Models, Datasets, Inference Endpoints, Spaces. |
| 2 | Hugginface Models                     | Exploring the models tab                            |
| 3 | Hugginface Datsets                    | Exploring the datasets tab                          |
| 4 | Hugginface Spaces                     | Exploring the spaces tab                            |
| 5 | Code with Huggingface on Google Colab | Getting started using the pipeline method           |
| 6 | Loading Models with `from_pretrained` | Config files, weight shards, device maps.           |

```paths
nb_root:   AI-Engineering-Essentials/Part2/section1/
script_root: assets/scripts/essentials-part-2/section1/
```


### Section 2 · Data & Finetuning

| #  | Lecture Title                         | Scope                                            |
| -- | ------------------------------------- | ------------------------------------------------ |
| 7  | HF Datasets in Practice               | Streaming, filtering, memory-safe transforms.    |
| 8  | Data Collators & Batching             | Padding strategies and GPU throughput tips.      |
| 9  | Finetuning a Causal-LM with `Trainer` | 20-line script, checkpoints, early stopping.     |
| 10 | PEFT & LoRA Intro                     | Adapter theory, VRAM savings, quick demo.        |
| 11 | Evaluating with `evaluate`            | Perplexity, BLEU, and debugging bad generations. |

```paths
nb_root:   AI-Engineering-Essentials/Part2/section2/
script_root: assets/scripts/essentials-part-2/section2/
```


### Section 3 · Sharing, Deployment & Capstone

| #  | Lecture Title                           | Scope                                              |
| -- | --------------------------------------- | -------------------------------------------------- |
| 12 | Push to the Hub                         | Versioning, model cards, private repos.            |
| 13 | Deploying a Gradio Space                | Fast CPU vs GPU endpoints, latency demo.           |
| 14 | Mini-Project Kick-off: Smart Summarizer | Project brief, dataset link, submission checklist. |

```paths
nb_root:   AI-Engineering-Essentials/Part2/section3/
script_root: assets/scripts/essentials-part-2/section3/
```

---

## AI Engineering Intermediate – Part 1

*“From fine-tuning to feature stores—upgrade your prototyping game.”*

| #  | Lecture Title                            | Scope                                                               |
| -- | ---------------------------------------- | ------------------------------------------------------------------- |
| 1  | Course Orientation & Skills Matrix       | Map the jump from Essentials to Mastery; prerequisite refresh.      |
| 2  | Beyond `Trainer`: Lightning + Accelerate | Re-implement a finetune for multi-GPU speed.                        |
| 3  | Building & Querying a Feature Store      | Spin up Feast and flow features into serving.                       |
| 4  | Data Versioning with DVC                 | Track data, models, metrics, and pipelines.                         |
| 5  | Prompt Engineering Patterns              | Chain-of-thought, RAG, self-consistency demos.                      |
| 6  | Embeddings 101 (Text & Images)           | Generate, visualise, compare with UMAP and FAISS.                   |
| 7  | Vector Databases in Action               | Deploy Qdrant; hybrid BM25 + vector search.                         |
| 8  | Building RAG Pipelines                   | End-to-end ingest → embed → query → prompt → eval.                  |
| 9  | Evaluation Beyond Accuracy               | Bias, toxicity, factuality; TruthfulQA demo.                        |
| 10 | Model Packaging with ONNX                | Export, quantize, benchmark vs FP16.                                |
| 11 | Dockerizing AI Apps                      | Multi-stage Dockerfile with GPU support.                            |
| 12 | Capstone Kick-off: RAG Chatbot           | Deliverables: loader, retriever, prompt template, Dockerized Space. |

---

## AI Engineering Intermediate – Part 2

*“Ship it for real—CI/CD, orchestration, and scalable infra.”*

| #  | Lecture Title                     | Scope                                           |
| -- | --------------------------------- | ----------------------------------------------- |
| 1  | Road-map & Capstone Preview       | How Part 2 turns prototypes into prod services. |
| 2  | CI/CD for ML with GitHub Actions  | Test, lint, train, auto-deploy to HF Spaces.    |
| 3  | Model Registry & Promotion        | MLflow stages, approvals, rollbacks.            |
| 4  | FastAPI for LLM Inference         | Wrap finetuned model with async streaming.      |
| 5  | Autoscaling with Kubernetes (K3d) | Local K3d demo, HPA on CPU/GPU usage.           |
| 6  | Secrets & Config Management       | Doppler/HF Secrets without code leaks.          |
| 7  | Monitoring & Tracing              | Prometheus + OpenTelemetry + Grafana.           |
| 8  | Canary & Shadow Deployments       | Mirror traffic, compare metrics, promote.       |
| 9  | Cost Optimization & Quantization  | 8-bit, 4-bit, LoRA adapters, cost calc.         |
| 10 | Security & PII Redaction          | Auth, rate limiting, real-time scrubber.        |
| 11 | Compliance & Model Cards 2.0      | Extended cards with dataset citations.          |
| 12 | Capstone Demo Day Prep            | Checklist: repo, CI badge, live Space URL.      |

---

## AI Engineering Advanced – Part 1

*“Designing multi-agent systems and advanced retrieval.”*

| #  | Lecture Title                                | Scope                                               |
| -- | -------------------------------------------- | --------------------------------------------------- |
| 1  | Multi-Agent Architectures                    | Compare ReAct, Auto-GPT, CrewAI message flows.      |
| 2  | Building an Agent with LangGraph             | Tool-calling graph with parallel branches.          |
| 3  | Toolformer & Function Calling                | Fine-tune to self-discover API calls; JSON schemas. |
| 4  | Advanced Retrieval                           | Hybrid, re-rank, feedback loops (ColBERT, TART).    |
| 5  | Knowledge Graph Augmented RAG                | Build Neo4j KG and combine with vectors.            |
| 6  | Streaming & Real-Time Inference              | Serve tokens via SSE/WebSockets; latency budgets.   |
| 7  | Memory for Agents                            | Episodic vs long-term memory retrievers.            |
| 8  | Planning & Scheduling Agents                 | Task specs, priority queues, reflection prompts.    |
| 9  | Self-Consistency & Self-Critique             | Adversarial critics to improve responses.           |
| 10 | Multi-Modal Agents                           | Add CLIP, TTS, STT for voice/image chats.           |
| 11 | Failure Modes & Safe-guards                  | Detect hallucinations, runaway loops, guardrails.   |
| 12 | Capstone Kick-off: Autonomous Research Agent | Scope: crawl, cite, summarise, report autonomously. |

---

## AI Engineering Advanced – Part 2

*“Enterprise-grade scaling, privacy, and governance.”*

| #  | Lecture Title                                | Scope                                              |
| -- | -------------------------------------------- | -------------------------------------------------- |
| 1  | Strategic Overview & Enterprise Requirements | SLAs, SLOs, governance checklists.                 |
| 2  | Distributed Training Strategies              | FSDP, ZeRO-3, sharding on multi-A100 nodes.        |
| 3  | Private & On-Prem Deployments                | Terraform + Ansible for air-gapped GPU cluster.    |
| 4  | Differential Privacy for LLMs                | Opacus ε-DP training; utility trade-offs.          |
| 5  | Retrieval Security                           | Per-user ACLs, tenant isolation in vector DBs.     |
| 6  | Synthetic Data Generation & Red-Teaming      | CTGAN-style rows, red-team outputs.                |
| 7  | Model Watermarking & Provenance              | Embed watermarks, verify ownership.                |
| 8  | SLA-Driven Autoscaling (KEDA)                | Event-driven scaling on token usage, latency SLOs. |
| 9  | Real-Time Feedback Loops & RLHF              | Stream user feedback to PPO reward model.          |
| 10 | Governance Dashboards                        | Streamlit admin panel: evals, bias, cost.          |
| 11 | Corporate Compliance & AI Policies           | EU AI Act, ISO 42001, GCC data laws.               |
| 12 | Final Enterprise Project                     | Deliver compliance-ready multi-agent service.      |

---

## LLM Ops – Managing Large Language Models

| # | Lecture Title                  | Scope                                                     |
| - | ------------------------------ | --------------------------------------------------------- |
| 1 | Intro to LLM Ops               | LLM Ops vs traditional MLOps; tool landscape.             |
| 2 | Telemetry & Usage Analytics    | Capture traces, token counts, prompt/response pairs.      |
| 3 | Drift Detection in LLMs        | Embedding drift, feedback signals, alerts.                |
| 4 | Continual Finetuning Pipelines | Nightly PEFT retrains via MLflow orchestration.           |
| 5 | Canary Checks & Guardrails     | Guardrails AI / yidong experiments for policy compliance. |
| 6 | Budget & Cost Governance       | Per-team quotas, chargeback tagging, anomaly alerts.      |
| 7 | Multi-Model Routing            | Route between OSS and paid APIs based on latency/quality. |
| 8 | Incident Response & Rollback   | Simulate bad push, rollback, write post-mortem.           |
| 9 | Tooling Round-up               | BentoML, Seldon, vLLM, DeepSpeed-MII, OpenLLMOps.         |

---

## AI Model Selection – Choosing the Best Fit

| # | Lecture Title               | Scope                                                          |
| - | --------------------------- | -------------------------------------------------------------- |
| 1 | Taxonomy of Model Families  | CNNs, RNNs, GNNs, Transformers, MoEs.                          |
| 2 | Metrics That Matter         | Map business constraints to latency, cost, accuracy, fairness. |
| 3 | Benchmarking Frameworks     | `lm-eval-harness`, GLUE, MMLU, custom scripts.                 |
| 4 | Hardware & Cost Constraints | Match model sizes to GPUs, edge devices, serverless limits.    |
| 5 | Tiny ML and Distillation    | DistilBERT vs BERT on sentiment; trade-offs.                   |
| 6 | Case Studies                | Three real-world stories with decision matrices.               |

---

## Fine-Tuning AI Models for Performance

| # | Lecture Title               | Scope                                                    |
| - | --------------------------- | -------------------------------------------------------- |
| 1 | Finetuning Taxonomy         | Supervised, RLHF, DPO, RAG-augmented finetuning.         |
| 2 | LoRA & PEFT Recap           | Rank, α, dropout hyper-params; grid search.              |
| 3 | Full-Parameter vs Adapter   | Benchmark VRAM, speed, quality.                          |
| 4 | Hyperparameter Optimization | Optuna sweep; Pareto frontier visualisation.             |
| 5 | Curriculum & Data Weighting | Token-based sampling, difficulty scoring.                |
| 6 | Evaluation & Ablation       | Design ablations: data size, prompt suffix, RLHF vs DPO. |
| 7 | Post-Training Optimization  | Quant-aware training, knowledge distillation.            |
| 8 | Deployment Considerations   | How finetune choices hit latency, cost, memory.          |

---

## AI Without Code – Build Smarter, Faster

| # | Lecture Title                     | Scope                                                         |
| - | --------------------------------- | ------------------------------------------------------------- |
| 1 | No-Code Landscape                 | Bubble, Zapier, n8n, Make, HF Spaces UI.                      |
| 2 | Prompt-Only Workflows             | Zapier “AI Email Reply” chain using prompts.                  |
| 3 | Drag-and-Drop RAG                 | Build Q\&A bot in Flowise; Pinecone + OpenAI keys.            |
| 4 | AI Agents in ReTool & Superblocks | Multi-step form calling LLM & SQL—no backend code.            |
| 5 | Custom Components with Low-Code   | Extend n8n with custom TypeScript node for HF inference.      |
| 6 | Deploy & Monitor                  | Publish app, logging, usage throttling via platform settings. |

