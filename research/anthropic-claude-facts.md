# Anthropic and Claude: verified fact sheet

**Verified on 2026-11-09**

How to read this sheet:
- Every fact has a source URL.
- **UNVERIFIED** means no official page confirmed the fact. Either the information came only from a search snippet, or official sources contradict each other.
- Prices are in USD. "MTok" means one million tokens.
- docs.claude.com now redirects to platform.claude.com/docs. Docs URLs below use the platform.claude.com form.

---

## 1. Anthropic (the company)

| Fact | Detail | Source |
|---|---|---|
| Founded | "At the beginning of 2021." **UNVERIFIED (partial):** this wording comes from a search snippet of the Series B post. The page was not opened. No other official page states the founding year. | https://www.anthropic.com/news/anthropic-raises-series-b-to-build-safe-reliable-ai |
| Co-founders (as listed officially) | Dario Amodei (CEO), Daniela Amodei (President), Tom Brown, Jack Clark, Jared Kaplan, Sam McCandlish, Chris Olah | https://www.anthropic.com/company/leadership |
| Legal structure | A Public Benefit Corporation "whose purpose is the responsible development and maintenance of advanced AI for the long-term benefit of humanity". The LTBT post calls it a "Delaware Public Benefit Corporation". | https://www.anthropic.com/company ; https://www.anthropic.com/news/the-long-term-benefit-trust |
| Long-Term Benefit Trust (LTBT) | Announced Sept 19, 2023. It is an independent body that can elect a growing share of the Board, and was expected to elect a majority within 4 years. It does not take part in day-to-day decisions. | https://www.anthropic.com/news/the-long-term-benefit-trust |
| Current LTBT trustees (on /company) | Ben Bernanke, Richard Fontaine, Neil Buddy Shah, Christopher Stubbs | https://www.anthropic.com/company |
| Board (on /company) | Dario Amodei, Daniela Amodei, Yasmin Razavi, Reed Hastings, Chris Liddell, Vas Narasimhan | https://www.anthropic.com/company |
| Headquarters | San Francisco, California | https://www.anthropic.com/transparency/voluntary-commitments |
| Amazon | Sept 25, 2023: Amazon invests "up to $4 billion" for a minority stake. AWS becomes the primary cloud provider, with Trainium and Inferentia chips. | https://www.anthropic.com/news/anthropic-amazon |
| Google Cloud | Oct 23, 2025: "up to one million TPUs" and "well over a gigawatt" of capacity in 2026, "worth tens of billions of dollars" | https://www.anthropic.com/news/expanding-our-use-of-google-cloud-tpus-and-services |
| Microsoft and NVIDIA | Nov 18, 2025: Anthropic commits $30B to Azure compute (up to 1 GW). NVIDIA will invest up to $10B and Microsoft up to $5B. | https://www.anthropic.com/news/microsoft-nvidia-anthropic-announce-strategic-partnerships |
| Latest funding round | Series H, May 28, 2026: $65B raised at a $965B post-money valuation. Led by Altimeter, Dragoneer, Greenoaks and Sequoia. | https://www.anthropic.com/news/series-h |
| Earlier rounds | Series G: $30B at a $380B valuation. Series F: $13B at a $183B valuation. **Dates UNVERIFIED** (the pages were not opened). | https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation ; https://www.anthropic.com/news/anthropic-raises-series-f-at-usd183b-post-money-valuation |
| Recent trustee appointments | Bernanke joined Jul 9, 2026 and Stubbs Oct 21, 2026. **UNVERIFIED (partial):** dates come from search summaries. | https://www.anthropic.com/news/ben-bernanke ; https://www.anthropic.com/news/christopher-stubbs-joins-long-term-benefit-trust |

---

## 2. Safety and research

### Constitutional AI and Claude's constitution

