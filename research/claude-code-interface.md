# Claude Code user-facing interface: verified reference

**Verified on 2026-11-09 against Claude Code 2.1.319** (local `claude --help` and subcommand `--help` output, plus the official docs at https://code.claude.com/docs/en/, which the changelog shows are current through 2.1.319).

How to read this file:

- **Source** gives the docs page (`https://code.claude.com/docs/en/<page>`) or "local --help". Where both agree, both are listed.
- **UNVERIFIED** means the item could not be confirmed in the official docs, or appears only in one source. Do not teach it as fact without checking again.
- Version notes ("requires v2.1.xxx") come from the docs. The local version (2.1.319) is newer than every version requirement quoted here.
- Docs base URL abbreviations: `commands` = https://code.claude.com/docs/en/commands, `cli-reference` = https://code.claude.com/docs/en/cli-reference, `interactive-mode` = https://code.claude.com/docs/en/interactive-mode, and so on.

---

## 0. Surprises and changes a textbook author should know

| Topic | What changed | Source |
|---|---|---|
| Default permission mode | Since v2.1.283, new interactive terminal and VS Code sessions **start in `auto` mode** (a classifier reviews actions), not in the mode that asks before everything. `claude -p` and the Agent SDK still start in `default`. | permission-modes |
| "default" mode renamed in the UI | The ask-before-acting mode is labelled **Manual** in the UI and in `claude --help`. Its config value is still `default`, and `manual` is accepted as an alias. | permission-modes, cli-reference, local --help |
| `#` memory shortcut | **Removed** in v2.0.70 ("Removed # shortcut for quick memory entry (tell Claude to edit your CLAUDE.md instead)"). Starting a message with `#` no longer saves a memory. | changelog |
| `/vim` | Removed in v2.1.92. Use `/config` → Editor mode. | commands |
| `/pr-comments` | Removed in v2.1.91. | commands |
| `/ultraplan` | Removed. Use plan mode instead. | commands |
| `/review` | Now an alias of `/code-review` (since v2.1.223). | commands |
| `/agents` | No longer opens a management UI (since after v2.1.197). It prints a reminder to ask Claude, or to edit `.claude/agents/` directly. | commands |
| `/bug` vs `/feedback` | Before v2.1.212 `/bug` was an alias of `/feedback`. Now `/bug` (alias `/share`) and `/feedback` are separate commands that open the same dialog. | commands |
| `/extra-usage` | Renamed `/usage-credits`. | commands |
| `/schedule` | Now creates "cloud scheduled tasks" (formerly "routines"). Alias `/routines`. | commands |
| `--remote` | Deprecated alias for `--cloud`. | cli-reference |
| `--enable-auto-mode` | Removed in v2.1.111. Use `--permission-mode auto`. | cli-reference |
| Vertex AI naming | The docs now call Google Vertex AI **"Google Cloud's Agent Platform"**. The env var is still `CLAUDE_CODE_USE_VERTEX` and the wizard is `/setup-vertex`. | authentication, env-vars |
| Models | Aliases now include `fable` and `best`. On the Anthropic API, `opus`/`sonnet`/`haiku` resolve to Opus 5.5 / Sonnet 5.5 / Haiku 5.5. `default` resolves to Opus 5.5 on Pro, Max, Ultra, Team, Enterprise and the API. | model-config |
| Effort defaults | Opus 5.5, Sonnet 5.5 and Haiku 5.5 default to **`medium`** effort. Most other models default to `high`. | model-config |
| Thinking toggle | You cannot turn extended thinking off on Opus 5.5, Sonnet 5.5, Haiku 5.5 or Fable models. | model-config |
| New plan tier | Docs list "Pro, Max, **Ultra**, Team, Enterprise" plans throughout. | authentication, setup |
| Background agents | Agent view (`claude agents`, `--bg`, `attach`, `logs`, `stop`, `rm`, `respawn`) is a **research preview**. | agent-view |
| `ultrathink` | The only recognized thinking keyword. "think", "think hard" and similar are passed through as ordinary text. | model-config |

---

## 1. Slash commands (in-session commands)

Source for every row: https://code.claude.com/docs/en/commands unless noted.

General rules (commands page):

- A command is recognized **only at the start of a message**. Text after the command name becomes its arguments.
- `<arg>` = required, `[arg]` = optional.
- If you send a command while Claude is responding, it is queued until the turn ends. Some, such as `/status`, `/tasks` and `/usage`, run immediately.
- Not every command shows for every user. Availability depends on platform, plan and provider. Some (for example `/heapdump`, `/setup-bedrock`, `/setup-vertex`) are hidden from the menu and run only when you type the full name.
- You can chain up to six skills in one message: `/skill-a /skill-b do XYZ`.
- MCP servers can expose prompts that appear as commands (see https://code.claude.com/docs/en/mcp).

### 1a. Built-in commands vs bundled skills vs workflows

The docs split the commands table into three kinds:

- **Built-in command**: behaviour coded into the CLI. This is most of them.
- **Bundled skill** (marked "Skill" in the docs): "prompt-based: they give Claude detailed instructions and let it orchestrate the work using its tools" (https://code.claude.com/docs/en/skills#bundled-skills). Turn them off with the `disableBundledSkills` setting.
- **Workflow** (marked "Workflow"): a bundled dynamic workflow that fans out across many subagents in the background. Currently only `/deep-research`.

**Bundled skills according to the docs:** `/artifact-capabilities`, `/artifact-diagramming`, `/batch`, `/claude-api`, `/claude-in-chrome`, `/code-review` (alias `/review`), `/dataviz`, `/debug`, `/design`, `/design-sync`, `/doctor`, `/fewer-permission-prompts`, `/loop`, `/run`, `/run-skill-generator`, `/simplify`, `/slides`, `/update-config`, `/verify`, `/workflow-authoring`. `/plugin-authoring` is a skill from a built-in plugin.

> **Discrepancy:** the docs table does **not** mark `/init`, `/security-review` or `/schedule` as skills; it lists them as ordinary commands. In a local 2.1.319 session, however, the agent's skill list did include `init`, `security-review` and `schedule` as skills. For a textbook, describe them simply as "commands". **UNVERIFIED** which category is canonical.

### 1b. Full command table

| Command and syntax | What it does | Kind / notes |
|---|---|---|
| `/add-dir <path>` | Adds another working directory that Claude may read and edit this session. | Built-in. Most `.claude/` config is not discovered from the added dir. |
| `/advisor [model\|off]` | Turns the advisor tool on or off; the advisor consults a second model (`fable`, `opus`, `sonnet` or a full ID) at key moments. | Built-in. |
| `/agents` | Prints a reminder to ask Claude to create or manage subagents, or to edit `.claude/agents/` / `~/.claude/agents/`. | Built-in. **Changed**: it was an interactive UI up to v2.1.197. |
| `/artifact-capabilities` | Loads the reference for runtime capabilities that published artifacts can use. | Skill. Only where artifacts are available. |
| `/artifact-diagramming` | Loads diagramming guidance for artifacts. | Skill. |
| `/artifacts` | Lists your artifacts, then attaches, opens or copies a link to one. | Built-in. |
| `/auto-mode-setup` | Drafts `autoMode.environment` entries from your project and saves them to user settings after you review them. | Built-in. |
| `/autocompact [auto\|<tokens>]` | Sets how full the context gets before auto-compaction, for example `500k`, or `auto`. | Built-in. Saved to user settings. |
| `/autofix-pr [prompt]` | Starts a cloud session that watches the current branch's PR and pushes fixes for CI failures and review comments. | Built-in. Needs `gh` and cloud sessions. |
| `/background [prompt]` | Detaches the current session to run as a background agent and frees the terminal. | Built-in. Alias `/bg`. |
| `/batch <instruction>` | Plans a large change, splits it into 5–30 units and runs each in its own worktree with a background subagent. | Skill. Needs a git repo (or a WorktreeCreate hook). |
| `/branch [name]` | Copies the conversation at this point and switches you into the copy; the original stays resumable. | Built-in. |
| `/btw [question]` | Asks a side question about the session without adding it to the conversation history. | Built-in. |
| `/bug [report]` | Reports a bug or shares the conversation after a consent screen. | Built-in. Alias `/share`. |
| `/cd <path>` | Moves the session to another working directory, keeping the conversation. | Built-in. |
| `/chrome` | Configures Claude in Chrome settings. | Built-in. |
| `/claude-api [subcommand]` | Loads Claude API / Managed Agents reference material for your project's language. | Skill. Subcommands include `migrate`, `upgrade`, `api-version`, `prompt-audit`, `cost-optimize`, `build-eval`, and others. |
| `/claude-in-chrome [task]` | Has Claude carry out a task in your browser through Claude in Chrome. | Skill. |
| `/clear [name]` | Starts a new conversation with empty context. The old one stays resumable, and the optional name labels it. | Built-in. Aliases `/reset`, `/new`. |
| `/code-review [low\|medium\|high\|xhigh\|max\|ultra] [--fix] [--comment] [--max-findings n\|all\|default] [pr#\|branch\|path]` | Reviews the current diff, or a given PR/branch/path, for correctness bugs. `--fix` applies findings, `--comment` posts them, `ultra` runs a cloud review. | Skill. Alias `/review`. |
| `/color [color\|default]` | Sets the prompt-bar colour: `red`, `blue`, `green`, `yellow`, `purple`, `orange`, `pink` or `cyan`. | Built-in. |
| `/compact [instructions]` | Summarizes the conversation so far to free context, optionally focused by your instructions. | Built-in. |
| `/config [key=value ...]` | Opens the Settings UI (theme, model, output style and so on), or sets keys directly, for example `/config theme=dark`. | Built-in. Alias `/settings`. `/config --help` lists keys. |
| `/context [all]` | Shows context-window usage as a coloured grid, with suggestions. | Built-in. |
| `/copy [N]` | Copies the last (or Nth-latest) response to the clipboard. A picker lets you choose code blocks, and `w` writes to a file. | Built-in. |
| `/cost` | Alias for `/usage`. | Built-in. |
| `/dataviz [request]` | Design guidance for charts and dashboards. | Skill. |
| `/debug [description]` | Turns on debug logging for this session and troubleshoots using the debug log. | Skill. |
| `/deep-research <question>` | Fans out web searches and writes a cited report. | Workflow. |
| `/design [brief]` | Drafts UI mockups as a Claude Design artifact. | Skill. Needs artifacts; not on Bedrock, Agent Platform or Foundry. |
| `/design consent`, `/design revoke` | Grants or withdraws Claude's access to Claude Design. | Built-in. |
| `/design-login` | Authorizes design-system access for `/design-sync`. | Built-in. The standalone claude.ai/design site closes by 14 Dec 2026. |
| `/design-sync [hint]` | Converts your repo's React design system and uploads it to Claude Design. | Skill. |
| `/desktop` | Continues the current session in the Claude Desktop app. | Built-in. macOS / x64 Windows plus a subscription. Alias `/app`. |
| `/diff` | Shows working-tree changes, including Claude's edits. | Built-in. |
| `/doctor [prompt-audit [path]]` | Runs a setup checkup of installation, settings, extensions and CLAUDE.md, and offers fixes that Claude applies after you confirm. | **Skill** (despite sounding built-in). Alias `/checkup`. |
| `/effort [level\|auto\|status\|ultracode [on\|off]]` | Sets the effort level (`low`…`xhigh`, `max`, `auto`), prints it (`status`), or toggles ultracode. | Built-in. `max` lasts for the session only. |
| `/exit` | Exits the CLI; in an attached background session it detaches instead. | Built-in. Alias `/quit`. |
| `/export [filename]` | Exports the conversation as plain text. | Built-in. |
| `/fast [on\|off]` | Toggles fast mode. | Built-in. |
| `/feedback [report]` | Sends product feedback, using the same dialog as `/bug`. | Built-in. |
| `/fewer-permission-prompts` | Scans transcripts and adds a read-only allowlist to `.claude/settings.json`. | Skill. |
| `/focus` | Toggles focus view: last prompt, a tool summary and the final answer only. | Built-in. Fullscreen rendering only. |
| `/fork [prompt]` | Copies the conversation into a new background session while you keep working here. | Built-in. |
| `/goal [condition\|clear]` | Sets a goal; Claude keeps working across turns until the condition is met. | Built-in. |
| `/heapdump` | Writes a heap snapshot and memory breakdown for diagnosing memory problems. | Built-in. Hidden from the menu. The snapshot contains credentials, so don't share it. |
| `/help` | Shows help and available commands. | Built-in. |
| `/hooks` | Views hook configurations. | Built-in. |
| `/ide` | Manages IDE integrations and shows their status. | Built-in. |
| `/import [codex\|gemini\|cursor] [--dry-run] [--yes]` | Imports config (instructions, MCP servers, commands, skills) from Codex, Gemini CLI or Cursor. | Built-in. Not on Bedrock, Agent Platform or Foundry. |
| `/init` | Creates a starter `CLAUDE.md` for the project. `CLAUDE_CODE_NEW_INIT=1` gives an interactive flow. | Built-in per docs (see the discrepancy above). |
| `/insights` | Writes an HTML report analysing your recent sessions. | Built-in. |
| `/install-github-app` | Installs the Claude GitHub App and optionally sets up GitHub Actions. | Built-in. github.com only. |
| `/install-slack-app` | Installs the Claude Slack app through OAuth. | Built-in. |
| `/keybindings` | Opens your keyboard-shortcuts file (`~/.claude/keybindings.json`). | Built-in. |
| `/list-agents` | Lists subagents, teammates and other sessions Claude can message. | Built-in. Also `/peers`. Only with cross-session messaging. |
| `/login` | Signs in to your Anthropic account. | Built-in. |
| `/logout` | Signs out. | Built-in. |
| `/loop [interval] [prompt]` | Re-runs a prompt on an interval while the session is open, for example `/loop 5m check if the deploy finished`. With no interval, Claude self-paces. | Skill. Alias `/proactive`. |
| `/mcp [reconnect (<server>\|all)\|enable\|disable [<server>\|all]]` | Manages MCP server connections and OAuth. | Built-in. |
| `/memory` | Edits CLAUDE.md files and turns auto memory on or off. | Built-in. |
| `/mobile` | Shows a QR code to download the Claude mobile app. | Built-in. Aliases `/ios`, `/android`. |
| `/model [model]` | Switches model and saves it as your default. In the picker, `s` switches for this session only and left/right arrows adjust effort. | Built-in. |
| `/output-style [style]` | Lists or switches output styles. | Built-in. |
| `/passes` | Shares a free week of Claude Code (eligible accounts only). | Built-in. |
| `/permissions` | Manages allow / ask / deny rules and reviews auto-mode denials. | Built-in. Alias `/allowed-tools`. |
| `/plan [description]` | Enters plan mode, optionally starting on a task. | Built-in. |
| `/plugin [subcommand]` | Opens the plugin menu, or runs `list`, `install`, `enable`, `disable` and so on. | Built-in. |
| `/plugin-authoring` | Loads the reference for writing a "mod". | Skill from a built-in plugin. |
| `/powerup` | Interactive lessons on Claude Code features. | Built-in. |
| `/pr-comments [PR]` | **Removed in v2.1.91.** | — |
| `/privacy-settings` | Views and updates privacy settings. | Built-in. Pro / Max / Ultra only. |
| `/radio` | Opens "Claude FM" lo-fi radio. | Built-in. |
| `/rate-limit-options` | Shows options when a usage limit blocks you: wait, add credits, or upgrade. | Built-in. Subscription only. |
| `/recap` | Generates a one-line summary of the session. | Built-in. |
| `/release-notes` | Views the changelog in a version picker. | Built-in. |
| `/reload-plugins [--force]` | Reloads plugins without restarting. | Built-in. |
| `/reload-skills` | Re-scans skill directories. | Built-in. |
| `/remote-control` | Makes this session controllable from claude.ai or the Claude app. | Built-in. Alias `/rc`. Subscription required. |
| `/remote-env` | Chooses the default cloud environment for cloud sessions. | Built-in. |
| `/rename [name]` | Renames the session; with no name, one is auto-generated. | Built-in. |
| `/restart` | Restarts Claude Code and resumes the session to apply an update. | Built-in. Pro / Max / Ultra, native install on macOS or Linux. Alias `/update`. |
| `/resume [session]` | Resumes a conversation by ID or name, or opens the picker. | Built-in. Alias `/continue`. |
| `/review [...]` | Alias of `/code-review`. | Skill alias. |
| `/rewind` | Rewinds conversation and/or code to a checkpoint, or summarizes from a point. | Built-in. Aliases `/checkpoint`, `/undo`. |
| `/run` | Launches and drives your app to see a change working. | Skill. |
| `/run-skill-generator` | Writes a per-project skill that teaches `/run` and `/verify` how to launch your app. | Skill. |
| `/sandbox` | Toggles sandbox mode. | Built-in. Supported platforms only. |
| `/schedule [description]` | Creates, updates, lists or runs cloud scheduled tasks. | Built-in per docs. Alias `/routines`. |
| `/scroll-speed` | Adjusts mouse-wheel scroll speed. | Built-in. Fullscreen only. |
| `/security-review` | Reviews your branch's diff against origin's default branch for security vulnerabilities. | Built-in per docs. Needs an `origin` remote. |
| `/setup-bedrock` | Wizard for Amazon Bedrock auth, region and models. | Built-in. Hidden until `CLAUDE_CODE_USE_BEDROCK=1`. |
| `/setup-vertex` | Wizard for Google Cloud's Agent Platform (Vertex). | Built-in. Hidden until `CLAUDE_CODE_USE_VERTEX=1`. |
| `/simplify [target]` | Reviews changed code for reuse, simplification and efficiency, then applies fixes. It does not hunt bugs. | Skill. |
| `/skill-doctor` | Shows each skill's context cost and usage. | Built-in. |
| `/skills` | Lists skills; `t` sorts by tokens, and Space/Enter cycles visibility. | Built-in. |
| `/slides [brief]` | Makes a Claude Slides artifact. | Skill. |
| `/stats` | Alias for `/usage`, opening on the Stats tab. | Built-in. |
| `/status` | Settings UI on the Status tab: version, model, account, connectivity. | Built-in. |
| `/statusline` | Configures the status line. | Built-in. |
| `/stickers` | Orders Claude Code stickers. | Built-in. |
| `/stop` | Stops the background session you're attached to. | Built-in. |
| `/subtask <task>` | Spawns a forked background subagent whose result comes back into this conversation. | Built-in. |
| `/tasks` | Views and manages background work (shells, subagents). | Built-in. Also `/bashes`. |
| `/team-onboarding` | Generates a team onboarding guide from your usage history. | Built-in. |
| `/teleport` | Pulls a cloud session into this terminal. | Built-in. Also `/tp`. Subscription required. |
| `/terminal-setup` | Installs a Shift+Enter newline binding (VS Code, Cursor, Alacritty, Zed and others) or configures Apple Terminal / iTerm2. | Built-in. |
| `/theme` | Changes the colour theme, including `auto`, daltonized, ANSI and custom themes. | Built-in. |
| `/tui [default\|fullscreen]` | Switches the terminal renderer. | Built-in. |
| `/ultraplan <prompt>` | **Removed.** Use plan mode. | — |
| `/ultrareview [PR or branch]` | Deep multi-agent cloud code review. The preferred form is `/code-review ultra`. | Built-in. 3 free runs on Pro / Max / Ultra, then usage credits. |
| `/update-config [request]` | Describe a settings change and Claude edits `settings.json`. | Skill. |
| `/upgrade` | Opens the plan-upgrade page. | Built-in. Not on Enterprise. |
| `/usage` | Shows session cost, plan limits and activity stats. | Built-in. Aliases `/cost`, `/stats`. |
| `/usage-credits` | Configures or requests usage credits. | Built-in. Formerly `/extra-usage`. |
| `/verify` | Builds, runs and observes your app to confirm a change works. | Skill. Runs only when you invoke it. |
| `/vim` | **Removed in v2.1.92.** Use `/config` → Editor mode. | — |
| `/voice [hold\|tap\|off]` | Toggles voice dictation. | Built-in. Claude.ai account required. |
| `/web-setup` | Connects GitHub for cloud sessions using local `gh` credentials. | Built-in. |
| `/workflow-authoring` | Loads the reference for writing dynamic workflow scripts. | Skill. |
| `/workflows` | Opens the workflow progress view. | Built-in. |

---

## 2. CLI: `claude` subcommands and flags

### 2a. Basic invocation patterns (cli-reference)

| Syntax | What it does |
|---|---|
| `claude` | Starts an interactive session. |
| `claude "query"` | Starts an interactive session with an initial prompt. |
| `claude -p "query"` | Runs non-interactively, prints the response, and exits. |
| `cat file \| claude -p "query"` | Processes piped content. |
| `claude -c` | Continues the most recent conversation in this directory. |
| `claude -c -p "query"` | Continues non-interactively. |
| `claude -r "<session>" "query"` | Resumes a session by ID or name. |

Mistyped subcommands get a suggestion: `claude udpate` prints `Did you mean claude update?` (cli-reference).

### 2b. Subcommands

| Subcommand and syntax | What it does | Source |
|---|---|---|
| `claude agents [options]` | Opens agent view to monitor and dispatch background sessions. `--json` prints sessions as JSON (`--json --all` includes completed ones), and `--cwd <path>` filters. Also accepts `--model`, `--effort`, `--permission-mode`, `--agent`, `--settings`, `--add-dir`, `--plugin-dir`, `--mcp-config`, `--restricted`, `--strict-mcp-config`, `--setting-sources`, `--allow-dangerously-skip-permissions`, `--dangerously-skip-permissions`. | cli-reference, agent-view, local --help |
| `claude attach <id\|name>` | Opens a background session in this terminal. `←` returns to agent view and `Ctrl+Z` returns to the shell. | cli-reference, local --help |
| `claude auth login [--claudeai\|--console] [--email <email>] [--sso]` | Signs in. `--claudeai` (subscription) is the default; `--console` uses Console API billing. | cli-reference, local --help |
| `claude auth logout` | Logs out. | cli-reference, local --help |
| `claude auth status [--json\|--text]` | Shows auth status, as JSON by default. Exit code 0 if logged in, 1 if not. | cli-reference, local --help |
| `claude auto-mode config` | Prints the effective auto-mode config as JSON. | local --help, auto-mode-config |
| `claude auto-mode defaults [--label <prefix>]` | Prints the built-in auto-mode classifier rules. | cli-reference, local --help |
| `claude auto-mode critique` | Gets AI feedback on your custom auto-mode rules. | local --help, auto-mode-config |
| `claude auto-mode reset [-y\|--yes]` | Removes the `autoMode` section from user settings. | cli-reference, local --help |
| `claude daemon status\|logs\|run\|stop [--any] [--keep-workers]\|uninstall` | Manages the background-session supervisor. | cli-reference, `claude daemon --help`. **Not listed** in top-level `claude --help`. |
| `claude doctor` | Read-only install and settings diagnostics without starting a session. | cli-reference, local --help |
| `claude gateway --config gateway.yaml` | Runs the self-hosted enterprise Claude apps gateway (admins). | cli-reference, local --help |
| `claude import [codex\|gemini\|cursor] [--dry-run] [--yes]` | Starts a session that imports config from another coding agent. | cli-reference, local --help |
| `claude install [--force] [stable\|latest\|<version>]` | Installs or reinstalls the native binary. | cli-reference, local --help |
| `claude logs <id\|name>` | Prints a background session's recent output. | cli-reference, local --help |
| `claude mcp add [options] <name> <commandOrUrl> [args...]` | Adds an MCP server. Options: `-t/--transport stdio\|sse\|http`, `-s/--scope local\|user\|project` (default `local`), `-e/--env KEY=value`, `-H/--header`, `--client-id`, `--client-secret`, `--callback-port`. | local --help |
| `claude mcp add-json <name> <json>` | Adds an MCP server from a JSON string. | local --help |
| `claude mcp add-from-claude-desktop` | Imports MCP servers from Claude Desktop (Mac and WSL only). | local --help |
| `claude mcp list` / `get <name>` / `remove <name>` | Lists, inspects or removes MCP servers. | local --help |
| `claude mcp login <name> [--no-browser]` / `logout <name>` | Runs or clears an MCP server's OAuth. | cli-reference, local --help |
| `claude mcp reset-project-choices` | Resets approvals of project `.mcp.json` servers. | local --help |
| `claude mcp serve` | Runs Claude Code itself as an MCP server. | local --help |
| `claude plugin` (alias `plugins`) `install\|i`, `uninstall\|remove`, `enable`, `disable`, `list`, `update`, `details`, `configure`, `validate`, `marketplace add\|list\|remove\|update`, `init\|new`, `prune\|autoremove`, `tag`, `eval`, `test` | Manages plugins and marketplaces. | local --help, https://code.claude.com/docs/en/plugins/cli-reference |
| `claude purge [path] [--all] [--dry-run] [-i] [-y]` | Deletes a project's local Claude Code data (transcripts, tasks, file history, `~/.claude.json` entry). | cli-reference, local --help |
| `claude remote-control [--name <n>] [--spawn same-dir\|worktree\|session] [--capacity N] [-c] [--session-id <id>] [--permission-mode <m>] [--[no-]chrome] ...` | Starts a Remote Control server (no local interactive session). | cli-reference, remote-control, `claude remote-control --help`. **Not listed** in top-level `claude --help`. |
| `claude respawn <id>` / `claude respawn --all` | Restarts background session(s) on the current binary. | cli-reference, local --help |
| `claude rm <id> [--discard-unpushed <commit>@<worktree-id>] [--force-remove-worktree <worktree-id>]` | Deletes a background session, and its worktree when that is safe. | cli-reference, local --help |
| `claude self-hosted-runner [setup\|doctor\|orchestrator]` | Registers a machine as a self-hosted cloud environment runner (admins). | cli-reference, local help. **Not listed** in top-level `claude --help`. |
| `claude setup-token` | Generates a one-year OAuth token for CI. It is printed, not saved, and requires a subscription. | cli-reference, authentication, local --help |
| `claude stop <id>` (alias `kill`) | Stops a background session; the conversation is kept. | cli-reference, local --help |
| `claude ultrareview [target] [--json] [--timeout <min>] [--post\|--no-post] [--trust-workspace]` | Runs a cloud multi-agent code review non-interactively. | cli-reference, local --help |
| `claude update` (alias `upgrade`) | Checks for and installs updates; package-manager installs update through the package manager. | cli-reference, local --help |

### 2c. Flags

The docs warn: "`claude --help` does not list every flag, so a flag's absence from `--help` does not mean it is unavailable" (cli-reference).

**In both the docs and local help** (one sentence each):

| Flag | What it does |
|---|---|
| `--add-dir <dirs...>` | Gives Claude file access to extra directories. |
| `--agent <agent>` | Runs the session as a named custom agent. |
| `--agents <json-or-file>` | Defines custom subagents inline as JSON. |
| `--allow-dangerously-skip-permissions` | Adds `bypassPermissions` to the Shift+Tab cycle without starting in it. |
| `--allowedTools`, `--allowed-tools <tools...>` | Tools or rules that run without prompting, for example `"Bash(git log *)" "Read"`. |
| `--append-system-prompt <text>` | Appends text to the default system prompt. |
| `--autocompact <auto\|tokens>` | Sets the auto-compact window for this session. |
| `--ax-screen-reader` | Screen-reader-friendly flat output. |
| `--bare` | Minimal mode: skips hooks, skills, plugins, MCP, CLAUDE.md and auto memory. Sets `CLAUDE_CODE_SIMPLE=1`. |
| `--betas <betas...>` | Beta API headers (API-key users only). |
| `--bg`, `--background` | Starts the session as a background agent and returns immediately. Can't be combined with `-p`. |
| `--chrome` / `--no-chrome` | Turns Claude in Chrome on or off for the session. |
| `--cloud [description\|session_id\|url]` | Creates a new cloud session, or with `-p` queues a message into an existing one. |
| `-c`, `--continue` | Continues the most recent conversation in this directory. |
| `--dangerously-skip-permissions` | Same as `--permission-mode bypassPermissions`. Use only in isolated containers or VMs. |
| `-d`, `--debug [filter]` | Debug mode, optionally filtered, for example `--debug='mcp,startup'`. The filter applies only in the `=` form. |
| `--debug-file <path>` | Writes debug logs to a file (and turns on debug mode). |
| `--desktop` | Opens the Desktop app on this directory (with `--continue` or `--resume <id>` for a session) and exits. |
| `--disable-slash-commands` | Disables all skills and commands. |
| `--disallowedTools`, `--disallowed-tools <tools...>` | Deny rules; a bare tool name removes that tool entirely. |
| `--effort <level>` | Session effort: `low`, `medium`, `high`, `xhigh`, `max`. The docs also accept `ultracode`, which local help doesn't list. |
| `--environment <id>` | Creates a cloud session on a self-hosted environment (`ccpool_...`). |
| `--exclude-dynamic-system-prompt-sections` | Moves per-machine context out of the system prompt (for cache reuse). |
| `--fallback-model <models>` | Comma-separated fallback models to use when the primary is overloaded or unavailable. |
| `--fork-session` | With `--resume` or `--continue`, creates a new session ID instead of reusing the original. |
| `--forward-subagent-text` | Emits subagent text in stream-json (needs `-p`). |
| `--from-pr [value]` | Opens the session picker filtered to sessions linked to a PR. |
| `-h`, `--help` | Shows help. |
| `--ide` | Auto-connects to the IDE if exactly one is available. |
| `--include-hook-events` | Includes hook events in stream-json. |
| `--include-partial-messages` | Streams partial messages (needs `-p` and stream-json). |
| `--input-format text\|stream-json` | Input format for `-p`. |
| `--json-schema <schema>` | Validates structured JSON output (`-p` only). |
| `--max-budget-usd <amount>` | Stops a `-p` run at an estimated spend. |
| `--mcp-config <configs...>` | Loads MCP servers from JSON files or strings. |
| `--model <model>` | Session model: an alias (`fable`, `opus`, `sonnet`, `haiku`, …) or a full name. |
| `-n`, `--name <name>` | Display name for the session, shown in the picker, prompt bar and terminal title. |
| `--no-session-persistence` | Doesn't save the session to disk (`-p` only). |
| `--output-format text\|json\|stream-json` | Output format for `-p`. |
| `--permission-mode <mode>` | Starting permission mode (see §4). |
| `--permission-prompts host\|none` | Who answers permission prompts in `-p`; with `none`, they are denied. |
| `--plugin-dir <path>` | Loads a plugin from a directory or `.zip` for this session (repeatable). |
| `--plugin-url <url>` | Fetches a plugin `.zip` from a URL for this session. |
| `-p`, `--print` | Non-interactive: prints the response and exits. Skips the workspace trust dialog. |
| `--prompt-suggestions` | Emits predicted next prompts (print/SDK). |
| `--remote-control [name]` | Starts an interactive session with Remote Control enabled. The docs also list the alias `--rc`. |
| `--remote-control-session-name-prefix <prefix>` | Prefix for auto-generated Remote Control names. |
| `--replay-user-messages` | Re-emits stdin user messages (stream-json). |
| `--restricted` | Removes command-running tools and WebFetch, ignores user/project/local settings, and refuses bypass. Intended for eval harnesses. |
| `-r`, `--resume [value]` | Resumes by ID, name or transcript path, or opens the picker. |
| `--safe-mode` | Starts with all customizations disabled, for troubleshooting. Sets `CLAUDE_CODE_SAFE_MODE=1`. |
| `--session-id <uuid>` | Uses a specific session UUID. |
| `--setting-sources <list>` | Which settings sources load: `user`, `project`, `local`. |
| `--settings <file-or-json>` | Extra settings file or JSON for this session. |
| `--strict-mcp-config` | Uses only the MCP servers from `--mcp-config`. |
| `--system-prompt <text>` | Replaces the whole system prompt. |
| `--system-prompt-snapshot on\|off` | Whether the first-request system prompt is recorded and reused. |
| `--teleport [session]` | Resumes a cloud session in the local terminal. |
| `--tmux` | Creates a tmux session for the worktree (needs `--worktree`). `--tmux=classic` for traditional tmux. |
| `--tools <tools...>` | Restricts the built-in tools: `""` for none, `"default"`, or names. |
| `--verbose` | Verbose, turn-by-turn output. |
| `-v`, `--version` | Prints the version (local prints `2.1.319 (Claude Code)`). |
| `-w`, `--worktree [name]` | Starts in a new git worktree at `<repo>/.claude/worktrees/<name>`. |

**In the docs but NOT in local `claude --help`.** These are documented, so likely still valid; the docs say `--help` omits some flags.
`--advisor <model>`, `--append-subagent-system-prompt`, `--append-subagent-system-prompt-file`, `--append-system-prompt-file`, `--system-prompt-file`, `--channels` (research preview), `--dangerously-load-development-channels`, `--exec` (with `--bg`, runs a shell command as a background job), `--init`, `--init-only`, `--maintenance` (Setup hooks), `--max-turns` (`-p` only), `--permission-prompt-tool`, `--ref <branch>` (with `--environment`), `--rc` (alias of `--remote-control`), `--teammate-mode in-process|auto|tmux|iterm2`, `--remote` (deprecated alias of `--cloud`), `--enable-auto-mode` (**removed** in v2.1.111). Source: cli-reference.

**In local `claude --help` but NOT in the docs (UNVERIFIED in docs):**
- `--brief`: "Enable SendUserMessage tool for agent-to-user communication" (local --help only).
- `--file <specs...>`: "File resources to download at startup. Format: file_id:relative_path" (local --help only).
- Local help's `--permission-mode` choices list `manual` instead of `default`. The docs confirm both work.

---

## 3. Keyboard shortcuts and input prefixes

Source: https://code.claude.com/docs/en/interactive-mode unless noted. On macOS, the `Alt+…` shortcuts need "Option as Meta" enabled in the terminal (terminal-config).

### 3a. Input prefixes / quick commands

| Prefix | What it does |
|---|---|
| `/` at start | Runs a command or skill. Typing `/` mid-prompt after a space offers completion, but runs nothing. |
| `!` at start | Shell mode: runs the command directly, adds its output to the conversation, and Claude responds to it, for example `! npm test`. Exit with Esc, Backspace or Ctrl+U on an empty prompt. |
| `@` | File-path mention with autocomplete (`@src/auth.ts`). |
| `:` | Emoji shortcode, for example `:name:`. |
| `?` on empty input | Toggles the shortcut help panel. |
| `#` | **No longer a shortcut.** "Removed # shortcut for quick memory entry (tell Claude to edit your CLAUDE.md instead)", v2.0.70 (changelog). Use `/memory` or ask Claude. |
| `ultrathink` in a prompt | Requests deeper reasoning for that turn, and can raise it to `xhigh` (shown in rainbow colours). Source: model-config. |

### 3b. General controls

| Shortcut | What it does |
|---|---|
| `Ctrl+C` | Interrupts a running operation. With nothing running, the first press clears input and a second press exits. |
| `Ctrl+D` | Exits (press twice within 800 ms). With text in the prompt, deletes the character after the cursor. |
| `Esc` | Interrupts Claude mid-turn (work so far is kept), closes a dialog, or declines a permission prompt. |
| `Esc` `Esc` | With text, clears the draft (Up recalls it). With an empty prompt, opens the **rewind** menu. |
| `Shift+Tab` (or `Alt+M` on some Windows setups) | Cycles permission modes (see §4). |
| `Ctrl+L` | Redraws the screen and keeps history. Note: it is a redraw, not a "clear conversation". |
| `Ctrl+O` | Toggles the transcript viewer (detailed tool use, and thinking shown as gray italics). |
| `Ctrl+R` | Reverse-searches prompt history. |
| `Ctrl+V` (also `Cmd+V` in iTerm2, `Alt+V` on Windows/WSL) | Pastes an image from the clipboard as an `[Image #N]` chip. |
| `Ctrl+B` | Sends a running Bash command or agent to the background (tmux users press it twice). |
| `Ctrl+T` | Shows or hides Claude's task checklist. |
| `Ctrl+S` | Stashes the current prompt, or restores it. |
| `Ctrl+G` or `Ctrl+X Ctrl+E` | Edits the prompt in your external editor. |
| `Ctrl+Z` | Suspends Claude Code (Unix); `fg` resumes it. |
| `Ctrl+X Ctrl+K` | Stops all background subagents (press twice within 3 s). |
| `Ctrl+Enter` or `Ctrl+X Ctrl+S` | Sends queued messages now. |
| `Up/Down` or `Ctrl+P/Ctrl+N` | Moves within multi-line input, then through history. |
| `Tab` | Accepts an autocomplete suggestion, or adds a comment to a permission answer. |
| `Left/Right` | Cycles dialog tabs. On an empty prompt, `←` opens agent view (agent-view). |
| `Option+P` / `Alt+P` | Switches model without clearing the prompt. |
| `Option+T` / `Alt+T` | Toggles extended thinking. No effect on Opus 5.5, Sonnet 5.5, Haiku 5.5 or Fable. |
| `Option+O` / `Alt+O` | Toggles fast mode. |
| Hold/tap `Space` | Voice dictation, when enabled with `/voice`. |

### 3c. Text editing

`Ctrl+A` / `Ctrl+E` (start/end of line), `Ctrl+K` (delete to end of line), `Ctrl+U` (delete to start of line), `Ctrl+W` (delete back to whitespace), `Ctrl+Y` (paste deleted text), `Alt+Y` (cycle paste history), `Alt+B` / `Alt+F` (word back/forward), `Alt+D` (delete word), `Ctrl+_` or `Ctrl+Shift+-` (undo the last input edit). Source: interactive-mode.

### 3d. Multiline input

| Method | Shortcut |
|---|---|
| Quick escape | `\` then `Enter` (works in all terminals) |
| Control sequence | `Ctrl+J` (any terminal, no configuration) |
| Shift+Enter | Native in iTerm2, WezTerm, Ghostty, Kitty, Warp, Apple Terminal and Windows Terminal. Others: run `/terminal-setup`. |
| Option+Enter | macOS, after enabling Option as Meta |
| Paste | Paste multi-line text directly |

Source: interactive-mode, terminal-config.

### 3e. Vim mode

Turn it on with **`/config` → Editor mode** (the `/vim` command was removed in v2.1.92). Supports NORMAL/INSERT/VISUAL modes: `Esc`/`Ctrl+[` → NORMAL; `i I a A o O` enter insert; `v`/`V` start visual selection; plus navigation, editing and text objects. Source: interactive-mode.

### 3f. Other notes

- Command history is stored per working directory. Up-arrow recall reaches earlier sessions of the same project (interactive-mode).
- Messages typed while Claude is working are queued and sent at the next safe point (interactive-mode).
- Custom keybindings live in `~/.claude/keybindings.json` and are opened with `/keybindings` (https://code.claude.com/docs/en/keybindings).

---

## 4. Permission modes

Source: https://code.claude.com/docs/en/permission-modes, local --help.

| Mode (config value) | UI label | What runs without asking | Best for |
|---|---|---|---|
| `default` (CLI alias `manual`) | Manual | Reads only | Reviewing every action, sensitive work |
| `acceptEdits` | Accept edits / "Edit automatically" in VS Code | Reads, file edits, common filesystem commands (`mkdir`, `touch`, `mv`, `cp`, …) | Iterating on code you're reviewing |
| `plan` | Plan | Reads (plus classifier-approved commands when auto is available). Edits blocked until you approve a plan. | Exploring before changing |
| `auto` | Auto | Everything, with a background classifier reviewing actions | Long tasks, fewer prompts |
| `dontAsk` | Don't ask | Reads in the working directories and pre-approved tools. Anything that would prompt is **denied**. | Locked-down CI/scripts |
| `bypassPermissions` | Bypass permissions | Everything (no checks) | Isolated containers/VMs only |

Key facts:

- **Starting mode:** the `--permission-mode` flag, then `permissions.defaultMode` in settings, then the built-in default. The built-in default is **`auto`** for interactive terminal and VS Code sessions from v2.1.283, and `default` for `claude -p` / the SDK. If auto isn't available (unsupported model, org turned it off), the session starts in Manual.
- **Shift+Tab cycle:** `default` → `acceptEdits` → `plan`, and then optional modes: `bypassPermissions` first, `auto` last. From `auto`, the first press goes to `default`.
  - `auto` is in the cycle when auto mode is available.
  - `bypassPermissions` appears only if you started with `--permission-mode bypassPermissions`, `--dangerously-skip-permissions`, `--allow-dangerously-skip-permissions`, or `defaultMode: "bypassPermissions"` in user, `--settings` or managed settings.
  - `dontAsk` **never** appears in the cycle; set it with `--permission-mode dontAsk`.
- Status bar text: `⏸ manual mode on`, `⏵⏵ accept edits on`, `⏸ plan mode on`, `⏵⏵ auto mode on`, `⏵⏵ don't ask on`, `⏵⏵ bypass permissions on`.
- Deny rules block in every mode, including bypass. Explicit `ask` rules, `rm` of critical paths and similar still prompt in every mode.
- Bash permission prompts in Manual/acceptEdits can offer **"Yes, and switch to auto mode"**.
- Other surfaces: the VS Code mode indicator, the Desktop mode selector, and the claude.ai/code dropdown. Cloud sessions offer Accept edits, Plan and Auto only.
- `/permissions` manages allow/ask/deny rules; `/plan` enters plan mode.

---

## 5. Installation, updates, and authentication

### 5a. System requirements (https://code.claude.com/docs/en/setup)

- OS: macOS 13.0+; Windows 10 1809+ or Windows Server 2019+; Ubuntu 20.04+; Debian 10+; Alpine Linux 3.19+.
- Hardware: 4 GB+ RAM, x64 or ARM64.
- Network: an internet connection. Location: an Anthropic-supported country.
- Shell: Bash, Zsh, PowerShell or CMD.
- ripgrep is usually bundled. Git is optional. On native Windows, Git for Windows is recommended so the Bash tool can be used; without it, Claude Code uses PowerShell.
- Accounts: Pro, Max, Ultra, Team, Enterprise or Console. **The free claude.ai plan does not include Claude Code.**

### 5b. Install commands (setup)

| Method | Command |
|---|---|
| Native (recommended), macOS/Linux/WSL | `curl -fsSL https://claude.ai/install.sh \| bash` |
| Native, Windows PowerShell | `irm https://claude.ai/install.ps1 \| iex` |
| Native, Windows CMD | `curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd` |
| Homebrew | `brew install --cask claude-code` (stable channel) or `brew install --cask claude-code@latest` |
| WinGet | `winget install Anthropic.ClaudeCode` |
| npm | `npm install -g @anthropic-ai/claude-code` (requires Node.js 22+; **do not use sudo**) |
| Linux packages | Signed apt, dnf and apk repositories, with `stable` and `latest` channels (see the setup page for exact repository commands; not reproduced here) |

- A specific version or channel with the native installer: `curl -fsSL https://claude.ai/install.sh | bash -s stable` or `... | bash -s 2.1.89`. In PowerShell: `& ([scriptblock]::Create((irm https://claude.ai/install.ps1))) stable`.
- Verify: `claude --version`, then `claude doctor`.
- Common Windows mistakes: `irm is not recognized` means you're in CMD, not PowerShell. `The token '&&' is not a valid statement separator` means you're in PowerShell, not CMD.
- The native install puts the launcher at `~/.local/bin/claude`, with versions in `~/.local/share/claude/versions/`.
- Uninstall (native, macOS/Linux): `rm -f ~/.local/bin/claude` and `rm -rf ~/.local/share/claude`.

### 5c. Updates and channels (setup)

- Native installs **auto-update** in the background. Homebrew, WinGet, apt, dnf and apk installs **don't**. Upgrade them with `brew upgrade claude-code` (or `claude-code@latest`), `winget upgrade Anthropic.ClaudeCode`, and so on. `CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE=1` makes Claude Code run the Homebrew/WinGet upgrade for you.
- npm upgrade: `npm install -g @anthropic-ai/claude-code@latest` (avoid `npm update -g`).
- Manual update: `claude update` (alias `claude upgrade`).
- Channel: the setting `"autoUpdatesChannel": "latest"` (default) or `"stable"` (about a week old, skips releases with major regressions). Set it with `/config` → Auto-update channel. `minimumVersion` sets a floor.
- Disable: `DISABLE_AUTOUPDATER=1` stops background updates only. `DISABLE_UPDATES=1` blocks all updates.

### 5d. Authentication (https://code.claude.com/docs/en/authentication)

| Option | How |
|---|---|
| Claude subscription (Pro/Max/Ultra, Team/Enterprise) | Run `claude` and follow the browser login, or use `/login` or `claude auth login`. Press `c` to copy the URL if the browser doesn't open. |
| Claude Console (API billing) | `claude auth login --console`, or choose Console at the login prompt. An admin must invite you. You can sign in with or without creating an API key. |
| API key | Set `ANTHROPIC_API_KEY`. In interactive mode you approve it once; with `-p` it is always used. |
| Bearer token / gateway | `ANTHROPIC_AUTH_TOKEN` (sent as `Authorization: Bearer`). |
| Amazon Bedrock | `CLAUDE_CODE_USE_BEDROCK=1` plus AWS credentials; `/setup-bedrock` wizard. |
| Google Cloud's Agent Platform (Vertex AI) | `CLAUDE_CODE_USE_VERTEX=1` plus GCP credentials; `/setup-vertex` wizard. |
| Microsoft Foundry | `CLAUDE_CODE_USE_FOUNDRY=1` plus Azure credentials. |
| Long-lived token (CI) | `claude setup-token` prints a **one-year** OAuth token; set it as `CLAUDE_CODE_OAUTH_TOKEN`. Needs a subscription. Can't establish Remote Control or fetch claude.ai connectors. Not read in `--bare` mode. |
| Credential helper | `apiKeyHelper` setting (a script that prints a key). |
| Enterprise gateway | Claude apps gateway; corporate SSO through `/login`. |

- **Precedence:** cloud provider env vars, then `ANTHROPIC_AUTH_TOKEN`, then `ANTHROPIC_API_KEY`, then `apiKeyHelper`, then `CLAUDE_CODE_OAUTH_TOKEN`, then Anthropic profile/federation credentials, then `/login` subscription OAuth.
- Credential storage: the macOS Keychain; on Linux `~/.claude/.credentials.json` (mode 0600); on Windows `%USERPROFILE%\.claude\.credentials.json`.
- Multiple accounts: `alias claude-work='CLAUDE_CONFIG_DIR=~/.claude-work claude'`.
- `claude auth` subcommands: `login [--claudeai|--console] [--email <email>] [--sso]`, `logout`, `status [--json|--text]` (local --help, cli-reference).
- `/status` shows which credential is active.

---

## 6. Model configuration (https://code.claude.com/docs/en/model-config)

### 6a. Aliases

| Alias | Meaning |
|---|---|
| `default` | Clears any override and uses the account default (Opus 5.5 on Pro/Max/Ultra/Team/Enterprise/API; Sonnet 4.5 on Foundry). |
| `best` | The model `fable` resolves to where Fable is available, otherwise the same as `opus`. |
| `fable` | The Fable model for your provider (Fable 5.1 unless overridden). For the hardest, longest tasks. |
| `opus` | The latest Opus (Opus 5.5 on the Anthropic API). |
| `sonnet` | The latest Sonnet (Sonnet 5.5 on the Anthropic API). |
| `haiku` | Fast Haiku (Haiku 5.5 on the Anthropic API). |
| `sonnet[1m]`, `opus[1m]` | 1M-token context variants (no effect where the model already has a native 1M window). |
| `opusplan` | `opus` in plan mode, `sonnet` for execution. |

On Bedrock, Agent Platform and Foundry the aliases can resolve to older models, for example `sonnet` resolving to Sonnet 4.5. Pin a version with a full name such as `claude-opus-5-5`, or with `ANTHROPIC_DEFAULT_OPUS_MODEL`, `ANTHROPIC_DEFAULT_SONNET_MODEL`, `ANTHROPIC_DEFAULT_HAIKU_MODEL` or `ANTHROPIC_DEFAULT_FABLE_MODEL`.

### 6b. Setting the model (priority order)

1. `/model <alias|name>` during the session. With no argument it opens a picker: `Enter` saves the choice as your default, `s` applies it to this session only, and left/right adjusts effort.
2. `claude --model <alias|name>`.
3. `ANTHROPIC_MODEL`.
4. The `"model"` key in settings.
5. `ANTHROPIC_DEFAULT_MODEL` (the default for new sessions).

`/model` **saves** your choice as the default for new sessions (it writes `model` to user settings). Resumed sessions keep their saved model. `Option+P` / `Alt+P` switches model mid-prompt. Check the current model with `/status`.

### 6c. Effort levels

- Levels: `low`, `medium`, `high`, `xhigh`, `max`. Opus 4.6 and Sonnet 4.6 lack `xhigh`; an unsupported level falls back to the highest supported one below it.
- Defaults: **`medium`** on Opus 5.5, Sonnet 5.5 and Haiku 5.5; `xhigh` on Opus 4.7; `high` elsewhere.
- Ways to set it: `/effort [level|auto|status]` (a slider with no argument; `auto` clears your saved level), the left/right arrows in `/model`, `claude --effort <level>`, `CLAUDE_CODE_EFFORT_LEVEL` (the highest priority), and the `modelSettings` / `effortLevel` settings.
- `max` applies to the current session only (unless set through the env var). Settings files don't accept `max`.
- `ultracode` is not an effort level: it is a setting that makes Claude orchestrate dynamic workflows. `--effort ultracode` sets `xhigh` and turns ultracode on.
- `ultrathink` in a prompt gives deeper reasoning for one turn.

### 6d. Fallback model

- `claude --fallback-model sonnet,haiku` gives a comma-separated chain, tried in order when the primary is overloaded or unavailable. The switch lasts for the current turn only, and the chain is capped at 3 models.
- To persist a chain: `"fallbackModel": ["claude-sonnet-5", "claude-haiku-4-5"]` in settings. The flag overrides the setting.
- This is separate from **automatic content-based fallback**: Fable, Opus 5.5 and Sonnet 5.5 can re-run safety-flagged cyber or bio requests on an older model.

### 6e. Extended thinking

- Toggle: `Option+T` / `Alt+T`. Global default: `/config` (saved as `alwaysThinkingEnabled`). `MAX_THINKING_TOKENS=0` disables it on the API.
- Thinking **cannot** be turned off on Opus 5.5, Sonnet 5.5, Haiku 5.5 or Fable.
- `Ctrl+O` shows collapsed thinking.

---

## 7. Sessions, checkpoints, background agents, and other surfaces

### 7a. Checkpointing / rewind (https://code.claude.com/docs/en/checkpointing)

- Every prompt that starts a turn creates a checkpoint of Claude's file edits. Snapshots are kept for the 100 most recent checkpoints and survive a resume. They are cleaned up after about 30 days (`cleanupPeriodDays`).
- Open with `/rewind` (aliases `/checkpoint`, `/undo`) or `Esc Esc` on an empty prompt.
- Actions: **Restore code and conversation**, **Restore conversation**, **Restore code**, **Summarize from here**, **Summarize up to here**, **Never mind**.
- Limits:
  - Files changed only by Bash commands aren't tracked.
  - Most subagent edits aren't restored.
  - External edits aren't tracked.
  - Symlinks and hard links are skipped.
  - Checkpoints are not a replacement for git.

### 7b. Continue / resume / fork / name (https://code.claude.com/docs/en/sessions)

| Syntax | What it does |
|---|---|
| `claude --continue` / `-c` | Reopens the most recent session in this directory. |
| `claude --resume` / `-r` | Opens the session picker. |
| `claude --resume <name\|id\|transcript-path>` | Resumes a specific session. |
| `claude --from-pr <number\|url>` | Opens the picker filtered to sessions linked to a PR. |
| `claude --continue --fork-session` | Resumes into a **new** session ID, leaving the original intact. |
| `/resume [session]` | Switches session from inside Claude Code. |
| `/branch [name]` | Branches the current conversation and switches into the branch. |
| `/fork [prompt]` | Copies the conversation into a new **background** session. |
| `claude -n <name>` / `/rename <name>` | Names a session. In the picker, `Ctrl+R` renames. |

- Picker keys: `↑/↓` or `j/k` navigate, `Enter` resumes, `Space` previews, `Ctrl+A` shows all projects, `Ctrl+W` shows all worktrees, `Ctrl+B` filters to the current branch, `/` searches.
- Transcripts are stored at `~/.claude/projects/<project>/<session-id>.jsonl`, with 30-day retention by default.

### 7c. Background sessions / agent view (https://code.claude.com/docs/en/agent-view), research preview

| Syntax | What it does |
|---|---|
| `claude --bg "task"` | Starts a background session and prints its short ID. |
| `claude --bg --exec 'pytest -x'` | Runs a shell command as a background job. |
| `claude agents` | Opens agent view: dispatch tasks, peek with `Space`, attach with `Enter`/`→`, detach with `←`. Press `?` for shortcuts. |
| `claude attach <id\|name>` / `claude logs <id\|name>` / `claude stop <id>` / `claude rm <id>` / `claude respawn <id>\|--all` | Manage sessions from the shell. |
| `/background` (alias `/bg`), or `←` on an empty prompt | Sends the current session to the background. |
| `/stop` | Stops the attached background session. |

- Detaching (`←`, `Ctrl+Z`, `/exit`) never stops the session.
- Background sessions run locally, consume quota the same as interactive sessions, and stop if the machine shuts down.
- State lives under `~/.claude/jobs/`.

Do not confuse these with **background Bash tasks**: `Ctrl+B` backgrounds a running command, and `/tasks` lists those tasks (interactive-mode).

### 7d. Worktrees (https://code.claude.com/docs/en/worktrees)

- `claude --worktree feature-auth` (or `-w`) creates `.claude/worktrees/feature-auth/` on branch `worktree-feature-auth`. Without a name, a generated one is used.
- `-w '#123'` or a PR/MR URL branches from that pull request.
- On exit, a clean unnamed worktree is removed automatically; otherwise you are asked whether to keep or remove it. Resume a kept one with `claude --worktree <name> --resume`.
- `--tmux` opens the worktree session in tmux (or iTerm2 panes).
- Tip from the docs: add `.claude/worktrees/` to `.gitignore`.

### 7e. IDE integrations

**VS Code** (https://code.claude.com/docs/en/vs-code):

- Install: the `anthropic.claude-code` extension (also for Cursor, and on Open VSX). Requires VS Code 1.94.0+.
- The extension bundles its own CLI. To run `claude` in the integrated terminal you need the standalone install.
- Shortcuts:
  - `Cmd+Esc` / `Ctrl+Esc`: focus toggle.
  - `Cmd+Shift+Esc` / `Ctrl+Shift+Esc`: new tab.
  - `Option+K` / `Alt+K`: insert an @-mention, for example `@file.ts#5-10`.
  - `Cmd+Shift+T` / `Ctrl+Shift+T`: reopen a closed session.
  - `Ctrl+Option+F` / `Ctrl+Alt+F`: focus view.
  - `Cmd+N` / `Ctrl+N`: new conversation (needs `enableNewConversationShortcut`).
- Gotcha: macOS Tahoe's Game Overlay can intercept `Cmd+Esc`.

**JetBrains** (https://code.claude.com/docs/en/jetbrains):

- Supports IntelliJ IDEA, PyCharm, Android Studio, WebStorm, PhpStorm and GoLand.
- Install the "Claude Code" plugin from the JetBrains Marketplace **and** the CLI; the plugin doesn't bundle the CLI.
- Shortcuts: `Cmd+Esc` / `Ctrl+Esc` quick-launch; `Cmd+Option+K` / `Alt+Ctrl+K` inserts a file reference.
- Diffs appear in the IDE diff viewer.
- From an external terminal, run `/ide` to connect. `claude --ide` auto-connects.

### 7f. Desktop app (https://code.claude.com/docs/en/desktop)

- Claude Code is the **Code** tab in the Claude Desktop app.
- Downloads: macOS (universal), Windows (x64, plus an ARM64 installer), and Linux (beta, via apt).
- Move a CLI session into Desktop with `/desktop` (alias `/app`), or from the shell with `claude --desktop [--continue | --resume <session-id>]`. Requires macOS or x64 Windows plus a subscription.
- In Desktop, `/resume` picks up sessions started in the CLI.

### 7g. Claude Code on the web / cloud sessions (https://code.claude.com/docs/en/claude-code-on-the-web)

- Runs on Anthropic-managed cloud infrastructure, from claude.ai/code, the mobile app's Code tab, Desktop, or the terminal.
- Plans: Pro, Max, Ultra, Team, and Enterprise premium seats.
- `claude --cloud "task"` starts a cloud session. It clones your GitHub remote at the current branch, so **push first**.
- `claude --teleport` or `/teleport` (`/tp`) pulls a cloud session into the terminal. From the CLI the handoff is one-way: you can't push a running local session to the cloud.
- Related commands: `/web-setup` (connect GitHub), `/remote-env` (choose an environment), `/autofix-pr`.

### 7h. Remote Control (https://code.claude.com/docs/en/remote-control)

- Lets you continue a **local** session from claude.ai/code or the Claude iOS/Android app; execution stays on your machine.
- Three ways to start it:
  - `claude remote-control` (server mode, `--name`, `--spawn same-dir|worktree|session`, `--capacity`, and so on).
  - `claude --remote-control [name]` / `--rc` (an interactive session).
  - `/remote-control` (`/rc`) from inside a session.
- Requirements:
  - A Pro, Max, Ultra, Team or Enterprise subscription. API keys are not supported. On Team/Enterprise, an Owner must enable it.
  - Not available on Bedrock, Agent Platform or Foundry, with a non-Anthropic `ANTHROPIC_BASE_URL`, or with `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` set.
- Don't confuse it with `--cloud`, which runs the session in the cloud.

### 7i. Chrome integration (https://code.claude.com/docs/en/chrome)

- Requires Chrome, Edge or another Chromium browser; the "Claude in Chrome" extension v1.0.36+; a direct Anthropic plan; and a `/login` sign-in. API keys and `setup-token` tokens keep Chrome integration off. Not available on Bedrock, Agent Platform or Foundry.
- Start with `claude --chrome`. `/chrome` shows status, permissions and reconnect; `--no-chrome` disables it. `/claude-in-chrome [task]` is the skill.
- Claude shares your browser's logged-in state and pauses for logins and CAPTCHAs.

---

## 8. Useful environment variables for ordinary users

Source: https://code.claude.com/docs/en/env-vars (plus model-config and setup). Set them in the shell, or in the `"env"` block of `settings.json`.

| Variable | What it does |
|---|---|
| `ANTHROPIC_API_KEY` | API key (`X-Api-Key`). Overrides your subscription once approved, and is always used with `-p`. `unset ANTHROPIC_API_KEY` returns to the subscription. |
| `ANTHROPIC_AUTH_TOKEN` | Custom `Authorization: Bearer` value (for gateways). |
| `ANTHROPIC_BASE_URL` | Sends requests to a proxy or gateway. Disables Remote Control if it isn't api.anthropic.com. |
| `ANTHROPIC_MODEL` | Model for the session (alias or full name). |
| `ANTHROPIC_DEFAULT_MODEL` | The model new sessions start on. |
| `ANTHROPIC_DEFAULT_OPUS_MODEL` / `_SONNET_MODEL` / `_HAIKU_MODEL` / `_FABLE_MODEL` | Pin what each alias resolves to. |
| `CLAUDE_CODE_SUBAGENT_MODEL` | Default model for subagents. |
| `CLAUDE_CODE_EFFORT_LEVEL` | Effort level (`low`…`max`, or `auto`/`unset`). Highest priority. |
| `MAX_THINKING_TOKENS` | Fixed thinking budget; `0` turns thinking off where allowed. |
| `CLAUDE_CODE_MAX_OUTPUT_TOKENS` | Max output tokens. |
| `CLAUDE_CONFIG_DIR` | Moves `~/.claude` elsewhere; useful for multiple accounts. |
| `CLAUDE_CODE_OAUTH_TOKEN` | Token from `claude setup-token`, for CI. |
| `CLAUDE_CODE_USE_BEDROCK` / `CLAUDE_CODE_USE_VERTEX` / `CLAUDE_CODE_USE_FOUNDRY` | Use Bedrock / Google Cloud's Agent Platform / Microsoft Foundry. |
| `DISABLE_AUTOUPDATER` | `1` stops background auto-updates (`claude update` still works). |
| `DISABLE_UPDATES` | `1` blocks all updates. |
| `CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE` | `1` makes Claude Code run the Homebrew/WinGet upgrade for you. |
| `DISABLE_TELEMETRY` | Opts out of telemetry. Note that even `0`/`false` opts out; unset it to opt back in. |
| `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` | Disables auto-updates, telemetry, error reporting, `/feedback`, release notes and more. Also disables Remote Control. |
| `HTTPS_PROXY` / `HTTP_PROXY` | Proxy server. |
| `BASH_DEFAULT_TIMEOUT_MS` | Foreground Bash/PowerShell timeout (default 120000 ms). |
| `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS` | `1` turns off background tasks and `Ctrl+B`. |
| `CLAUDE_CODE_DISABLE_AUTO_MEMORY` | `1` disables auto memory. |
| `CLAUDE_CODE_AUTO_COMPACT_WINDOW` | Auto-compact threshold (100000–1000000 tokens). |
| `CLAUDE_CODE_NEW_INIT` | `1` gives an interactive `/init` flow. |
| `CLAUDE_CODE_GIT_BASH_PATH` | Windows: path to Git Bash's `bash.exe`. |
| `CLAUDE_CODE_SAFE_MODE` | `1` is the same as `--safe-mode`. |
| `CLAUDE_CODE_SIMPLE` | `1` is the same as `--bare`. |
| `CLAUDE_AX_SCREEN_READER` | `1` gives screen-reader output. |
| `MCP_TIMEOUT` | MCP server startup timeout in ms (default 30000). |
| `USE_BUILTIN_RIPGREP` | `0` uses the system ripgrep (Alpine/musl, search problems). Source: setup, troubleshooting. |

---

## 9. Troubleshooting highlights

Sources: https://code.claude.com/docs/en/troubleshooting, https://code.claude.com/docs/en/troubleshoot-install, https://code.claude.com/docs/en/errors.

**First steps**

- Inside a session, run `/doctor` (a checkup that can apply fixes).
- If `claude` won't start, run `claude doctor` from the shell (read-only).
- `/mcp` shows MCP status. `/status` shows the active account and credentials.
- `claude --safe-mode` tests with all customizations off.
- `/debug` or `claude --debug` turns on logging.

**Installation**

| Symptom | Fix |
|---|---|
| `command not found: claude` / `'claude' is not recognized` | The install directory isn't on PATH. Open a new terminal and fix PATH (`~/.local/bin` on macOS/Linux). |
| `syntax error near unexpected token '<'`, `curl: (22) ... 403` | The install script returned HTML (network, proxy or region). See troubleshoot-install. |
| `irm is not recognized` / `The token '&&' is not a valid statement separator` | Wrong shell: use the PowerShell or CMD command that matches your shell. |
| `EACCES: permission denied` (npm) | Fix permissions; don't use `sudo npm install -g`. |
| `Killed` during install on Linux | Low memory: add swap or free memory. |
| `Auto-update failed · Run claude doctor` | Run `claude update` from the shell. |
| `App unavailable in region` | Claude Code isn't available in your country. |
| `unable to get local issuer certificate`, TLS errors | Corporate CA or proxy: configure certificates (network-config). |
| Search or `@file` not finding files | The bundled ripgrep fails: install the system `ripgrep` and set `USE_BUILTIN_RIPGREP=0`. |

**Login**

| Symptom | Fix |
|---|---|
| Login loops or unclear failures | Run `/logout`, close Claude Code, run `claude` and log in again. Press `c` to copy the OAuth URL. |
| `OAuth error: Invalid code` | The code expired or was truncated; retry quickly. Over SSH, open the URL in your local browser. |
| `API Error: 403 Request not allowed` | Check the subscription is active (Pro/Max/Ultra), or that your Console account has the "Claude Code" or "Developer" role, or your proxy settings. |
| `This organization has been disabled` despite an active subscription | A stale `ANTHROPIC_API_KEY` is overriding it: `unset ANTHROPIC_API_KEY` and remove it from your shell profile. |
| `Login expired · Please run /login` | Run `/login`. You are warned 3 days before expiry. |

**Running**

| Symptom | Fix |
|---|---|
| High CPU or memory | Use `/compact`, restart between tasks, `claude --continue` to resume in a fresh process, `--safe-mode` to isolate plugins, and `/heapdump` for diagnostics. |
| `Autocompact is thrashing` | Read large files in chunks, run a focused `/compact`, use a subagent, or `/clear`. |
| Hangs | `Ctrl+C`. If that fails, restart and run `claude --resume` (nothing is lost). |
| Garbled text in a VS Code/Cursor terminal | Run `/terminal-setup` (turns GPU acceleration off). |
| Display corrupted | `Ctrl+L` redraws the screen. |
| Unexpectedly running in auto mode | It's the default since v2.1.283. Set `permissions.defaultMode` or use `--permission-mode default`. |
| API errors `5xx`, `529 Overloaded`, `429` | See https://code.claude.com/docs/en/errors. |

---

## UNVERIFIED / open items

1. `--brief` and `--file <specs...>` appear only in local `claude --help`; they are not in the docs CLI reference.
2. Whether `/init`, `/security-review` and `/schedule` are "built-in commands" (per the docs commands table) or "bundled skills" (per the local session's skill registry). The docs don't mark them as skills.
3. Exact apt, dnf and apk repository setup commands were not transcribed. See https://code.claude.com/docs/en/setup#install-with-linux-package-managers.
4. `claude plugin` subcommand flags beyond the names listed in local `--help` were not individually verified.
5. `claude daemon`, `claude remote-control` and `claude self-hosted-runner` work (their `--help` runs) and are documented, but are absent from the top-level `claude --help` command list.
