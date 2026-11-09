# AI Industry Fact Sheet

**Verified on 2026-11-09**

How to read this sheet:
- Every fact has a source link. Official company pages and docs come first. Wikipedia and news outlets fill gaps.
- **UNVERIFIED** means the claim comes from one secondary source, sources disagree, or no official page was found. Do not print it in the textbook as settled fact.
- The industry moves fast. Version numbers and "flagship" labels below are a snapshot as of 2026-11-09. Recheck before publishing.
- Many 2026 facts here came after the researcher's training data ended (June 2026). They were taken from live sources, not from memory.

---

## 1. Headline snapshot (as of 2026-11-09)

| Company | Current flagship (per official source) | Open or closed | Source |
|---|---|---|---|
| OpenAI | GPT-6 Astra (released Sep 3, 2026). GPT-6.1 Sol and GPT-6.1 Terra are newer but smaller/cheaper. | Proprietary (plus older open-weight gpt-oss) | [OpenAI models docs](https://developers.openai.com/api/docs/models), [CNBC](https://www.cnbc.com/2026/09/03/open-ai-astra-gpt-6-cyber.html) |
| Google DeepMind | Gemini 4 Argon (announced Sep 30, 2026; GA in API Oct 13, 2026) | Proprietary (Gemma is the open family) | [Google blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/), [Gemini API changelog](https://aistudio.google.com/docs/changelog) |
| Anthropic | Claude Fable 5.1 (most capable GA model); Claude Opus 5.5 is the recommended default | Proprietary | [Claude models overview](https://platform.claude.com/docs/en/about-claude/models/overview) |
| Meta | Muse family (Muse Spark, Apr 8, 2026); successor to Llama | Mostly proprietary; some open-weight Muse models | [Meta newsroom](https://about.fb.com/news/2026/04/introducing-muse-spark-meta-superintelligence-labs/) |
| xAI (now "SpaceX Super Intelligence") | Grok 4.7 (Sep 2026) | Proprietary (Grok-1 and Grok-2.x weights released) | [xAI API release notes](https://docs.x.ai/developers/release-notes) |
| Microsoft AI | MAI-Thinking-1 (Aug 12, 2026, public preview) | Proprietary | [microsoft.ai](https://microsoft.ai/news/introducing-mai-thinking-1/) |
| DeepSeek | DeepSeek-V4-Pro and DeepSeek-V4.1-Flash | Open weights (MIT) | [DeepSeek API news](https://api-docs.deepseek.com/news/news), [Wikipedia](https://en.wikipedia.org/wiki/DeepSeek) |
| Mistral AI | Mistral Large 4 (preview Oct 6, 2026; weights Oct 29, 2026) | Open weights | [TechCrunch](https://techcrunch.com/2026/10/06/mistrals-new-1t-model-aims-to-leapfrog-closed-and-open-rivals/), [Fortune](https://fortune.com/2026/10/29/mistral-releases-new-model-large-4-and-claims-top-open-model-for-agentic-coding-and-cyber-defense/) |
| Alibaba | Qwen3.8 family (Qwen3.8-Max, Aug 2026) | Mixed: Max cloud models proprietary, many open weights | [Wikipedia: Qwen](https://en.wikipedia.org/wiki/Qwen), [SCMP](https://www.scmp.com/tech/article/3362738/alibabas-ai-model-qwen38-max-made-widely-accessible-ahead-open-weights-release) |
| NVIDIA | Nemotron 3 / 3.5 open models; Vera Rubin GPU platform | Open weights | [NVIDIA blog](https://blogs.nvidia.com/blog/nemotron-3-5-super-vl/) |
| Amazon | Nova 2 family (Nova 2 Lite, Nova 2 Sonic, etc.) | Proprietary | [aws.amazon.com/nova](https://aws.amazon.com/nova/) |

### Big 2026 structural changes a reader should know
- **SpaceX acquired xAI** (all-stock, announced Feb 2, 2026). xAI was later renamed SpaceXAI (July 2026), then "SpaceX Super Intelligence" / SpaceXSI (Oct 2026). Sources: [xAI: "xAI joins SpaceX"](https://x.ai/news/xai-joins-spacex), [Wikipedia: xAI](https://en.wikipedia.org/wiki/XAI_(company)). Exact rename dates: **UNVERIFIED** (secondary sources disagree).
- **SpaceX acquired Cursor's maker Anysphere** for $60B (announced June 16, 2026; closed Aug 14, 2026). Sources: [CNBC](https://www.cnbc.com/2026/06/16/spacex-spcx-cursor-acquisition-ipo.html), [Wikipedia: Anysphere](https://en.wikipedia.org/wiki/Anysphere).
- **NVIDIA agreed to buy Hugging Face** for about $12.9B (definitive agreement Sep 2, 2026). Not yet closed; expected to close in the first half of 2027, pending regulators. Sources: [NVIDIA SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000078/nvda-20260902.htm), [TechCrunch](https://techcrunch.com/2026/09/03/nvidia-confirms-it-will-buy-hugging-face-for-12-9-billion/), [Wikipedia: Hugging Face](https://en.wikipedia.org/wiki/Hugging_Face).
- **Microsoft–OpenAI deal rewritten** (Apr 27, 2026). Azure exclusivity and the AGI clause are gone. Source: [CNBC](https://www.cnbc.com/2026/04/27/openai-microsoft-partnership-revenue-cap.html).
- **Meta moved from open Llama to the mostly proprietary Muse family** (Apr 2026). Source: [Meta newsroom](https://about.fb.com/news/2026/04/introducing-muse-spark-meta-superintelligence-labs/), [VentureBeat](https://venturebeat.com/technology/goodbye-llama-meta-launches-new-proprietary-ai-model-muse-spark-first-since).
- **Gemini CLI was retired for free and individual users on June 18, 2026.** Antigravity CLI replaced it. Source: [Google Developers Blog](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/).
- **Windsurf was renamed Devin Desktop** by Cognition (June 2026). Source: [Cognition blog](https://cognition.com/blog/introducing-devin-desktop). Exact date (June 2, 2026): **UNVERIFIED** (secondary sources only).

---

## 2. Company profiles

### 2.1 OpenAI
- **Founded:** December 2015, as a nonprofit. Founders include Sam Altman, Elon Musk, Ilya Sutskever, Greg Brockman, Trevor Blackwell and others. [Wikipedia](https://en.wikipedia.org/wiki/OpenAI)
- **HQ:** San Francisco. **CEO:** Sam Altman. [Wikipedia](https://en.wikipedia.org/wiki/OpenAI)
- **Structure:** On Oct 28, 2025 the for-profit arm became OpenAI Group PBC (a public benefit corporation), controlled by the nonprofit OpenAI Foundation. Microsoft holds about 27%. [Microsoft blog](https://blogs.microsoft.com/blog/2025/10/28/the-next-chapter-of-the-microsoft-openai-partnership/), [CNBC](https://www.cnbc.com/2026/04/27/openai-microsoft-partnership-revenue-cap.html)
- **Strategy:** Build ever more capable general models and sell them through ChatGPT (consumers and businesses) and an API (developers). It is pushing hard into agents: models that use a computer and write code on their own.
- **Major products:** ChatGPT, Codex (coding agent), the API, GPT Image, Deep Research, ChatGPT Atlas (browser). OpenAI said in March 2026 it would discontinue the Sora app and API. [Wikipedia](https://en.wikipedia.org/wiki/OpenAI)
- **Current models (Nov 2026):** [OpenAI models docs](https://developers.openai.com/api/docs/models)
  - **GPT-6 Astra.** "Most capable model." Released Sep 3, 2026. [CNBC](https://www.cnbc.com/2026/09/03/open-ai-astra-gpt-6-cyber.html), [OpenAI](https://openai.com/index/gpt-6-astra/)
  - **GPT-6.1 Sol.** Near-Astra performance at lower cost. Released Sep 29, 2026 at DevDay. [Wikipedia: GPT-6.1](https://en.wikipedia.org/wiki/GPT-6.1), [TechCrunch](https://techcrunch.com/2026/09/29/openai-launches-gpt-6-1-sol-says-it-nearly-matches-gpt-6-astra-and-costs-less/)
  - **GPT-6.1 Terra.** Fast, efficient model. Released Oct 26, 2026. [Wikipedia: GPT-6.1](https://en.wikipedia.org/wiki/GPT-6.1)
  - **GPT-6 Luna.** Most efficient model, for high-volume tasks. [OpenAI models docs](https://developers.openai.com/api/docs/models). Release date (Sep 22, 2026): **UNVERIFIED**.
  - A planned **GPT-6.1 Astra** release was reportedly cancelled over safety regressions. [Gizmodo](https://gizmodo.com/openai-cancels-release-of-gpt-6-1-astra-because-it-regressed-on-safety-2000818566). Treat as reported, not confirmed by OpenAI.
  - Earlier in 2026: GPT-5.5 (Apr 23, 2026). [Wikipedia: GPT-5.5](https://en.wikipedia.org/wiki/GPT-5.5)
  - **UNVERIFIED:** "GPT-6 Cyber" (early Nov 2026) and "GPT Image 2.6" (Nov 4, 2026). These appear only on aggregators.
- **Open vs proprietary:** Frontier models are proprietary. OpenAI released open-weight models gpt-oss-120b and gpt-oss-20b (Apache 2.0) in August 2025. [OpenAI](https://openai.com/index/introducing-gpt-oss/)
- **Research contributions:** The GPT series. GPT-1 (2018) and GPT-2 (2019) popularised large generative pretraining. GPT-3 ([Brown et al., 2020](https://arxiv.org/abs/2005.14165)) showed few-shot learning. Others: ChatGPT and RLHF at scale ([InstructGPT, 2022](https://arxiv.org/abs/2203.02155)), CLIP, DALL-E, and the o1 "reasoning model" line (2024).
- **Infrastructure and partners:** Microsoft Azure stays the primary cloud, but is no longer exclusive. Others: Stargate (with Oracle, SoftBank and MGX, Jan 2025), Oracle ($300B compute deal, Sep 2025), AMD (6 GW of chips, Oct 2025), AWS ($38B, Nov 2025), a custom chip with Broadcom, and NVIDIA. [Wikipedia](https://en.wikipedia.org/wiki/OpenAI), [CNBC](https://www.cnbc.com/2026/04/27/openai-microsoft-partnership-revenue-cap.html)
- **Business model:** ChatGPT subscriptions (Plus, Pro, Business, Enterprise), pay-per-token API, and enterprise deals.

### 2.2 Google DeepMind and Google's Gemini products
- **Founded:** DeepMind was founded in London on Nov 15, 2010 by Demis Hassabis, Shane Legg and Mustafa Suleyman. Google acquired it in January 2014. It merged with Google Brain in April 2023 to form Google DeepMind. [Wikipedia](https://en.wikipedia.org/wiki/Google_DeepMind)
- **HQ:** London. The parent is Google/Alphabet (Mountain View, CA). **Leader:** Demis Hassabis. [Wikipedia](https://en.wikipedia.org/wiki/Google_DeepMind)
- **Strategy:** Build frontier Gemini models and put them inside Google's huge products (Search, Android, Workspace, Cloud). Run them on Google's own TPU chips. Also pursue AI for science.
- **Major products:** Gemini app, Gemini API / Google AI Studio, Vertex AI on Google Cloud, AI Mode in Search, NotebookLM, Veo (video), Imagen and Nano Banana (images), Lyria (music), Google Antigravity (agentic coding), Jules (coding agent). [Gemini API changelog](https://aistudio.google.com/docs/changelog), [Wikipedia: Antigravity](https://en.wikipedia.org/wiki/Google_Antigravity)
- **Current models (Nov 2026):**
  - **Gemini 4 Argon.** Google's frontier model. Announced Sep 30, 2026 with limited access (cyber defenders first). Became GA in the Gemini API on Oct 13, 2026, and in the Gemini app for AI Pro and Ultra subscribers. [Google blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/), [Gemini app post](https://blog.google/innovation-and-ai/products/gemini-app/gemini-4-argon-availability/), [changelog](https://aistudio.google.com/docs/changelog)
  - **Gemini 3.8 Flash.** Fast model, GA in Sep 2026. [changelog](https://aistudio.google.com/docs/changelog)
  - **Gemini Omni 1.2 Flash.** GA Nov 5, 2026. [changelog](https://aistudio.google.com/docs/changelog)
  - Gemini 3 family launched Nov 18, 2025, and Gemini 3.1 Pro Preview followed on Feb 19, 2026. [Wikipedia: Gemini 3](https://en.wikipedia.org/wiki/Gemini_3_(AI)), [changelog](https://aistudio.google.com/docs/changelog)
  - **UNVERIFIED:** Gemini 3.5 Pro. It was announced at I/O 2026, and its release status is unclear.
- **Open vs proprietary:** Gemini is proprietary. **Gemma** is Google's open-weight family; the first version came out Feb 21, 2024. [Wikipedia](https://en.wikipedia.org/wiki/Google_DeepMind)
- **Research contributions:**
  - The **Transformer**: "Attention Is All You Need" (Vaswani et al., Google, 2017). [arXiv 1706.03762](https://arxiv.org/abs/1706.03762)
  - **BERT** (2018). [arXiv 1810.04805](https://arxiv.org/abs/1810.04805)
  - **AlphaGo**, which beat Lee Sedol 4–1 in March 2016. [Wikipedia](https://en.wikipedia.org/wiki/Google_DeepMind)
  - **AlphaFold**: Hassabis and John Jumper shared the 2024 Nobel Prize in Chemistry. [Wikipedia](https://en.wikipedia.org/wiki/Google_DeepMind)
  - Early sparse Mixture-of-Experts work at Google Brain (Shazeer et al., 2017). [arXiv 1701.06538](https://arxiv.org/abs/1701.06538)
  - The Genie world models.
- **Infrastructure:** Google's own TPUs and Google Cloud. Anthropic also signed a deal in Oct 2025 for up to one million TPUs. [Wikipedia: Anthropic](https://en.wikipedia.org/wiki/Anthropic)
- **Business model:** Ads (Search), Google One / AI Pro and AI Ultra subscriptions, Workspace, Google Cloud / Vertex AI, and pay-per-token API. Gemini 4 Argon list price: $2 input / $10 output per million tokens (introductory), then $4 / $20. [Google blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)
- **Apple deal:** Announced Jan 12, 2026. Apple's next-generation Apple Foundation Models will be based on Gemini models and cloud technology. [Google–Apple joint statement](https://blog.google/company-news/inside-google/company-announcements/joint-statement-google-apple/)

### 2.3 Microsoft (Copilot, MAI models, OpenAI partnership)
- **Company:** Founded 1975 by Bill Gates and Paul Allen. HQ: Redmond, Washington. (Widely known; see [Wikipedia: Microsoft](https://en.wikipedia.org/wiki/Microsoft).)
- **Microsoft AI (MAI) division:** Formed March 19, 2024 and led by Mustafa Suleyman. An MAI Superintelligence team was created on Nov 6, 2025. In March 2026 a separate Copilot division was created (led by Jacob Andreou). [Wikipedia: Microsoft AI](https://en.wikipedia.org/wiki/Microsoft_AI)
- **Strategy:** Put AI ("Copilot") across Windows, Microsoft 365, GitHub and Azure, and sell model access through Azure / Microsoft Foundry. It hedges by using OpenAI models, its own MAI models, and third-party models (including Anthropic's Claude in Foundry).
- **Major products:** Microsoft 365 Copilot, Copilot consumer app, GitHub Copilot, Azure AI / Microsoft Foundry. [Claude in Microsoft Foundry](https://platform.claude.com/docs/en/about-claude/models/overview)
- **MAI models:**
  - MAI-Voice-1 and MAI-1-preview (Aug 28, 2025), MAI-Image-1 (Oct 13, 2025). [Wikipedia](https://en.wikipedia.org/wiki/Microsoft_AI)
  - Seven new models around Build (June 2026), including MAI-Code-1-Flash, which is rolling out in GitHub Copilot in VS Code. [microsoft.ai](https://microsoft.ai/news/introducingmai-code-1-flash/)
  - **MAI-Thinking-1**, Microsoft's reasoning model. Published Aug 12, 2026. Sparse MoE, about 35B active / about 1T total parameters. Public preview on Microsoft Foundry. [microsoft.ai](https://microsoft.ai/news/introducing-mai-thinking-1/)
  - **UNVERIFIED:** MAI-Code-1.1-Flash.
- **OpenAI partnership:** Microsoft first invested in 2019, with billions more from 2023.
  - **Oct 28, 2025:** OpenAI was recapitalised and Microsoft received about 27%. [Microsoft blog](https://blogs.microsoft.com/blog/2025/10/28/the-next-chapter-of-the-microsoft-openai-partnership/)
  - **Apr 27, 2026 amendment:** [CNBC](https://www.cnbc.com/2026/04/27/openai-microsoft-partnership-revenue-cap.html)
    - Microsoft's license to OpenAI IP is now non-exclusive, through 2032.
    - OpenAI may serve products on any cloud. Azure stays primary and gets launches first.
    - The AGI clause was removed.
    - OpenAI keeps paying a 20% revenue share, now capped, through 2030.
- **Infrastructure:** Azure datacenters (NVIDIA GPUs) plus Microsoft's in-house Maia accelerator. Maia status in 2026: **UNVERIFIED** (not checked this round).
- **Business model:** Per-seat Copilot subscriptions, Azure consumption, GitHub Copilot subscriptions.

### 2.4 Meta (Llama and successors)
- **Company:** Founded 2004 (as Facebook) by Mark Zuckerberg and others. HQ: Menlo Park, California. ([Wikipedia: Meta Platforms](https://en.wikipedia.org/wiki/Meta_Platforms))
- **AI labs:** FAIR (Facebook AI Research) was founded in 2013, with Yann LeCun a founding director. **Meta Superintelligence Labs (MSL)** was formed in 2025, with Alexandr Wang as Chief AI Officer. [Wikipedia: Meta AI](https://en.wikipedia.org/wiki/Meta_AI)
- **Strategy:** It used to win developers with open Llama weights. Since 2026 it builds frontier "personal superintelligence" models (Muse), mostly kept proprietary, and puts them in WhatsApp, Instagram, Facebook, Messenger, Threads and Ray-Ban Meta glasses.
- **Major products:** Meta AI assistant and app (meta.ai), AI in Meta's social apps, Ray-Ban Meta / Oakley Meta smart glasses, Meta Model API, Muse Code (terminal coding agent, Aug 2026). [Meta newsroom](https://about.fb.com/news/2026/04/introducing-muse-spark-meta-superintelligence-labs/), [Wikipedia: Muse](https://en.wikipedia.org/wiki/Muse_Spark)
- **Models:**
  - **Llama** (open weights, 2023–2025). LLaMA 1 came out February 2023, and Llama 4 on April 5, 2025. [Wikipedia: Llama](https://en.wikipedia.org/wiki/Llama_(language_model)), [Wikipedia: Meta AI](https://en.wikipedia.org/wiki/Meta_AI)
  - **Muse Spark.** Apr 8, 2026. The first MSL model. Not open-weight: offered via the Meta AI apps and a private-preview API. Meta says it "hope[s] to open-source future versions." [Meta newsroom](https://about.fb.com/news/2026/04/introducing-muse-spark-meta-superintelligence-labs/)
  - **Muse Spark 1.1** (Jul 9), **1.2** (Aug 5) and **1.3** (Sep 2, 2026), all proprietary. [Wikipedia: Muse](https://en.wikipedia.org/wiki/Muse_Spark), [Meta research blog](https://research.meta.ai/blog/introducing-muse-spark-1-3)
  - **Muse Glimmer.** 30B open-weight model, Apache 2.0, Aug 10, 2026. [Wikipedia: Muse](https://en.wikipedia.org/wiki/Muse_Spark), [Hugging Face](https://huggingface.co/meta-models/Muse-Glimmer-30B)
  - **UNVERIFIED:** Muse Wonder (Oct 12, 2026), and Muse Spark Open (Oct 15, 2026; reported as an 816B MoE open-weight model). The license detail carries a citation-needed tag.
  - **UNVERIFIED:** Whether a future Llama will ship. Meta has announced no next-generation Llama.
- **Research contributions:**
  - Llama made strong open weights mainstream. [LLaMA paper, arXiv 2302.13971](https://arxiv.org/abs/2302.13971)
  - PyTorch, the deep-learning framework that started at Meta.
  - Segment Anything (SAM).
- **Infrastructure:** Very large NVIDIA GPU clusters plus in-house MTIA accelerators. [Wikipedia: Meta AI](https://en.wikipedia.org/wiki/Meta_AI)
- **Business model:** Advertising across its apps. AI raises engagement and ad performance. Meta AI also has optional paid tiers. [Wikipedia: Meta AI](https://en.wikipedia.org/wiki/Meta_AI)

### 2.5 NVIDIA
- **Founded:** Apr 5, 1993 by Jensen Huang, Chris Malachowsky and Curtis Priem. **HQ:** Santa Clara, California. **CEO:** Jensen Huang. [Wikipedia](https://en.wikipedia.org/wiki/Nvidia)
- **Strategy:** Sell the "picks and shovels" of AI: GPUs, networking, full rack-scale systems and the CUDA software platform. It increasingly also releases open models (Nemotron) and moves up the stack (Hugging Face deal).
- **Major products:** Data-center GPUs and generations:
  - Ampere (A100, 2020)
  - Hopper (H100)
  - Blackwell (announced Mar 18, 2024)
  - Vera Rubin (successor to Blackwell, detailed at GTC Mar 2026)

  Software and platforms: CUDA, NIM microservices, DGX systems. [Wikipedia](https://en.wikipedia.org/wiki/Nvidia)
- **Models:** The **Nemotron** open-weight family.
  - Nemotron 3 (announced Dec 15, 2025; Nano / Super / Ultra hybrid MoE). [Wikipedia](https://en.wikipedia.org/wiki/Nvidia)
  - Nemotron 3 Ultra (about 550B total parameters). [NVIDIA research](https://research.nvidia.com/labs/nemotron/Nemotron-3-Ultra/)
  - Nemotron 3.5 Super VL (120B total / 12B active, open). [NVIDIA blog](https://blogs.nvidia.com/blog/nemotron-3-5-super-vl/)
  - Exact Nemotron 3.5 release dates: **UNVERIFIED**.
- **Open vs proprietary:** Nemotron models are open weights. Hardware and CUDA are proprietary.
- **Research contributions:** CUDA (2006–07) made GPUs usable for general computing, and so for deep learning. AlexNet (2012) was trained on NVIDIA GPUs.
- **Key deals:**
  - Groq: inference technology licence plus key staff, about $20B, Dec 2025. [Wikipedia](https://en.wikipedia.org/wiki/Nvidia)
  - Hugging Face: about $12.9B acquisition, pending. [NVIDIA 8-K](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000078/nvda-20260902.htm)
  - OpenAI: 10 GW letter of intent, Sep 2025, later restructured. [Wikipedia](https://en.wikipedia.org/wiki/Nvidia)
- **Market value:** First company to reach $5 trillion (Oct 29, 2025). [Wikipedia](https://en.wikipedia.org/wiki/Nvidia)
- **Rubin shipping status:** Sources say H2 2026 deployment. Exact shipment dates are **UNVERIFIED**. [Wikipedia: Rubin](https://en.wikipedia.org/wiki/Rubin_(microarchitecture))
- **Business model:** Hardware and systems sales, mostly to hyperscalers and AI labs, plus software and enterprise licences.

### 2.6 Amazon / AWS (Bedrock, Nova, Trainium)
- **Company:** Amazon was founded in 1994 by Jeff Bezos. HQ: Seattle. AWS launched in 2006. ([Wikipedia: Amazon](https://en.wikipedia.org/wiki/Amazon_(company)))
- **Strategy:** Be the neutral "model marketplace" cloud. Bedrock offers many vendors' models, including Anthropic's Claude. Amazon also builds its own Nova models and Trainium chips to cut cost.
- **Major products:**
  - **Amazon Bedrock**: announced Apr 13, 2023; GA Sep 28, 2023. [Wikipedia: Bedrock](https://en.wikipedia.org/wiki/Amazon_Bedrock)
  - SageMaker.
  - Nova Act: a browser-automation agent service. [aws.amazon.com/nova](https://aws.amazon.com/nova/)
  - Nova Forge: build custom models on top of Nova. [aws.amazon.com/nova](https://aws.amazon.com/nova/)
  - Alexa+.
  - Kiro: an agentic IDE. It was not checked this round, so treat it as **UNVERIFIED**.
- **Models:**
  - Original Nova (Micro / Lite / Pro), Dec 2024.
  - **Nova 2** (re:Invent, Dec 2025): Nova 2 Lite, Nova 2 Pro (preview), Nova 2 Omni and Nova 2 Sonic. [TechRepublic](https://www.techrepublic.com/article/news-aws-reinvent-day-2-2025/), [aws.amazon.com/nova](https://aws.amazon.com/nova/)
  - **UNVERIFIED:** Nova 2.5 Sonic (GA Oct 5, 2026), and the retirement of Nova Premier, Canvas and Reel (Sep 2026). These come from secondary sources only.
- **Open vs proprietary:** Nova is proprietary.
- **Chips:**
  - **Trainium3**: Amazon's first 3nm AI chip, in Trn3 UltraServers of 144 chips. GA at re:Invent 2025. [TechRepublic](https://www.techrepublic.com/article/news-aws-reinvent-day-2-2025/)
  - **Project Rainier**: a giant Trainium2 cluster built for Anthropic. [DeepLearning.AI](https://www.deeplearning.ai/the-batch/amazon-plans-to-spend-tens-of-billions-on-ai-infrastructure-with-project-rainier)
- **Anthropic partnership:** Amazon is Anthropic's primary cloud and a major investor. An April 2026 expansion was reported: $5B now plus up to $20B tied to milestones, and about 5 GW of Trainium compute. [Amazon](https://www.aboutamazon.com/news/company-news/amazon-invests-additional-5-billion-anthropic-ai). Exact totals: **UNVERIFIED** (reports differ).
- **Business model:** Cloud consumption (Bedrock tokens, compute), plus AI in retail and Alexa.

### 2.7 xAI (Grok), now "SpaceX Super Intelligence"
- **Founded:** Incorporated Mar 9, 2023 by Elon Musk, and publicly announced Jul 12, 2023. **HQ:** Palo Alto, California. [Wikipedia](https://en.wikipedia.org/wiki/XAI_(company))
- **Corporate history:** [Wikipedia](https://en.wikipedia.org/wiki/XAI_(company)), [x.ai](https://x.ai/news/xai-joins-spacex)
  - Merged with X Corp. (March 2025).
  - Acquired by SpaceX in an all-stock deal (Feb 2, 2026).
  - Rebranded SpaceXAI (July 2026), then SpaceX Super Intelligence / SpaceXSI (Oct 2026). The API docs now use "SpaceXSI".
- **Strategy:** Train frontier models on very large self-built compute (the Colossus cluster in Memphis), then distribute them through X, Grok apps, Tesla and SpaceX products.
- **Major products:** Grok chatbot (in X and standalone apps), Grok API, Grok Imagine (image and video), Grok Voice, Grok Build (coding CLI, Apache-licensed, Jul 16, 2026). [docs.x.ai](https://docs.x.ai/developers/release-notes), [Wikipedia: Grok Build](https://en.wikipedia.org/wiki/Grok_Build)
- **Models:**
  - **Grok 4.7** is the current frontier model on the API (`grok-4.7`, September 2026). [docs.x.ai release notes](https://docs.x.ai/developers/release-notes). Day of release (Sep 21, 2026) per [Wikipedia](https://en.wikipedia.org/wiki/Grok_(chatbot)).
  - Earlier: Grok-1 (Nov 2023), Grok 3 (Feb 2025), Grok 4 (Jul 2025), Grok 4.1 (Nov 2025), and 4.20, 4.3, 4.5 and 4.6 in 2026. [Wikipedia](https://en.wikipedia.org/wiki/Grok_(chatbot))
  - **Grok 5 has NOT been released** as of Nov 2026. [geotoolbox (secondary)](https://geotoolbox.ai/blog/grok-5)
- **Open vs proprietary:** Current models are proprietary. Grok-1 weights were released under Apache 2.0 (Mar 17, 2024), and Grok 2.5 weights later under a community licence. [Wikipedia](https://en.wikipedia.org/wiki/Grok_(chatbot))
- **Infrastructure:** The Colossus supercomputer in Memphis, built on NVIDIA GPUs. [Wikipedia](https://en.wikipedia.org/wiki/XAI_(company))
- **Business model:** X Premium and SuperGrok subscriptions, and the API.

### 2.8 DeepSeek
- **Founded:** Jul 17, 2023 by Liang Wenfeng. Owned and funded by the hedge fund High-Flyer. **HQ:** Hangzhou, China. [Wikipedia](https://en.wikipedia.org/wiki/DeepSeek)
- **Strategy:** Research-first lab. Releases very efficient open-weight models at low prices, showing that frontier-class results do not need the largest budgets.
- **Products:** DeepSeek chat app, DeepSeek API, open weights on Hugging Face / GitHub.
- **Models:** [Wikipedia](https://en.wikipedia.org/wiki/DeepSeek)
  - V2: May 2024
  - V3: Dec 2024
  - **R1: Jan 20, 2025.** An open reasoning model that shook markets.
  - V3.1: Aug 2025
  - V3.2: Dec 2025
  - **V4 (preview): Apr 24, 2026.** V4-Pro has 1.6T total parameters; V4-Flash has 284B.
  - **V4.1-Flash: Sep 10, 2026.**
  - The API now serves `deepseek-flash` as DeepSeek-V4.1-Flash-1017, and `deepseek-v4-pro`. [DeepSeek API news](https://api-docs.deepseek.com/news/news). The exact date of the "1017" update (Oct 17, 2026) is inferred from the build name, so **UNVERIFIED**.
  - **UNVERIFIED:** V4.1-Pro is mentioned but had not launched.
- **Open vs proprietary:** Open weights, MIT licence for R1, V3.1, V3.2 and V4. [Wikipedia](https://en.wikipedia.org/wiki/DeepSeek)
- **Research contributions:**
  - **DeepSeek-R1** showed that pure reinforcement learning can teach reasoning (R1-Zero). [arXiv 2501.12948](https://arxiv.org/abs/2501.12948)
  - **GRPO**, an RL algorithm from DeepSeekMath. [arXiv 2402.03300](https://arxiv.org/abs/2402.03300)
  - **Multi-head Latent Attention** and fine-grained **Mixture-of-Experts** (DeepSeek-V2/V3). [arXiv 2405.04434](https://arxiv.org/abs/2405.04434)
  - DeepSeek Sparse Attention (V3.2).
- **Infrastructure:** Historically NVIDIA GPUs (A100, H800). Increasingly Chinese chips: V4 runs on Huawei Ascend and Cambricon. [Wikipedia](https://en.wikipedia.org/wiki/DeepSeek)
- **Business model:** A low-price API and a free chat app, funded by High-Flyer.

### 2.9 Mistral AI
- **Founded:** April 2023 by Arthur Mensch (CEO), Guillaume Lample and Timothée Lacroix. **HQ:** Paris, France. [Wikipedia](https://en.wikipedia.org/wiki/Mistral_AI)
- **Strategy:** Europe's leading independent lab. It offers open-weight plus enterprise and sovereign deployments that customers can run on their own infrastructure.
- **Products:** Le Chat assistant (renamed **Mistral Vibe** in May 2026, per Wikipedia), La Plateforme API, Devstral / coding tools. [Wikipedia](https://en.wikipedia.org/wiki/Mistral_AI)
- **Models:** [Wikipedia](https://en.wikipedia.org/wiki/Mistral_AI)
  - Mistral 7B (Sep 2023)
  - **Mixtral 8x7B (Dec 2023)**, an early widely used open sparse-MoE model
  - Mistral Large 3 (Dec 2025, Apache 2.0)
  - Mistral Medium 3.5 (Apr 2026)
  - **Mistral Large 4**: preview Oct 6, 2026; downloadable weights Oct 29, 2026; about 1T-parameter MoE (52B active). [TechCrunch](https://techcrunch.com/2026/10/06/mistrals-new-1t-model-aims-to-leapfrog-closed-and-open-rivals/), [Euronews](https://www.euronews.com/2026/10/29/mistral-releases-latest-ai-model-for-download-giving-companies-more-control-over-their-cyb)
- **Open vs proprietary:** Mixed, but strongly open-weight leaning. Licences range from Apache 2.0 to custom terms. Large 4 uses the "Mistral Ecosystem Open-Weight License" (per Wikipedia).
- **Research contributions:** Mixtral popularised open Mixture-of-Experts. [arXiv 2401.04088](https://arxiv.org/abs/2401.04088)
- **Partnerships:** Microsoft (investment in 2024, infrastructure deal in July 2026), ASML (major investor, Sep 2025), NVIDIA (Mar 2026), Samsung (stake, Sep 2026). [Wikipedia](https://en.wikipedia.org/wiki/Mistral_AI)
- **Business model:** API, enterprise licences, on-premise deployments, Le Chat / Vibe subscriptions.

### 2.10 Alibaba (Qwen)
- **Company:** Alibaba Group was founded in 1999 by Jack Ma and others. HQ: Hangzhou. Qwen is built by Alibaba Cloud. [Wikipedia: Qwen](https://en.wikipedia.org/wiki/Qwen)
- **Strategy:** Release a broad family of open-weight models to build a developer ecosystem. Keep the top "Max" models proprietary on Alibaba Cloud, and plug Qwen into Alibaba's consumer apps.
- **Products:** Qwen app (234M users by May 2026), Alibaba Cloud Model Studio, open weights on Hugging Face / ModelScope. [Wikipedia](https://en.wikipedia.org/wiki/Qwen)
- **Models:** [Wikipedia](https://en.wikipedia.org/wiki/Qwen), [SCMP](https://www.scmp.com/tech/article/3362738/alibabas-ai-model-qwen38-max-made-widely-accessible-ahead-open-weights-release)
  - Qwen first launched as Tongyi Qianwen in April 2023.
  - Qwen3.5 (Feb 2026)
  - Qwen3.6 (Apr 2026)
  - Qwen3.7 (May–Jun 2026)
  - **Qwen3.8** (Aug 2026 onward):
    - Qwen3.8-Max (cloud, Aug 3)
    - Qwen3.8-2.4T-A95B open weights (Aug 12)
    - Qwen3.8-27B (Apache 2.0, Aug 14)
    - Qwen3.8-Flash (Aug 26)
  - **No "Qwen 4" flagship is confirmed.** One site claims a "Qwen 4 Coder": **UNVERIFIED**.
- **Open vs proprietary:** Mostly open weights (many Apache 2.0). Max-tier cloud models are proprietary.
- **Research contributions:** Among the most downloaded open model families. Many community fine-tunes are built on Qwen.
- **Infrastructure:** Alibaba Cloud.
- **Business model:** Cloud consumption, plus driving traffic to Alibaba commerce apps.

### 2.11 Anthropic (included because Claude Code is covered below)
- **Founded:** January 2021 by former OpenAI staff, including Dario Amodei (CEO) and Daniela Amodei (President). A public benefit corporation. **HQ:** San Francisco. [Wikipedia](https://en.wikipedia.org/wiki/Anthropic)
- **Strategy:** Safety-focused frontier lab that sells mainly to businesses and developers. Strong focus on coding and agents.
- **Products:** Claude apps, Claude API (Claude Platform), Claude Code, the Model Context Protocol (MCP). [Wikipedia](https://en.wikipedia.org/wiki/Anthropic)
- **Current models:** [Claude models overview](https://platform.claude.com/docs/en/about-claude/models/overview), [Wikipedia](https://en.wikipedia.org/wiki/Anthropic)
  - Claude Fable 5.1 (Sep 1, 2026)
  - Claude Opus 5.5 (Sep 22, 2026); Anthropic's docs say "start with" it for most workloads
  - Claude Sonnet 5.5 (Sep 28, 2026)
  - Claude Haiku 5.5 (Oct 7, 2026)
  - All have 1M-token context.
  - Claude Mythos 5.1 is restricted to approved users.
- **Research contributions:** Constitutional AI, interpretability ("features" research), MCP (open protocol, Nov 2024). [Wikipedia](https://en.wikipedia.org/wiki/Anthropic)
- **Infrastructure:**
  - AWS is the primary cloud (Trainium and Project Rainier).
  - Google TPUs (up to 1M, Oct 2025).
  - Microsoft Azure / NVIDIA ($30B compute commitment).
  - [Wikipedia](https://en.wikipedia.org/wiki/Anthropic)
- **Business model:** API usage, Claude subscriptions (Pro, Max, Team, Enterprise), and availability through cloud partners (Bedrock, Google Cloud, Microsoft Foundry).

---

## 3. Other notable players (short entries)

| Player | Founded / founders / HQ | What they do (Nov 2026) | Open? | Sources |
|---|---|---|---|---|
| **Cohere** | 2019; Aidan Gomez (a co-author of the Transformer paper), Ivan Zhang, Nick Frosst; Toronto | Enterprise AI for regulated industries. Latest: **Command A+** (May 20, 2026; 218B MoE, 25B active). Products: North (workspace), Embed and Rerank. Signed a merger agreement with Aleph Alpha in Sep 2026 (pending). | Command A+ weights under Apache 2.0 | [Cohere blog](https://cohere.com/blog/command-a-plus), [Wikipedia](https://en.wikipedia.org/wiki/Cohere), [MarkTechPost](https://www.marktechpost.com/2026/05/21/cohere-releases-command-a-a-218b-sparse-moe-model-for-agentic-workflows-that-runs-on-as-few-as-two-h100-gpus/) |
| **Perplexity** | Aug 2022; Aravind Srinivas (CEO), Denis Yarats, Johnny Ho, Andy Konwinski; San Francisco | AI "answer engine" with citations. Comet AI browser (Jul 2025, free from Oct 2025). Perplexity Computer agent (Feb 2026). In-house Sonar models. Subscription-first since Feb 2026. Ongoing Amazon lawsuit over Comet shopping. | Mostly proprietary | [Wikipedia](https://en.wikipedia.org/wiki/Perplexity_AI) |
| **Hugging Face** | 2016; Clément Delangue, Julien Chaumond, Thomas Wolf; New York (Brooklyn) | The "GitHub of AI": Hub for models and datasets, the `transformers` library. **NVIDIA agreed to acquire it** (Sep 2, 2026, about $12.9B; pending, expected H1 2027). | Open-source platform | [Wikipedia](https://en.wikipedia.org/wiki/Hugging_Face), [TechCrunch](https://techcrunch.com/2026/09/03/nvidia-confirms-it-will-buy-hugging-face-for-12-9-billion/) |
| **Moonshot AI (Kimi)** | Mar 2023; Yang Zhilin, Zhou Xinyu, Wu Yuxin; Beijing. Alibaba is a major investor. | Kimi assistant and models. K2 (Jul 2025, 1T open), K2 Thinking (Nov 2025), K2.5 (Jan 2026), **K3** (Jul 16, 2026, about 2.8T params, open weights with a revenue-share licence), **K3.1 Pro** (Oct 2026). Cursor's Composer 2 / 2.5 models were reportedly built on Kimi K2.5. | Open weights (custom licences) | [Wikipedia](https://en.wikipedia.org/wiki/Moonshot_AI), [Fortune](https://fortune.com/2026/07/16/moonshots-kimi-k3-pushes-chinese-ai-into-fable-level-territory/). **UNVERIFIED:** K3.1 Pro exact date (Oct 4 vs Oct 24) and whether its weights are open. |
| **Zhipu AI / Z.ai (GLM)** | 2019; Tsinghua University spin-out (Jie Tang, Li Juanzi); Beijing. Listed in Hong Kong Jan 8, 2026. On the US Entity List since Jan 2025. | GLM models: GLM-4.5 (Jul 2025), GLM-5 (Feb 12, 2026), GLM-5.2 (Jun 16, 2026), **GLM-5.3** (Aug 14, 2026). GLM Coding Plan. | Open weights (MIT since Jul 2025) | [Wikipedia](https://en.wikipedia.org/wiki/Z.ai). **UNVERIFIED:** GLM-5.3 weights release date. |
| **Cursor / Anysphere** | 2022; Michael Truell, Sualeh Asif, Aman Sanger, Arvid Lunnemark (MIT students); San Francisco. **Owned by SpaceX since Aug 14, 2026.** | Cursor, an AI-first code editor (VS Code fork) with agents. Bugbot code review. In-house **Composer** coding models (Composer 2, Mar 2026; Composer 2.5, May 2026). | Proprietary | [Wikipedia: Anysphere](https://en.wikipedia.org/wiki/Anysphere), [CNBC](https://www.cnbc.com/2026/06/16/spacex-spcx-cursor-acquisition-ipo.html), [SiliconANGLE](https://siliconangle.com/2026/03/19/vibe-coding-startup-cursor-launches-programming-optimized-composer-2-model/) |
| **Apple** | 1976; Steve Jobs, Steve Wozniak, Ronald Wayne; Cupertino | Apple Intelligence: on-device plus Private Cloud Compute. Jan 12, 2026: next-gen Apple Foundation Models will be based on Google Gemini and power a more personal Siri. Also integrates ChatGPT. | Proprietary | [Google–Apple joint statement](https://blog.google/company-news/inside-google/company-announcements/joint-statement-google-apple/), [CNBC](https://www.cnbc.com/2026/01/12/apple-google-ai-siri-gemini.html). **UNVERIFIED:** whether the Gemini-based Siri has fully shipped, and the reported ~$1B/yr payment. |
| **Cognition** | 2023; San Francisco | Devin (autonomous software engineer). Acquired Windsurf (Jul 2025) and renamed it **Devin Desktop** (2026). SWE-series in-house models. | Proprietary | [Cognition blog](https://cognition.com/blog/introducing-devin-desktop), [Wikipedia](https://en.wikipedia.org/wiki/Cognition_AI) |

---

## 4. AI coding-agent landscape (Nov 2026)

| Tool | Maker | What it is | Instruction file it reads | Official link |
|---|---|---|---|---|
| **Claude Code** | Anthropic | Agentic coding tool in the terminal, IDEs, desktop and web. GA since May 2025. | `CLAUDE.md` (also `CLAUDE.local.md`, `.claude/rules/`). It reads `AGENTS.md` when no CLAUDE.md exists, or via import. | [code.claude.com/docs](https://code.claude.com/docs/en/memory) |
| **OpenAI Codex** | OpenAI | Coding agent across Codex CLI (open source), IDE extension, Codex Cloud, and the ChatGPT web, desktop and mobile apps. | `AGENTS.md` | [learn.chatgpt.com/docs](https://learn.chatgpt.com/docs), [agents.md](https://agents.md/), [github.com/openai/codex](https://github.com/openai/codex) |
| **Gemini CLI → Antigravity CLI** | Google | Gemini CLI was an open-source terminal agent (Jun 2025). It was retired for free and individual users on **Jun 18, 2026** and replaced by the closed-source **Antigravity CLI** (`agy`). Still works with paid API keys. | `GEMINI.md` (filename configurable, e.g. to `AGENTS.md`) | [Google Developers Blog](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/), [geminicli.com docs](https://geminicli.com/docs/cli/gemini-md/) |
| **Google Antigravity** | Google | Agent-first development platform. IDE launched Nov 18, 2025. Antigravity 2.0 desktop app, CLI and SDK followed May 19, 2026. | Not verified this round (**UNVERIFIED**) | [Wikipedia](https://en.wikipedia.org/wiki/Google_Antigravity) |
| **Jules** | Google | Asynchronous cloud coding agent. It clones a GitHub repo into a VM, plans, and opens a PR. | `AGENTS.md` | [jules.google](https://jules.google/), [agents.md](https://agents.md/) |
| **GitHub Copilot** | GitHub (Microsoft) | Code completion and chat; agent mode in IDEs; **Copilot cloud agent** (formerly "coding agent": works in the background and opens PRs; GitHub now also calls the newer experience "Copilot in the cloud"); **Copilot CLI** (terminal); Copilot code review. | `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md`, plus agent files `AGENTS.md`, `CLAUDE.md` or `GEMINI.md` | [GitHub Docs: custom instructions](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions), [cloud agent](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent), [Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli) |
| **Cursor** | Anysphere (SpaceX) | AI code editor with agents and its own Composer models. | `.cursor/rules` (not verified this round) and `AGENTS.md` | [cursor.com](https://cursor.com), [agents.md](https://agents.md/) |
| **Windsurf → Devin Desktop** | Cognition | Windsurf editor, renamed Devin Desktop in 2026. Its Cascade agent is being replaced by "Devin Local". | `AGENTS.md` (listed as "Windsurf from Cognition") | [Cognition blog](https://cognition.com/blog/introducing-devin-desktop), [agents.md](https://agents.md/) |
| **Devin** | Cognition | Autonomous cloud "AI software engineer". | `AGENTS.md` | [agents.md](https://agents.md/) |
| **Others** | various | Grok Build (SpaceXSI, Apache-licensed CLI, Jul 2026), Muse Code (Meta, Aug 2026), Aider, goose, opencode, Zed, Warp, Junie (JetBrains), Amp, Factory, Kilo Code, RooCode, Augment Code | mostly `AGENTS.md` | [agents.md](https://agents.md/), [Wikipedia: Grok Build](https://en.wikipedia.org/wiki/Grok_Build), [Wikipedia: Muse](https://en.wikipedia.org/wiki/Muse_Spark) |

## 5. Instruction-file conventions

| File | Primary tool | Notes | Source |
|---|---|---|---|
| `CLAUDE.md` | Claude Code | Project (`./CLAUDE.md` or `./.claude/CLAUDE.md`), user and org levels. `CLAUDE.local.md` holds personal settings. If a repo has only `AGENTS.md`, Claude Code reads that instead. If both exist, it reads CLAUDE.md only, unless CLAUDE.md imports AGENTS.md or settings change this. GitHub Copilot's agents also accept a root `CLAUDE.md`. | [Claude Code memory docs](https://code.claude.com/docs/en/memory), [GitHub Docs](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions) |
| `AGENTS.md` | Cross-tool open standard (OpenAI Codex, Jules, Gemini CLI, GitHub Copilot cloud agent, Cursor, Devin / Windsurf, Zed, Warp, VS Code and many more) | "A README for agents." Now stewarded by the **Agentic AI Foundation under the Linux Foundation**. Nested files are allowed; the nearest one wins. | [agents.md](https://agents.md/) |
| `GEMINI.md` | Gemini CLI (and successor tooling) | Loaded from global (`~/.gemini/GEMINI.md`), workspace and just-in-time locations. The filename is configurable via `context.fileName`. Also accepted by GitHub Copilot agents. | [geminicli.com](https://geminicli.com/docs/cli/gemini-md/) |
| `.github/copilot-instructions.md` | GitHub Copilot | Repository-wide instructions for Copilot Chat, code review and the cloud agent. Path-specific `.github/instructions/NAME.instructions.md` files use `applyTo` globs. | [GitHub Docs](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions) |

---

## 6. Widely cited benchmarks

| Benchmark | What it measures | Status note (2026) | Source |
|---|---|---|---|
| **MMLU** | Multiple-choice knowledge across 57 subjects (law, medicine, math and more). | Largely saturated by frontier models. Harder variants (e.g. MMLU-Pro) are used instead. | [Hendrycks et al. 2020, arXiv 2009.03300](https://arxiv.org/abs/2009.03300) |
| **GPQA (Diamond)** | Graduate-level, "Google-proof" science questions written by PhD experts. | Diamond is the hardest subset and widely quoted. | [Rein et al. 2023, arXiv 2311.12022](https://arxiv.org/abs/2311.12022) |
| **SWE-bench / SWE-bench Verified** | Can a model fix real GitHub issues in Python repos so the tests pass? Verified is a human-checked 500-task subset (OpenAI, Aug 2024). | **OpenAI stopped reporting Verified on Feb 23, 2026**, citing contamination and flawed tasks. It recommends **SWE-bench Pro** instead. | [Jimenez et al., arXiv 2310.06770](https://arxiv.org/abs/2310.06770), [OpenAI: SWE-bench Verified](https://openai.com/index/introducing-swe-bench-verified/), [OpenAI: why we no longer evaluate it](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/) |
| **ARC-AGI (1/2/3)** | Fluid intelligence: solve novel puzzles from a few examples. **ARC-AGI-3** (launched Mar 2026) uses interactive game-like environments. At launch humans solved 100% and the best AI about 0.37%. | ARC Prize 2026 ($2M pool). Submissions were due Nov 2, 2026; results due Dec 4, 2026. | [arcprize.org](https://arcprize.org/competitions/2026/arc-agi-3), [ARC-AGI-3 paper arXiv 2603.24621](https://arxiv.org/abs/2603.24621), [Chollet 2019, arXiv 1911.01547](https://arxiv.org/abs/1911.01547) |
| **Humanity's Last Exam (HLE)** | About 2,500 expert-written, very hard questions across many fields, built to sit at the frontier of human knowledge. | | [Phan et al. 2025, arXiv 2501.14249](https://arxiv.org/abs/2501.14249), [lastexam.ai](https://lastexam.ai) |
| **LMArena / Chatbot Arena (now "Arena")** | Crowdsourced blind head-to-head votes between chatbots, turned into Elo-style rankings. | Rebranded from LMArena to **Arena** (Jan 2026, per secondary sources: **UNVERIFIED**). | [Chiang et al. 2024, arXiv 2403.04132](https://arxiv.org/abs/2403.04132) |
| **Terminal-Bench** | Agents completing real tasks in a command-line terminal. | Newer versions (3.0 / 4.0) are cited in 2026 launches. | Cited in [OpenAI GPT-6 Astra coverage](https://www.cnbc.com/2026/09/03/open-ai-astra-gpt-6-cyber.html) and [Mistral Large 4 coverage](https://fortune.com/2026/10/29/mistral-releases-new-model-large-4-and-claims-top-open-model-for-agentic-coding-and-cyber-defense/) |

Teaching note: vendors' benchmark claims in launch posts are self-reported. Independent leaderboards and replication often differ.

---

## 7. Consolidated UNVERIFIED list
1. OpenAI: "GPT-6 Cyber" and "GPT Image 2.6" (aggregators only). The GPT-6 Luna release date. The cancelled GPT-6.1 Astra (press report, not an OpenAI statement).
2. Google: Gemini 3.5 Pro release status. Which instruction file Antigravity reads.
3. Meta: Muse Wonder, Muse Spark Open (size and licence). Whether a future Llama will ship.
4. xAI / SpaceXSI: exact rename dates. Grok 5 has no release date.
5. Microsoft: MAI-Code-1.1-Flash. Status of the Maia chip in 2026.
6. DeepSeek: exact date of V4.1-Flash-1017. V4.1-Pro timing.
7. Amazon: Nova 2.5 Sonic. 2026 Nova retirements. Exact size of the April 2026 Anthropic investment. Kiro details.
8. NVIDIA: Rubin shipment dates. Nemotron 3.5 release dates.
9. Moonshot K3.1 Pro date and weights. GLM-5.3 weights date.
10. Apple: whether the Gemini-based Siri has fully shipped. The ~$1B/yr payment figure.
11. Arena rebrand date (Jan 28, 2026). Exact Windsurf → Devin Desktop date (Jun 2, 2026).
12. Cursor's own instruction format (`.cursor/rules`) was not re-checked this round.