- **Paper:** "Constitutional AI: Harmlessness from AI Feedback". arXiv v1 is dated **Dec 15, 2022**. https://arxiv.org/abs/2212.08073
- **"Claude's constitution" (first published version):** May 9, 2023. The page now has an update note pointing to the new version. https://www.anthropic.com/news/claudes-constitution
- **"Claude's new constitution":**
  - The announcement was published Jan 22, 2026. https://www.anthropic.com/news/claude-new-constitution
  - The document itself is dated Jan 21, 2026 and released under CC0 1.0. https://www.anthropic.com/constitution
  - It sets a priority order: broadly safe, then broadly ethical, then compliant with Anthropic's guidelines, then genuinely helpful. **UNVERIFIED (partial):** this order comes from a summary, not a direct read of the document.

### Responsible Scaling Policy (RSP)

Source for the version history: https://www.anthropic.com/responsible-scaling-policy

| Version | Effective date | Note |
|---|---|---|
| 1.0 | Sept 19, 2023 | First version |
| 2.0 | Oct 15, 2024 | |
| 2.1 | Mar 31, 2025 | |
| 2.2 | May 14, 2025 | |
| 3.0 | Feb 24, 2026 | Full rewrite |
| 3.1 | Apr 2, 2026 | |
| 3.2 | Apr 29, 2026 | |
| 3.3 | May 26, 2026 | |
| **3.4** | **Jul 8, 2026** | **Current** |

ASL (AI Safety Level) facts:
- **ASL-3 activation:** ASL-3 protections were activated May 22, 2025, alongside the launch of Claude Opus 4, as a precaution. https://www.anthropic.com/news/activating-asl3-protections
  - The same post calls ASL-2 the baseline standard.
  - It also states "We have ruled out that Claude Opus 4 needs the ASL-4 Standard."
- **Current models:** the Transparency Hub says Claude Opus 5 and Claude Fable 5.1 were deployed with ASL-3 protections. https://www.anthropic.com/transparency
- **UNVERIFIED:**
  - The formal definitions of each ASL level (ASL-1 to ASL-4+). The current RSP v3.x page does not define them in the same way the 2023 policy did.
  - Any activation of ASL-4. No official statement was found.

### Interpretability and other research highlights

| Research | Date | Source |
|---|---|---|
| "Towards Monosemanticity" (dictionary learning / features) | Oct 2023 | https://transformer-circuits.pub/2023/monosemantic-features |
| "Scaling Monosemanticity" / "Mapping the Mind of a Large Language Model" (features found in Claude 3 Sonnet) | May 21, 2024 | https://www.anthropic.com/research/mapping-mind-language-model |
| Golden Gate Claude | May 23, 2024 | https://www.anthropic.com/research/golden-gate-claude |
| Alignment faking (with Redwood Research) | Dec 18, 2024 | https://www.anthropic.com/research/alignment-faking |
| Anthropic Economic Index | Feb 10, 2025 | https://www.anthropic.com/research/the-anthropic-economic-index |
| "Tracing the thoughts of a large language model": the "Circuit Tracing" and "On the Biology of a Large Language Model" papers (studying Claude 3.5 Haiku) | Mar 27, 2025 | https://www.anthropic.com/research/tracing-thoughts-language-model ; https://transformer-circuits.pub/2025/attribution-graphs/biology.html |
| Exploring model welfare | Apr 24, 2025 | https://www.anthropic.com/research/exploring-model-welfare |
| Circuit-tracing tools open-sourced | May 29, 2025 (**date from a search summary**) | https://www.anthropic.com/research/open-source-circuit-tracing |
| Agentic misalignment (16 models tested) | Jun 20, 2025 | https://www.anthropic.com/research/agentic-misalignment |
| Signs of introspection in LLMs | Oct 29, 2025 | https://www.anthropic.com/research/introspection |
| Project Glasswing, a cybersecurity initiative launched with the unreleased Claude Mythos Preview | Apr 7, 2026 | https://www.anthropic.com/glasswing |
| Commitments on model deprecation and preservation (preserving model weights) | (date not checked) | https://www.anthropic.com/research/deprecation-commitments |

