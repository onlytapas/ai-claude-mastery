# Chapter notes — what each chapter must cover

Already written (don't repeat them; link to them instead): ch1–ch8 (AI history), ch14 (tokens), ch63–ch76 (Claude Code mastery and the command reference), ch83 (MCP in Claude Code), ch85–ch86 (APIs/HTTP/JSON; first Claude API call), ch96–ch105 (MCP, tokens and connected automation, including ch97 keys/access tokens/OAuth/secrets, ch101 Playwright MCP, ch100 Jira MCP), ch117–ch128 (AI-Powered QA, including ch124 evals and ch125 value/ROI).

## Part II · How AI actually works (ch9–ch25)
Every chapter starts in plain words. Go deep in "Under the hood" sections.
- **ch9 The map:** AI ⊃ ML ⊃ deep learning ⊃ generative AI ⊃ LLMs. What a "model" is. Training vs inference. Where everyday products sit. A glossary-building lab.
- **ch10 Three ways machines learn:** supervised, unsupervised, reinforcement learning, with everyday and QA examples (defect classification, clustering logs, game agents). Self-supervised learning as the bridge to LLMs.
- **ch11 Neural networks:** neurons, weights, biases and activation functions (ReLU, sigmoid). A tiny network worked by hand with numbers. Layers, parameters, forward pass. A runnable Python/NumPy-free toy.
- **ch12 How a network learns:** loss functions, gradient descent (the foggy-hill analogy), learning rate, backpropagation step by step with a 2-weight example. Epochs, batches, overfitting vs underfitting, validation sets. Python toy that learns.
- **ch13 Data:** datasets, labelling, cleaning, splits (train/validation/test), bias in data, data quality as a QA problem, synthetic data, copyright and consent debates (labelled as debate), how LLM training data is gathered at a high level.
- **ch15 Embeddings:** words and sentences as vectors, meaning-as-distance, cosine similarity worked example, dimensions, sentence embeddings, uses (search, clustering, duplicate bug detection). Lab computing similarity (Python), noting which embedding providers exist (verify; Anthropic recommends a partner provider — check docs).
- **ch16 The Transformer, step by step:** the plain-language idea → tokens and embeddings → positional encoding → self-attention with Q/K/V explained with a worked mini example → softmax → multi-head attention → feed-forward → residuals and layer norm → stacking blocks → the output layer and next-token probabilities → encoder vs decoder vs decoder-only. Many diagrams. The most important technical chapter: be clear and correct.
- **ch17 Pre-training:** the next-token objective, data mixtures, scale (parameters, tokens, compute), what is learned, cost at a high level, temperature/sampling at inference (note Anthropic's API no longer exposes temperature as of 2026-10-21, per ch86), base vs chat models, knowledge cutoff.
- **ch18 Post-training:** supervised fine-tuning, RLHF (reward model, preference pairs), RLAIF, Constitutional AI (Anthropic's paper Dec 2022 and the Jan 2026 constitution — research file), Direct Preference Optimisation briefly, safety training, the helpful-honest-harmless trade-offs.
- **ch19 Reasoning models and thinking time:** chain-of-thought, test-time/inference-time compute, reinforcement learning for reasoning (DeepSeek-R1 as a public example), extended/adaptive thinking and effort in Claude (verify in research), when thinking helps and when it wastes time, and the cost/latency trade-off.
- **ch20 Context windows and memory:** what's in the window, sizes (current Claude: 1M tokens — research), "lost in the middle" and quality degradation, compaction, memory features (Claude apps memory, CLAUDE.md, auto memory) as context injection, prompt caching in brief (point to ch89), practical hygiene.
- **ch21 Multimodal AI:** images (vision encoders at a high level), PDFs, charts, screenshots for QA, audio and speech, video, image generation vs understanding, limits (counting objects, small text), privacy of screenshots.
- **ch22 Hallucinations:** why they happen (plausibility vs truth, training incentives, gaps, sycophancy), types, how to reduce them (grounding, RAG, citations, tools, asking for uncertainty, verification), how to test for them (QA lab), and the honesty training of models.
- **ch23 Retrieval, RAG and vector databases (concepts):** why RAG exists, the pipeline (ingest → chunk → embed → store → retrieve → generate with citations), vector databases and similarity search, keyword vs semantic vs hybrid. Conceptual only; ch92 is production RAG and ch94 is the project.
- **ch24 Measuring AI: evaluations and benchmarks:** what benchmarks are, the major ones (MMLU, GPQA, SWE-bench Verified/Pro, ARC-AGI, Humanity's Last Exam, Terminal-Bench, Arena — use research/ai-industry-facts.md), contamination, saturation, leaderboards, why your own evals matter (link ch124, ch36).
- **ch25 Serving AI:** GPUs/TPUs/Trainium at a plain level, memory bandwidth, data centres and energy, inference cost per token, latency vs throughput, batching, why prices differ by model, what this means for users. Deep hardware detail belongs in Optional ch137.

## Part III · The AI industry (ch26–ch30)
Use `research/ai-industry-facts.md`. Every company fact gets a source and a "Verified 9 Nov 2026" date. Present companies neutrally.
- **ch26 How the industry fits together:** the stack (chips → cloud → model labs → platforms → applications), research labs vs foundation-model developers vs cloud providers vs application companies vs coding platforms, open vs closed ecosystems, partnerships and money flows, the 2026 consolidation (SpaceX–xAI, SpaceX–Cursor, NVIDIA–Hugging Face pending, Microsoft–OpenAI deal rewritten).
- **ch27 OpenAI:** history and founding, structure, the GPT line through GPT-6 Astra / 6.1 Sol and Terra, products (ChatGPT, Codex, API), research contributions, partnerships, business model, strengths and limits.
- **ch28 Google DeepMind and Microsoft:** DeepMind history (AlphaGo, AlphaFold), the Transformer origin, Gemini through Gemini 4 Argon, Gemma, Antigravity CLI replacing Gemini CLI for individuals; Microsoft Copilot, the MAI models, Azure/Foundry (which hosts Claude too), and the OpenAI relationship.
- **ch29 Meta, NVIDIA and Amazon:** Llama's open-weights era and the shift to the mostly proprietary Muse family (Apr 2026); NVIDIA's GPUs, CUDA, Nemotron and the Hugging Face deal; AWS Bedrock, Nova, Trainium, and the Anthropic partnership.
- **ch30 xAI, DeepSeek, Mistral, Qwen and the wider field:** each with founding, models, open/closed status and position, plus short entries for Cohere, Perplexity, Hugging Face, Moonshot (Kimi), Zhipu (GLM) and Apple. A comparison table.

## Part IV · Understanding and comparing models (ch31–ch36)
- **ch31 Why there are so many models:** sizes and tiers, fast vs reasoning, general vs specialised (coding, embeddings, vision), versions and deprecation, pricing tiers.
- **ch32 Open-weight versus proprietary:** definitions (open weights ≠ open source), licences, running locally, privacy and control, safety debates (labelled), and when each fits a company.
- **ch33 Reading model cards and benchmarks critically:** what a model card / system card contains, how to read benchmark claims, cherry-picking, contamination, "SOTA" marketing, a red-flags checklist.
- **ch34 The major model families compared:** comparison tables across Claude, GPT, Gemini, Grok, Muse/Llama, DeepSeek, Mistral and Qwen by context size, modalities, tool use, agentic and coding strength, open/closed, price band. Only verified facts, dated. No declared "winner".
- **ch35 Choosing a model: real scenarios:** 10+ scenarios (bulk ticket triage, long contract review, coding agent, on-prem requirement, low latency chat, cost-capped CI job, vision on screenshots), with reasoning and trade-offs.
- **ch36 Testing and comparing models yourself (new):** a repeatable framework: define tasks, build a representative dataset, identical prompts, grading (code checks, rubric, LLM judge), measure accuracy, reasoning quality, hallucination rate, latency, tokens and cost, repeat runs for consistency, regression when models change, and a decision record. A complete runnable Python harness comparing two Claude models (and optionally another provider) via APIs, with expected output and troubleshooting.

## Part V · Anthropic and the Claude ecosystem (ch37–ch42)
Use `research/anthropic-claude-facts.md` heavily.
- **ch37 Anthropic:** founding (2021) and the official co-founder list, Public Benefit Corporation, Long-Term Benefit Trust, investors and cloud partners (Amazon, Google, Microsoft/NVIDIA), mission, headquarters, latest funding (Series H) with dates. Flag anything the research marks unverified.
- **ch38 Safety research:** Constitutional AI and the 2026 constitution, the Responsible Scaling Policy (version history to 3.4, ASL-3 activation May 2025), interpretability (monosemanticity, Golden Gate Claude, circuit tracing), alignment research (alignment faking, agentic misalignment), model welfare, Project Glasswing and Mythos. Explain plainly why each matters.
- **ch39 Claude through the generations:** the full timeline from Claude 1 to the 5.5 family, with what changed each time, plus retirements and deprecations.
- **ch40 The Claude models today and how to choose:** Fable 5.1 / Opus 5.5 / Sonnet 5.5 / Haiku 5.5: what Fable is (and Mythos), context, output, prices, effort defaults, thinking. Anthropic's "start with Opus 5.5" guidance. Choosing for QA tasks. Dated.
- **ch41 Model, app, Claude Code, API — how the pieces fit:** model vs harness vs app vs API vs Agent SDK vs MCP vs cloud platforms, with a single clear diagram. Where your data goes in each.
- **ch42 Claude for organisations:** plans (Free, Pro, Max, Ultra, Team, Enterprise — from research, dated, "check current pricing"), admin console, SSO/SCIM, data handling and retention options, managed settings for Claude Code, connectors policy, usage analytics, and that features vary by plan, region and admin.

## Part VI · Mastering the Claude apps (ch43–ch51)
Mark UI locations as liable to change, and date them.
- **ch43 Getting started with Claude:** account, the interface, starting and managing conversations, choosing a model, thinking/effort options, settings, incognito, keyboard tips, usage limits.
- **ch44 Prompting well — fundamentals:** clarity, context, task, constraints, format, examples, XML tags, iterating; before/after examples from QA work; a prompt checklist.
- **ch45 Prompting well — advanced:** role and system-style instructions, chain prompts, few-shot design, structured output, self-critique, prompt templates, meta-prompting, avoiding injection-prone designs; links to ch88 (context engineering).
- **ch46 Files, images, PDFs and spreadsheets:** what can be uploaded, limits, analysis of CSV/Excel, creating files (Word/Excel/PowerPoint/PDF via skills), screenshots for bugs, privacy.
- **ch47 Projects:** knowledge, instructions, sharing in Team/Enterprise, a QA project setup walkthrough.
- **ch48 Artifacts:** what they are, kinds, publishing and sharing, interactive tools for QA (checklists, dashboards), limits.
- **ch49 Research, web search and connectors:** web search, Research mode, citations, connectors (directory, custom, Google Drive, Jira, GitHub, Slack), admin controls; link ch99.
- **ch50 Memory, styles and personalisation:** memory, profile preferences, styles (check whether styles still exist; the research flags this as uncertain), incognito, managing what Claude remembers.
- **ch51 Desktop, mobile, browser and other apps:** desktop app, mobile, Claude in Chrome, Claude in Excel/Office and Slack (only as verified), voice, sharing and exporting.

## Part VII · The terminal from zero (ch52–ch62)
For people who have never used a terminal. macOS first, with Linux and Windows notes. Explain what every output means.
- **ch52 Operating systems, terminals and shells:** OS, GUI vs CLI, terminal vs shell vs command prompt, zsh/bash/PowerShell, opening one on each OS, anatomy of a prompt.
- **ch53 Files, folders and paths:** filesystem tree, home (~), absolute vs relative paths, . and .., hidden files, file extensions, case sensitivity, spaces and quoting.
- **ch54 Your first commands:** pwd, ls (with options), cd, mkdir, touch, cp, mv, rm (with safety), cat, less, head, tail, open, nano, clear, history, man and --help. Syntax, options and arguments explained, with a big lab.
- **ch55 Searching, pipes and redirection:** grep, find, wc, sort, uniq; stdin/stdout/stderr; |, >, >>, 2>, &&, ||, ;; exit codes ($?). QA examples on logs.
- **ch56 Environment variables, processes and permissions:** env, export, PATH, .zshrc, which; ps, top, kill, background jobs (&, jobs, fg); chmod and file permissions, sudo with caution; curl and wget basics.
- **ch57 Shell scripting basics:** a first script, shebang, variables, arguments, if, loops, functions, exit codes, a QA script (run tests, collect a report).
- **ch58 Package managers, Node.js and Python setup:** Homebrew, npm/npx, node versions (nvm), pip and venv/uv (verify), what installing does, global vs local, lock files.
- **ch59 Python fundamentals for AI work (new):** a practical crash course: running Python, variables, strings, lists, dicts, loops, functions, modules, reading and writing files, JSON, exceptions, virtual environments, reading tracebacks. QA-flavoured exercises (parse a JUnit XML, summarise a CSV). Runnable code.
- **ch60 Python for APIs (new):** HTTP with `requests` and `httpx`, JSON in and out, authentication headers from environment variables, error handling and retries with backoff, timeouts, pagination, async basics (async/await with httpx) and why it matters for AI calls, a small runnable API client for a public test API, and debugging tips.
- **ch61 Git and GitHub from zero:** what version control is, repositories, commits, branches, merges, remotes, clone/pull/push, PRs, .gitignore, SSH keys vs HTTPS tokens (link ch97), GitHub basics. Big lab.
- **ch62 Reading errors and fixing problems:** reading error messages, command not found, permission denied, no such file, port in use, network errors, using --help/man, searching errors safely, asking Claude for help effectively.

## Part X · Configuring and extending Claude Code (ch77–ch84; ch83 MCP already written)
Use `research/claude-code-config.md` and `local-cli-help.md` exactly.
- **ch77 CLAUDE.md and memory:** all locations and precedence, imports, CLAUDE.local.md, AGENTS.md fallback, /memory, auto memory, writing a good one, team examples, anti-patterns.
- **ch78 Settings and permissions:** settings files and precedence, key settings, permission rule syntax (allow/ask/deny; Bash, Read, Edit, WebFetch, mcp__…), modes, /permissions, /update-config, /fewer-permission-prompts, examples for a test repo.
- **ch79 Sandboxing:** what it is, enabling it, filesystem and network restrictions, what it doesn't cover (e.g. local MCP servers), with auto mode.
- **ch80 Skills and custom commands:** SKILL.md format and frontmatter, locations, invocation (automatic and /name), supporting files and scripts, arguments, .claude/commands merged into skills, skill-creator, testing skills, three QA skills built end to end.
- **ch81 Subagents:** file format and fields, built-in subagents, locations, tool restrictions, models, when to delegate, a QA reviewer and a log-analyst subagent, the /agents change.
- **ch82 Hooks:** every hook event (from research), the five hook types, matchers, input/output JSON, exit codes and blocking, examples (lint after edit, block edits to src/, notify, inject context), security.
- **ch84 Plugins, team setup and choosing the right tool:** plugin structure, plugin.json, marketplaces, `claude plugin` subcommands (validate, install, enable, details, eval), output styles and status line, a team starter kit, and a decision table: CLAUDE.md vs skill vs subagent vs hook vs MCP vs plugin vs settings.

## Part XI · Building with AI APIs (ch85–ch95; ch85–86 written)
Use the Claude API facts from ch86 and the research (API version 2026-10-21, no temperature, auth headers).
- **ch87 Conversations, system prompts and streaming:** multi-turn message arrays, system prompts, stop reasons, streaming events (SSE) with SDK examples, building a CLI chat in Python.
- **ch88 Context engineering for AI applications (new):** context engineering vs prompt engineering; building context (instructions, examples, retrieved docs, tool results, memory, state); ordering and long-context placement; prompt templates and versioning; structured outputs; injection-resistant design (separating instructions from data, delimiting untrusted content, least-privilege tools); context budgets; testing and optimising prompts with evals (link ch124). A worked example evolving a test-case-generator prompt through measured versions.
- **ch89 Tool use and structured outputs:** tool definitions and JSON Schema, the tool-use loop, parallel tools, errors, forced tool choice (Fable caveat from research), structured outputs / JSON schema output (verify current feature), a runnable QA example (a tool that queries test results).
- **ch90 Caching, rate limits, errors and cost:** prompt caching mechanics and pricing multipliers (verify), batch processing, rate-limit headers and tiers, retries with backoff, error types, cost estimation and monitoring, a cost-calculator script.
- **ch91 The OpenAI and Gemini APIs compared:** request shapes side by side (verify current official docs), SDKs, tool calling, structured output, pricing models, and portability tips. Note any differences honestly.
- **ch92 Production RAG (new):** ingestion (PDF/HTML/Confluence), cleaning, chunking strategies and sizes, metadata, embeddings, vector stores, hybrid search (BM25 + vectors), reranking, contextual retrieval (check Anthropic's published technique), citations, access control and permissions, freshness and re-indexing, evaluation (retrieval recall/precision, answer faithfulness), cost, and failure modes.
- **ch93 Project: build a RAG assistant:** a complete, runnable, local-first project (Python): ingest a folder of docs, chunk, embed (a verified free/local option, e.g. a sentence-transformers model, or an API option), store (e.g. SQLite/Chroma, verified), hybrid retrieve, answer with Claude citing sources, plus an eval script. Setup, all code, expected output and troubleshooting.
- **ch94 Project: build a QA helper app:** a complete runnable small app (Python, FastAPI or CLI) that takes a user story, generates test cases with structured output, flags ambiguities, exports CSV, with tests and an eval.
- **ch95 LLMOps (new):** logging and tracing AI calls, observability tools (verify names neutrally, e.g. OpenTelemetry GenAI conventions), prompt and model versioning, evaluation gates in CI, monitoring quality drift and cost, handling model deprecations (Anthropic's schedule), incident management for AI features, and a runbook template.

## Part XIII · Agentic AI (ch106–ch112)
- **ch106 What makes an agent:** the loop (perceive, plan, act, observe), tools, memory, autonomy levels, agents vs workflows (cite Anthropic's "Building effective agents" guidance if verified), where agents fail.
- **ch107 Agent design patterns:** prompt chaining, routing, parallelisation, orchestrator–workers, evaluator–optimiser, plan-and-execute, reflection, with diagrams and when to use each.
- **ch108 Production agents (new):** state management, memory (short and long-term), retries and idempotency, timeouts, human approval gates for consequential actions, permissions and least privilege, observability and tracing, cost and budget controls, failure recovery and safe rollback, testing agents. A runnable agent that completes a real multi-step task (e.g. triage a folder of test reports and draft a summary with approval before writing).
- **ch109 Building agents with the Claude Agent SDK:** packages (verify Python/TS names and current API), query loop, tools, MCP, permissions, hooks, a runnable QA agent.
- **ch110 Multi-agent systems:** orchestrator and subagents, handoffs, shared state, costs, when not to, Claude Code subagents and background sessions as examples.
- **ch111 Browser automation and computer use:** computer use API (verify current tool versions), Claude in Chrome, Playwright MCP vs computer use vs scripted tests, safety and sandboxing.
- **ch112 Supervising agents:** human-in-the-loop design, approval UX, audit logs, evaluation of agents (task success, trajectories), red-teaming, rollout, kill switches, governance.

## Part XIV · AI at work: software and business (ch113–ch116)
- **ch113 AI across the software lifecycle:** planning, design, coding, review, testing, release, operations; roles; risks; metrics.
- **ch114 Debugging, root-cause analysis and code review:** systematic debugging with Claude Code, logs and traces, git bisect, RCA write-ups, /code-review and ultrareview, reviewing AI-written code.
- **ch115 AI for business:** analysis, spreadsheets, reporting, documents, slides, research, meeting notes, knowledge management, with claude.ai features; data privacy.
- **ch116 Enterprise AI adoption (new):** vendor selection criteria, licensing and contracts, data protection and residency, enterprise architecture (gateways, SSO, logging, model routing, private networking via cloud providers), build vs buy vs partner, governance boards, ROI (link ch125), employee adoption and training, and a vendor-evaluation scorecard.

## Part XVI · Security, privacy and governance (ch129–ch134)
- **ch129 The AI threat landscape:** OWASP Top 10 for LLM applications (verify current version), MITRE ATLAS, threat modelling for AI features, a worked threat model.
- **ch130 Prompt injection and jailbreaks:** direct and indirect injection, jailbreak families, defences in depth, testing with safe exercises (link ch104 MCP security and ch124 evals).
- **ch131 Privacy, data and compliance:** what data goes where, retention and training settings (verify Anthropic's consumer vs commercial terms), PII handling, secrets, DLP, data residency.
- **ch132 AI law and standards (new):** the EU AI Act (risk tiers, obligations, timeline — verify dates), GDPR as applied to AI, India's Digital Personal Data Protection Act 2023 and Rules (verify current status and dates), the NIST AI Risk Management Framework (and Generative AI Profile), ISO/IEC 42001, and practical implications for a QA team. Not legal advice; say so.
- **ch133 Securing agents, tools and plugins:** least privilege, sandboxing, secrets, supply chain (plugins, MCP servers, packages), managed settings, monitoring.
- **ch134 Responsible AI and governance:** principles, fairness and bias testing, transparency, human oversight, accountability, an AI use policy template, review boards.

## Part XVII · Advanced AI engineering (ch135–ch139)
- **ch135 Fine-tuning and custom models (expert, optional):** when (rarely) to fine-tune vs prompt/RAG, LoRA/PEFT concepts, data preparation, evaluation, what cloud providers offer (verify), costs.
- **ch136 Running models on your own computer:** Ollama and llama.cpp (verify commands), open-weight models (Qwen, Mistral, DeepSeek, Gemma), quantisation (plain explanation), hardware needs, a hands-on lab, privacy benefits and limits.
- **ch137 Training at scale (expert, optional):** GPUs/TPUs, memory, parallelism (data/tensor/pipeline), clusters, scaling laws (Kaplan 2020, Chinchilla 2022), energy.
- **ch138 Deploying and optimising models (expert, optional):** serving stacks (vLLM etc., verify), batching, KV cache, quantisation, distillation, speculative decoding, latency/cost trade-offs.
- **ch139 Research frontiers and the future:** agents, reasoning, interpretability, multimodality, robotics, efficiency, safety research, open questions; predictions only in Opinion boxes.

## Part XVIII · Practice and Projects (ch141–ch145)
- **ch140 Examinations:** three exams (beginner, intermediate, advanced), each with 20–30 questions in the .quiz format (one data-ok each), covering the whole book, plus practical exam tasks and marking guides.
- **ch141 Projects and capstones:** a menu of graded projects by level (understand/use/build), each with brief, requirements, deliverables and rubric.
- **ch142 Capstone: build an AI QA assistant end to end (new):** a substantial, completable project that reads requirements (a local story file, or Jira via MCP), retrieves relevant docs (RAG), generates test scenarios with structured output, executes selected checks with Playwright (MCP or scripted tests), analyses failures, produces an evidence report, and requires human approval before consequential actions (filing bugs, posting). Architecture diagram, milestones, complete code skeleton with real runnable parts, setup, expected outputs, evaluation and troubleshooting. Links to ch92–ch94, ch96–ch105, ch108, ch120, ch124.
- **ch143 Interview preparation (optional):** question bank by topic with model answers, STAR-AI method, mock-interview prompt, portfolio advice.
- **ch144 Teaching others:** workshop plans (60 min, half-day, 4-session series), adapting to non-technical audiences, demos, exercises, handling questions, measuring learning, using this book as course material.