---

## 3. Claude model history

Release dates for the 4.5 generation onward come from each model's docs page. Earlier dates come from anthropic.com announcement posts.

| Model | Released / announced | Notes | Source |
|---|---|---|---|
| Claude (1) and Claude Instant | Mar 14, 2023 | Claude Instant was described as "a lighter, less expensive, and much faster option" | https://www.anthropic.com/news/introducing-claude |
| Claude 2 | Jul 11, 2023 | Came with a public beta chat experience at claude.ai | https://www.anthropic.com/news/claude-2 |
| Claude 2.1 | Nov 21, 2023 | 200K-token context window | https://www.anthropic.com/news/claude-2-1 |
| Claude 3 Opus and Claude 3 Sonnet | Mar 4, 2024 | At launch, the post said "Haiku will be available soon". 200K context. | https://www.anthropic.com/news/claude-3-family |
| Claude 3 Haiku | Mar 13, 2024 | Available that day through the API and to Claude Pro subscribers | https://www.anthropic.com/news/claude-3-haiku |
| Claude 3.5 Sonnet | June 2024 | Artifacts introduced at the same time. **The date conflicts:** the fetched page shows June 21, 2024, but the model ID is `claude-3-5-sonnet-20240620`. Confirm June 20 vs 21 by eye before printing. | https://www.anthropic.com/news/claude-3-5-sonnet |
| Upgraded Claude 3.5 Sonnet, Claude 3.5 Haiku, computer use (beta) | Oct 22, 2024 | The post said 3.5 Haiku would arrive "later this month" | https://www.anthropic.com/news/3-5-models-and-computer-use |
| Claude 3.7 Sonnet, plus Claude Code (research preview) | Feb 24, 2025 | Called "the first hybrid reasoning model on the market" | https://www.anthropic.com/news/claude-3-7-sonnet |
| Claude Opus 4 and Claude Sonnet 4 | May 22, 2025 | Claude Code became generally available the same day | https://www.anthropic.com/news/claude-4 |
| Claude Opus 4.1 | Aug 5, 2025 | | https://www.anthropic.com/news/claude-opus-4-1 |
| Claude Sonnet 4.5 | Sep 29, 2025 | | https://www.anthropic.com/news/claude-sonnet-4-5 |
| Claude Haiku 4.5 | Oct 15, 2025 | | https://platform.claude.com/docs/en/models/haiku-4-5/overview |
| Claude Opus 4.5 | Nov 24, 2025 | | https://platform.claude.com/docs/en/models/opus-4-5/overview |
| Claude Opus 4.6 | Feb 5, 2026 | | https://platform.claude.com/docs/en/models/opus-4-6/overview |
| Claude Sonnet 4.6 | Feb 17, 2026 | | https://platform.claude.com/docs/en/models/sonnet-4-6/overview |
| Claude Mythos Preview | Apr 7, 2026 | Invitation-only, through Project Glasswing. Now deprecated (June 9, 2026). | https://www.anthropic.com/glasswing ; https://platform.claude.com/docs/en/about-claude/model-deprecations |
| Claude Opus 4.7 | Apr 16, 2026 | Introduced the newer tokenizer | https://platform.claude.com/docs/en/models/opus-4-7/overview |
| Claude Opus 4.8 | May 28, 2026 | | https://platform.claude.com/docs/en/models/opus-4-8/overview |
| **Claude Fable 5** and **Claude Mythos 5** | Jun 9, 2026 | The first Fable model | https://platform.claude.com/docs/en/models/fable-5/overview ; https://www.anthropic.com/news/claude-fable-5-mythos-5 |
| Claude Sonnet 5 | Jun 30, 2026 | | https://platform.claude.com/docs/en/models/sonnet-5/overview |
| Claude Opus 5 | Jul 24, 2026 | | https://platform.claude.com/docs/en/models/opus-5/overview |
| **Claude Fable 5.1** and **Claude Mythos 5.1** | Sep 1, 2026 | | https://platform.claude.com/docs/en/models/fable-5-1/overview |
| **Claude Opus 5.5** | Sep 22, 2026 | | https://platform.claude.com/docs/en/models/opus-5-5/overview |
| **Claude Sonnet 5.5** | Sep 28, 2026 | | https://platform.claude.com/docs/en/models/sonnet-5-5/overview |
| **Claude Haiku 5.5** | Oct 7, 2026 | | https://platform.claude.com/docs/en/models/haiku-5-5/overview |

Retirements are listed at https://platform.claude.com/docs/en/about-claude/model-deprecations:
- Claude 1.x and Instant 1.x retired Nov 6, 2024.
- Claude 2.0, 2.1 and Claude 3 Sonnet retired Jul 21, 2025.
- Claude 3.5 Sonnet (both versions) retired Oct 28, 2025.
- Claude 3 Opus retired Jan 5, 2026.
- Claude 3.7 Sonnet and Claude 3.5 Haiku retired Feb 19, 2026.
- Claude 3 Haiku retired Apr 20, 2026.
- Claude Opus 4 and Claude Sonnet 4 retired Jun 15, 2026.
- Claude Opus 4.1 retired Aug 5, 2026.
- Claude Sonnet 4.5 is deprecated and retires Nov 30, 2026.

### What is "Fable"?

**Claude Fable is a new top tier, above Opus.** It is not a new name for Opus, Sonnet or Haiku.

What the official sources say:
- **Launch post (Jun 9, 2026):** Fable 5 is "a Mythos-class model that we've made safe for general use", and Anthropic's most capable generally available model. https://www.anthropic.com/news/claude-fable-5-mythos-5
- **Safety classifiers:** Fable runs safety classifiers covering cybersecurity, biology/chemistry, and distillation.
  - At Fable 5's launch, a request flagged by a classifier was answered by "our next-most-capable model, Claude Opus 4.8".
  - Anthropic says more than 95% of sessions involve no fallback. (Same source.)
- **Fable vs Mythos:** Claude Mythos is "the same underlying model" as Fable, "with the safeguards lifted in some areas".
  - Mythos 5.1 shares Fable 5.1's specifications and pricing.
  - It is available only to organizations verified through programs such as the Cyber Verification Program. The announcement also names the Life Sciences Verification Program.
  - Sources: https://platform.claude.com/docs/en/models/fable-5-1/overview ; https://www.anthropic.com/claude-fable-and-mythos-5-1
- **Fable vs the Opus/Sonnet/Haiku lineup** (models overview):
  - Fable 5.1 is "for demanding reasoning and long-horizon agentic work".
  - It has "Slower" comparative latency.
  - It costs $10/$50 per MTok, versus $4/$20 for Opus 5.5.
  - Anthropic recommends starting with Opus 5.5 "for most workloads". Use Fable 5.1 when evals on Opus 5.5 at higher effort still fall short.
  - Source: https://platform.claude.com/docs/en/about-claude/models/overview.md
- **API differences:**
  - Thinking is always on (adaptive).
  - Default effort is `high`.
  - Forced tool use returns an error on 5.1.
  - Cache reads cost 0.025× the base input price.
  - Source: https://platform.claude.com/docs/en/models/fable-5-1/overview
- **Plan history:** Fable 5 was included on Pro, Max, Team and seat-based Enterprise plans only through June 22, 2026. After that it needed usage credits. https://www.anthropic.com/news/claude-fable-5-mythos-5

---

## 4. Current models (Claude API)

Main source: https://platform.claude.com/docs/en/about-claude/models/overview.md. Pricing: https://platform.claude.com/docs/en/about-claude/pricing.md

| | Claude Fable 5.1 | Claude Opus 5.5 | Claude Sonnet 5.5 | Claude Haiku 5.5 |
|---|---|---|---|---|
| Positioning | Demanding reasoning, long-horizon agentic work | Long-running agentic coding and knowledge work (recommended starting point) | Best combination of speed and intelligence | High-volume, latency-sensitive tasks (classification, extraction, routing) |
| API ID (= alias) | `claude-fable-5-1` | `claude-opus-5-5` | `claude-sonnet-5-5` | `claude-haiku-5-5` |
| Released | Sep 1, 2026 | Sep 22, 2026 | Sep 28, 2026 | Oct 7, 2026 |
| Context window | 1M tokens | 1M | 1M | 1M |
| Max output | 128K tokens (sync) | 128K (300K on Batch API with a beta header) | 128K (300K Batch, beta) | 128K (300K Batch, beta) |
| Reliable knowledge cutoff / training data cutoff | Jun 2026 / Jun 2026 | Jun 2026 / Jun 2026 | Jun 2026 / Jun 2026 | Jun 2026 / Jun 2026 |
| Input / output price per MTok | $10 / $50 | $4 / $20 | $2 / $10 | $0.10 / $0.50 (prompts up to 100K tokens); $0.50 / $2.50 (over 100K) |
| Cache read per MTok | $0.25 (0.025×) | $0.20 (0.05×) | $0.10 (0.05×) | $0.01 / $0.05 (0.1×) |
| Thinking | Adaptive, always on | Adaptive, always on | Adaptive (`between_tools` turns off up-front thinking) | Adaptive |
| Default effort | `high` | `medium` | `high` | `medium` |
| Comparative latency | Slower | Moderate | Fast | Fastest |
| Amazon Bedrock ID | `anthropic.claude-fable-5-1` | `anthropic.claude-opus-5-5` | `anthropic.claude-sonnet-5-5` | `anthropic.claude-haiku-5-5` |
| Google Cloud (Vertex / Google managed) ID | `claude-fable-5-1` | `claude-opus-5-5` | `claude-sonnet-5-5` | `claude-haiku-5-5` |
| Microsoft Foundry ID | `claude-fable-5-1` | `claude-opus-5-5` | `claude-sonnet-5-5` | `claude-haiku-5-5` |
| Retirement (earliest) | Not before Sep 1, 2027 | Not before Sep 22, 2027 | Not before Sep 28, 2027 | Not before Oct 7, 2027 |

Notes from the same sources:
- **Discounts:** Batch API requests are 50% off.
- **Cache writes:** writing to the cache costs 1.25× the base input price for the 5-minute cache and 2× for the 1-hour cache.
- **Other platforms:** all four models are also on Claude Platform on AWS and on Claude Models on Google Cloud (Anthropic managed).
- **Thinking terms:**
  - "Extended thinking" is the manual `budget_tokens` mode on earlier models.
  - It is deprecated on Opus 4.6 and Sonnet 4.6, and not accepted on later models.
- **Tokenizer:** Claude 4.7 and later use a newer tokenizer. It produces "approximately 30% more tokens for the same text".
- **Fast mode:** available for Opus 5.5 on the Claude API.
- **Model IDs:** from the 4.6 generation onward, model IDs have no date and are pinned snapshots.
- **Partner pricing:** Bedrock and Vertex set their own prices.

**Older models still available ("legacy"):**

| Model | Input / output per MTok | Context |
|---|---|---|
| Fable 5 | $10 / $50 | 1M |
| Opus 5 | $5 / $25 | 1M |
| Opus 4.8 | $5 / $25 | 1M |
| Opus 4.7 | $5 / $25 | 1M |
| Opus 4.6 | $5 / $25 | 1M |
| Opus 4.5 | $5 / $25 | 200K |
| Sonnet 5 | $2 / $10 | 1M |
| Sonnet 4.6 | $3 / $15 | 1M |
| Haiku 4.5 | $1 / $5 | 200K |

Sources: same overview and pricing pages.

---

## 5. Products and plans (claude.ai / Claude apps)

Main source: https://claude.com/pricing.

**Caveat:** these pages were read through a summarising fetch tool. Re-check prices and plan boundaries by eye before printing.

### Plans

**Free ($0)**
- "Limited usage", with limits that reset every 5 hours and every week.
- Models: Sonnet and Haiku only. No Opus, Fable or Claude Code.
- Includes web search, file creation, memory, connectors, Artifacts, Skills, incognito and voice.
- Projects: up to 5.

**Pro**
- $20 per month billed monthly, or $17 per month billed annually.
- "More usage than Free".
- Models: Opus, Sonnet and Haiku. Fable is available only through usage credits.
- Includes Claude Code, Research, Claude in Chrome and Microsoft 365 add-ins.

**Max ($100 per month)**
- "5x Pro usage".
- Fable "included, up to half your weekly limit".
- $100 per month in API credits.
- Priority access.

**Ultra ($200 per month): NEW**
- "No 5-hour limit" (for verified accounts).
- "10x Pro usage every week".
- $200 per month in API credits.
- The checkout link uses `plan=max_20x`, so Ultra appears to replace the old "Max 20x".

**Team** ("for teams of 2 to 150")

| Seat type | Billed monthly | Billed annually |
|---|---|---|
| Standard | $25 per month | $20 per month |
| Premium (5x more usage than Standard) | $125 per month | $100 per month |

- Includes Claude Code, Cowork, Claude Tag (Slack), Microsoft 365, and up to $500 per month in pooled API credits.
- Admin features: SSO, domain verification, central billing, connector controls, usage analytics, and org-wide skills.
- Not on Team: SCIM, audit logs, role-based access and domain capture.

**Enterprise**
- "US$20/seat/month, billed annually, 20 seat minimum", plus usage at API rates.
- Adds SCIM, audit logs, role-based access, Compliance API, custom data retention, domain capture, IP allowlisting, spend limits and a HIPAA-ready option.

**Usage-limit wording** (from the pricing page): "How fast you reach a limit depends on the model you use, how long your chats are, and how large your files are." https://claude.com/pricing

### Apps and surfaces

**Web, desktop and mobile** (https://claude.com/download)
- Web: claude.ai.
- Desktop: macOS and Windows (x64 and ARM64). Linux is in beta.
- Mobile: iOS and Android.
- These apps are on all plans.

**Claude in Chrome** (https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome ; release notes: https://support.claude.com/en/articles/12138966-release-notes)
- A browser extension "that allows Claude to read, click, and navigate websites".
- Paid plans only.
- Launched as experimental Aug 26, 2025, and became a beta for all paid plans Dec 18, 2025.

**Claude for Excel, PowerPoint and Word** (https://claude.com/claude-for-microsoft-365)
- Excel launched in beta Nov 24, 2025.
- The PowerPoint add-in launched Feb 5, 2026.
- Outlook and Google Workspace versions are in beta.
- Not available on Free.

**Claude Tag (Claude in Slack)** (https://claude.com/product/overview)
- "Work with Claude directly in Slack."
- In beta for Team and Enterprise.

**Claude Cowork** (https://claude.com/product/cowork)
- Research preview Jan 12, 2026 (Max plan, macOS).
- Generally available on macOS and Windows Apr 9, 2026.
- Available on web and mobile Jul 7, 2026.
- Paid plans only.

**Claude Code**
- Surfaces: terminal (CLI), VS Code and Cursor, JetBrains (beta), desktop app, web (claude.ai/code), iOS/Android, GitHub Actions and Slack.
- Plans: Pro, Max, Ultra, Team, Enterprise, or a Console (API) account.
- Research preview Feb 24, 2025 (https://www.anthropic.com/news/claude-3-7-sonnet). Generally available May 22, 2025 (https://www.anthropic.com/news/claude-4).
- Sources: https://claude.com/product/claude-code ; https://code.claude.com/docs/en/overview

### Features

| Feature | Official description and plans | Source |
|---|---|---|
| Projects | "Self-contained workspaces with their own chat histories and knowledge bases". All plans (Free: up to 5). Sharing on Team and Enterprise only. | https://support.claude.com/en/articles/9517075-what-are-projects |
| Artifacts | Introduced with Claude 3.5 Sonnet (June 2024). On all plans today. | https://www.anthropic.com/news/claude-3-5-sonnet ; https://claude.com/product/overview |
| Research | Runs a series of connected web searches. Paid plans only. | https://support.claude.com/en/articles/11088861-use-research-on-claude |
| Web search | All plans. On Team and Enterprise, an owner must enable it. | https://support.claude.com/en/articles/10684626-enable-and-use-web-search |
| Connectors | Connect Claude to apps. Custom connectors use remote MCP servers. All plans (Free: one custom connector). | https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities |
| Memory | On by default for consumer plans. Reached Free users Mar 2, 2026. Chat search requires a paid plan. | https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context |
| Skills | "Reusable folders of instructions, scripts, and resources". All plans. Code execution must be on. | https://support.claude.com/en/articles/12512176-what-are-skills |
| File creation | .xlsx, .pptx, .docx and PDF files. Launched Sep 9, 2025. | https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude |
| Voice mode | In beta. All plans. | https://support.claude.com/en/articles/11101966 |
| Incognito chats | Not saved to chat history or memory. Launched Sep 11, 2025. | https://support.claude.com/en/articles/12260368-use-incognito-chats |
| Sharing | Snapshot links. Team and Enterprise users can share only within their organization. | https://support.claude.com/en/articles/10593882-share-and-unshare-chats |
| Export | Settings > Privacy, on web and desktop only | https://support.claude.com/en/articles/9450526-export-your-claude-data |
| Styles | **UNVERIFIED.** No current official page was found, so this feature may be retired. The personalization help article now points to Skills instead. | https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features |

---

## 6. Developer platform

Release notes: https://platform.claude.com/docs/en/release-notes/overview.md

### Console and branding

- **Rebrand (Sep 16, 2025):** Anthropic moved its developer products to the Claude brand. The Console moved from console.anthropic.com to platform.claude.com, and the docs moved from docs.anthropic.com to docs.claude.com.
- **Redirect:** console.anthropic.com has redirected to platform.claude.com since Jan 12, 2026.
- **Workbench is retired:**
  - The legacy Workbench closed Aug 17, 2026, and the experimental prompt-generate/improve/templatize APIs were retired the same day.
  - The Workbench's replacement is now called "playground" (release note dated Aug 18, 2026).
  - Help centre: https://support.claude.com/en/articles/8606378-how-do-i-use-the-workbench
- **Workspaces:** they group API keys, members and limits, with up to 100 per organization. https://platform.claude.com/docs/en/manage-claude/workspaces.md

### Messages API

Source: https://platform.claude.com/docs/en/api/overview.md and https://platform.claude.com/docs/en/api/messages.md

- **Endpoint:** `POST /v1/messages`.
- **Required fields:** `model`, `max_tokens`, `messages`.
- **Optional `system` field:** holds the system prompt.
- **Streaming:** set `stream: true` to receive server-sent events.
- **Roles:** `user` and `assistant` take turns.
- **Authentication:** current docs show `Authorization: Bearer <key>`. `x-api-key` is listed as a "legacy fallback… still supported".
- **Required headers:** `anthropic-version` and `content-type: application/json`.
- **API version:** the current version is **`2026-10-21`**, released Oct 21, 2026. Earlier versions were `2023-06-01` and `2023-01-01`. https://platform.claude.com/docs/en/api/versioning.md

### Features

Feature overview: https://platform.claude.com/docs/en/build-with-claude/overview.md. Dates are from the release notes.

- **Tool use:** https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview.md
  - Client tools (your own tools, plus Anthropic-defined `bash` and `text_editor`) run in your app.
  - Server tools run on Anthropic's servers: web search, web fetch, code execution and tool search.
  - Memory and computer use are stable.
- **Prompt caching:** https://platform.claude.com/docs/en/build-with-claude/prompt-caching.md
  - Beta Aug 14, 2024. Generally available Dec 17, 2024.
  - Default cache lifetime is 5 minutes. A 1-hour option is also available.
- **Message Batches API:** https://platform.claude.com/docs/en/build-with-claude/batch-processing.md
  - Beta Oct 8, 2024. Generally available Dec 17, 2024.
  - 50% discount. Most batches finish in under 1 hour.
- **Files API:** beta May 22, 2025. Now stable.
- **Citations:** Jan 23, 2025.
- **Structured outputs:** beta Nov 14, 2025. Generally available Jan 29, 2026.
- **Effort parameter:** beta Nov 24, 2025. Generally available Feb 5, 2026.
- **Context editing (beta):** Sep 29, 2025.
- **Compaction (beta):** Feb 5, 2026.
- **Managed Agents (beta):** Apr 8, 2026.

### Claude Agent SDK

- Renamed from the "Claude Code SDK" on Sep 29, 2025. https://claude.com/blog/building-agents-with-the-claude-agent-sdk
- Available for Python (`claude-agent-sdk`) and TypeScript (`@anthropic-ai/claude-agent-sdk`).
- Gives developers "the same tools, agent loop, and context management that power Claude Code". https://code.claude.com/docs/en/agent-sdk/overview

### Model Context Protocol (MCP)

- **Announced Nov 25, 2024** as "an open standard that enables developers to build secure, two-way connections between their data sources and AI-powered tools". https://www.anthropic.com/news/model-context-protocol
- **Donated Dec 9, 2025** to the Agentic AI Foundation, a directed fund under the Linux Foundation. https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation
  - Co-founders: Anthropic, Block and OpenAI.

### Agent Skills

- **Announced Oct 16, 2025.** https://claude.com/blog/skills
  - In the API, Skills launched in beta with `/v1/skills` and ready-made skills for pptx, xlsx, docx and pdf files.
- **Open standard:** published as an open standard at agentskills.io on Dec 18, 2025 (per an update to the same post).
- **Status now:** the docs list Skills as stable. https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview.md

---

## UNVERIFIED / conflicting items (summary)

1. **Founding year (2021):** comes only from a search snippet of the Series B post. No /company page states a founding year.
2. **Funding dates:** the dates of Series F and Series G were not confirmed.
3. **Trustee dates:** the appointment dates for Bernanke and Stubbs come from search summaries.
4. **Constitution:** the priority order of the 2026 constitution comes from a summary, not a direct read.
5. **ASL levels:** the definitions of each ASL level are not in the current RSP v3.4 page as fetched. No activation of ASL-4 was found.
6. **Claude 3.5 Sonnet release date:** June 20 or June 21, 2024. The page shows June 21, but the model ID says 20240620.
7. **Claude 3.5 Haiku:** the exact date it became available was not confirmed. The post only says "later this month" (October 2024).
8. **Styles:** no current official page was found. It may be retired.
9. **Plans:**
   - "Max 20x" now seems to be called "Ultra".
   - No annual prices are listed for Max or Ultra.
   - The plan figures were read through a summarising tool, so verify them by eye.
10. **"Claude Developer Platform":** current docs say "Claude Console" or "Claude Platform". The exact name "Claude Developer Platform" was not found.
11. **Skills API:** whether it is fully out of beta is unclear. The docs page says "stable", but the API reference is still under `/api/beta/skills`.
12. **Agent Skills and the AAIF:** a claim that Agent Skills moved to the Agentic AI Foundation in Oct 2026 appears only on a third-party blog.
13. **Old Console tools:** whether the prompt generator, prompt improver and evaluation tool still exist in the Console after Aug 17, 2026 was not confirmed.
