# Claude Code: Configuration and Extensibility Reference

**Verified on 2026-11-09 against docs and Claude Code 2.1.319**

Method: each official page was downloaded as raw Markdown from `https://code.claude.com/docs/en/<page>.md` (page list from https://code.claude.com/docs/llms.txt) and read directly; CLI facts were cross-checked with `claude --version`, `claude mcp --help`, `claude mcp add --help`, `claude plugin --help` and `local-cli-help.md`. Anything not confirmed is marked **UNVERIFIED**.

Notation: `~` = your home directory; a bare `.claude/` = the `.claude` folder inside your project. On Windows `~/.claude` means `%USERPROFILE%\.claude`.

---

## 1. Settings

Source: https://code.claude.com/docs/en/settings , https://code.claude.com/docs/en/settings-reference , https://code.claude.com/docs/en/managed-settings

### 1.1 Settings files

| Scope | File | Who it affects |
|---|---|---|
| User | `~/.claude/settings.json` | You, in every project on this machine |
| Shared project | `.claude/settings.json` | Everyone in the project (commit it) |
| Project local | `.claude/settings.local.json` | You, in this project only (kept out of git) |
| Managed | `managed-settings.json` (plus MDM / server-managed sources) | Everyone the organization deploys it to |

- Managed file locations: macOS `/Library/Application Support/ClaudeCode/managed-settings.json`; Linux and WSL `/etc/claude-code/managed-settings.json`; Windows `C:\Program Files\ClaudeCode\managed-settings.json`. An optional `managed-settings.d/` drop-in directory sits next to it. The legacy `C:\ProgramData\ClaudeCode\managed-settings.json` is **not** read. (managed-settings)
- Managed settings can also arrive as server-managed settings from the claude.ai admin console, or via MDM/OS policies. (settings)
- Installing Claude Code creates no settings file. Claude Code writes `~/.claude/settings.json` the first time you change certain `/config` options, and `.claude/settings.local.json` the first time you choose "Yes, and don't ask again" on a permission prompt. (settings)
- When Claude Code first writes `.claude/settings.local.json` in a git repo it adds `**/.claude/settings.local.json` to your **global** git excludes file. If you create the file by hand, add it to `.gitignore` yourself. (settings)
- In a git repo, the local file is read/written at the **repository root** (since v2.1.211). (settings)
- Separate file `~/.claude.json` is written by Claude Code itself: account details, MCP server configs (local/user scope), per-project state such as trust decisions, global config keys. You don't need to edit it. (settings)
- `CLAUDE_CONFIG_DIR` env var relocates the home-directory files. (settings)
- Settings files are strict JSON (no comments, no trailing commas). Add `"$schema": "https://json.schemastore.org/claude-code-settings.json"` for editor autocomplete. (settings)

### 1.2 Precedence (highest first)

1. **Managed settings** (cannot be overridden by anything, including `--settings`)
2. **Command line**: `--settings <file-or-json>` for that one session
3. **Project local**: `.claude/settings.local.json`
4. **Shared project**: `.claude/settings.json`
5. **User**: `~/.claude/settings.json`

Notes (settings):
- Environment variables are **not** a level in this stack; each env-var/key pair has its own rule (e.g. exported `ANTHROPIC_MODEL` beats the `model` key; `--model` beats both).
- List keys such as `permissions.allow` **merge** across files rather than override.
- A few security-sensitive keys honor a stricter lower-level value over a managed one ("Exceptions to managed settings precedence").
- Most edits are hot-reloaded (including `permissions` and `hooks`); `model` and `effortLevel` are read only at session start.
- Check what loaded: `/status` (shows a `Setting sources` line); find rejected entries with `claude doctor`.
- Local CLI also has `--setting-sources <sources>`: "Comma-separated list of setting sources to load (user, project, local)." (local-cli-help.md)

Minimal example (for one session only):
```bash
claude --settings '{"model": "claude-opus-5-5"}'
```

### 1.3 Most useful keys

All from https://code.claude.com/docs/en/settings-reference unless noted.

| Key | Meaning | Example |
|---|---|---|
| `model` | Default model for new sessions (alias or full ID). `--model` and `ANTHROPIC_MODEL` override it per session. | `"model": "claude-sonnet-5"` |
| `permissions` | Object holding `allow`, `ask`, `deny`, `defaultMode`, `additionalDirectories`, etc. (see section 2) | see below |
| `permissions.defaultMode` | Starting permission mode: `default`, `acceptEdits`, `plan`, `auto`, `dontAsk`, `bypassPermissions`, `manual` (alias of `default`). `auto` and `bypassPermissions` do **not** take effect from project/local files; put them in `~/.claude/settings.json`. | `"permissions": {"defaultMode": "acceptEdits"}` |
| `env` | Environment variables for every session and its subprocesses (string values). | `"env": {"DISABLE_AUTO_COMPACT": "1"}` |
| `hooks` | Hook configuration (section 7). | |
| `disableAllHooks` | `true` turns off hooks (cannot disable managed hooks from a non-managed file). (hooks) | `"disableAllHooks": true` |
| `statusLine` | Object `{ "type": "command", "command": "...", "padding": n, "refreshInterval": s, "hideVimModeIndicator": bool }`. | section 10 |
| `outputStyle` | Name of a built-in or custom output style; case-sensitive. | `"outputStyle": "Explanatory"` |
| `sandbox` | Sandbox settings, e.g. `sandbox.enabled` (section 3). | `"sandbox": {"enabled": true}` |
| `autoMemoryEnabled` | `false` turns auto memory off (default `true`). | `"autoMemoryEnabled": false` |
| `autoMemoryDirectory` | Custom auto-memory dir (absolute or `~/` path). | `"autoMemoryDirectory": "~/my-memory-dir"` |
| `claudeMd` | **Managed-only**: inject CLAUDE.md text as organization memory. | |
| `claudeMdExcludes` | Exclude specific CLAUDE.md files from loading. (memory) | |
| `enabledPlugins` | Plugins enabled at that scope (section 9). | |
| `extraKnownMarketplaces` | Declare plugin marketplaces in settings. | |
| `enableAllProjectMcpServers`, `disabledMcpjsonServers` | Approve / block `.mcp.json` servers. (settings-reference, mcp) | |
| `agent` | Run the main session as a named subagent (also `--agent`). (settings-reference; local help) | |
| `apiKeyHelper` | Command that supplies credentials. | |
| `cleanupPeriodDays` | Transcript retention period. | |
| `disableAutoMode` | `"disable"` removes auto mode (also accepted as `permissions.disableAutoMode`). | `"disableAutoMode": "disable"` |
| `permissions.disableBypassPermissionsMode` | `"disable"` blocks bypass mode. (permissions) | |
| `effortLevel`, `fallbackModel`, `availableModels`, `language`, `spinnerTipsEnabled`, `respectGitignore`, `plansDirectory`, `companyAnnouncements` | Other documented keys (see the reference for each). | |

Minimal working `~/.claude/settings.json` (taken from the settings page):
```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "permissions": {
    "allow": ["Bash(npm run lint)", "Bash(npm run test *)"],
    "deny": ["Read(./.env)", "Read(./.env.*)"]
  }
}
```

---

## 2. Permissions

Source: https://code.claude.com/docs/en/permissions , https://code.claude.com/docs/en/permission-modes

### 2.1 Rule basics
- Format: `Tool` or `Tool(specifier)`. Lists: `permissions.allow`, `permissions.ask`, `permissions.deny`.
- **Evaluation order: deny, then ask, then allow.** First match wins; specificity does not matter. An allow rule cannot carve an exception out of a deny rule.
- A deny at **any** settings level cannot be overridden by any other level (e.g. a managed deny beats `--allowedTools`).
- A bare tool-name deny (e.g. `"Bash"`) removes the tool from Claude's context entirely; a scoped deny (`Bash(rm *)`) blocks only matching calls.
- Rules are enforced by Claude Code, not by the model; CLAUDE.md text does not grant or revoke access.
- Manage interactively with `/permissions`.
- Use canonical tool names (from https://code.claude.com/docs/en/tools-reference), not display labels.

### 2.2 Syntax by tool

| Rule | Effect |
|---|---|
| `Bash` or `Bash(*)` | All Bash commands |
| `Bash(npm run build)` | Exactly that command |
| `Bash(npm run *)` | Prefix match; trailing ` *` also matches the bare `npm run` |
| `Bash(ls:*)` | Legacy equivalent of `Bash(ls *)` (`:*` only recognized at the end) |
| `Bash(ls*)` | No space, so also matches `lsof` |
| `Read(./.env)` | Read of `.env` in current directory |
| `Edit(/docs/**)` | Edits under `<primary working dir>/docs/` (when defined in project settings) |
| `Read(~/.zshrc)` | Home-relative path |
| `Edit(//tmp/scratch.txt)` | Absolute path (note the double slash) |
| `WebFetch(domain:example.com)` | Fetches to example.com only; add `domain:*.example.com` for subdomains |
| `mcp__puppeteer` / `mcp__puppeteer__*` | All tools of MCP server `puppeteer` |
| `mcp__puppeteer__puppeteer_navigate` | One MCP tool |
| `Agent(Explore)` | The Explore subagent (use in `deny` to disable it) |
| `Agent(model:opus)` | Parameter match (deny/ask rules only) |

Path anchoring for `/path` rules: in project or local settings it is `<primary working directory>/path`; in **user** settings it is `~/.claude/path`; for `--settings <file>` it is the file's directory. Use `//` for absolute and `~/` for home. (permissions, "Where a pattern anchors")

Wildcards and gotchas (permissions):
- Put `*` after the subcommand: `Bash(git log *)` allows only `git log`; `Bash(git *)` allows all git.
- Shell operators (`&&`, `||`, `;`, `|`, `|&`, `&`, newline) are understood: every subcommand must be allowed.
- Wrappers `timeout`, `time`, `nice`, `nohup`, `stdbuf`, `command`, `builtin`, `noglob` are stripped before matching.
- Tool-name globs: deny/ask rules accept `"*"` or `"mcp__*"`; allow rules accept globs only after a literal `mcp__<server>__` prefix.
- MCP rules with parentheses in settings files are skipped (use `--disallowedTools` for MCP parameter matching).
- Server names with `.` or spaces become `_` in rule names; plugin MCP servers use `mcp__plugin_<plugin>_<server>__*`.
- "Yes, and don't ask again" saves Bash/WebFetch approvals to `.claude/settings.local.json`; file-edit approvals last only for the session.

Example:
```json
{
  "permissions": {
    "allow": ["Bash(npm run *)", "Bash(git commit *)"],
    "deny": ["Bash(git push *)"]
  }
}
```

### 2.3 Permission modes

| Mode | Behaviour |
|---|---|
| `default` | Prompts on first use of each tool. Labeled **Manual** in the UI; `manual` is an accepted alias |
| `acceptEdits` | Auto-accepts file edits and common filesystem commands (`mkdir`, `touch`, `mv`, `cp`) in working dirs |
| `plan` | Reads and explores, does not edit source files |
| `auto` | No routine prompts; a background classifier checks actions first |
| `dontAsk` | Auto-denies anything that would prompt; pre-approved tools still run |
| `bypassPermissions` | Skips prompts (except actions no mode auto-approves). Use only in isolated containers/VMs |

- Switch with **Shift+Tab** in the CLI; set start mode with `--permission-mode <mode>` (local choices: `acceptEdits`, `auto`, `bypassPermissions`, `manual`, `dontAsk`, `plan`) or `permissions.defaultMode`. `--dangerously-skip-permissions` = bypass. (permission-modes; local-cli-help.md)
- **Surprise:** the *built-in* starting mode in a terminal or VS Code is now **`auto`** on v2.1.283+ (if auto mode is available); `claude -p` and the Agent SDK start in `default`. Setting `disableAutoMode` makes the default `default`. (permission-modes, "Which mode a session starts in")

---

## 3. Sandboxing

Source: https://code.claude.com/docs/en/sandboxing , settings-reference "Sandbox settings"

- **What:** an OS-enforced boundary around the **shell commands** Claude runs (Bash, PowerShell, Monitor and their child processes). Built on the open-source `@anthropic-ai/sandbox-runtime` package.
- **Platforms:** macOS (Seatbelt, built in), Linux and WSL2 (need `bubblewrap` and `socat`). Native Windows runs commands unsandboxed.
- **Off by default.** Enable with `/sandbox` (writes `sandbox.enabled` to `.claude/settings.local.json`) or set it yourself:
```json
{ "sandbox": { "enabled": true } }
```
- **Default restrictions:**
  - Writes: only the working directory, a per-user temp dir, and added directories; protected paths stay write-denied. Widen with `sandbox.filesystem.allowWrite`.
  - Reads: most of the machine (including `~/.ssh`) unless you add `sandbox.filesystem.denyRead` / credential settings.
  - Network: no direct route out; a local proxy allows only `sandbox.network.allowedDomains` (starts empty).
  - Env vars: inherited.
- **Not sandboxed:** Read/Edit/Write/WebFetch/WebSearch tools (governed by permissions), hooks, local MCP servers, status line command, `apiKeyHelper`, `!` commands you type, `excludedCommands`, and unsandboxed retries.
- **Modes:** auto-allow (default `autoAllowBashIfSandboxed: true`, sandboxed commands run without prompting) vs regular permissions mode.
- If the sandbox can't start, commands run unsandboxed unless `sandbox.failIfUnavailable` is set.
- Sandbox paths use normal conventions (`/tmp/build` absolute, `~/.kube` home), unlike permission rules (`//` absolute).

Example:
```json
{
  "sandbox": {
    "enabled": true,
    "filesystem": { "allowWrite": ["~/.kube", "/tmp/build"] }
  }
}
```

---

## 4. Memory (CLAUDE.md and auto memory)

Source: https://code.claude.com/docs/en/memory

### 4.1 CLAUDE.md locations (load order, broadest first)

| Scope | Location |
|---|---|
| Managed policy | macOS `/Library/Application Support/ClaudeCode/CLAUDE.md`; Linux/WSL `/etc/claude-code/CLAUDE.md`; Windows `C:\Program Files\ClaudeCode\CLAUDE.md` |
| User | `~/.claude/CLAUDE.md` |
| Project | `./CLAUDE.md` or `./.claude/CLAUDE.md` |
| Local | `./CLAUDE.local.md` (personal; add to `.gitignore`) |

- Files in the working directory **and every parent** load at launch, concatenated (not overriding), root first. `CLAUDE.local.md` is appended after `CLAUDE.md` at each level.
- CLAUDE.md files in **subdirectories** load on demand when Claude reads/edits files there.
- **CLAUDE.local.md status:** still documented and supported (not deprecated). With `CLAUDE_CODE_NEW_INIT=1`, `/init`'s personal option creates it and gitignores it.
- `AGENTS.md`: read directly (v2.1.277+) when there is no CLAUDE.md/CLAUDE.local.md; if both exist only CLAUDE.md loads unless configured otherwise.
- CLAUDE.md files over 4 MiB are skipped.
- `/init` generates a starter CLAUDE.md. (commands)

### 4.2 Imports
- Syntax `@path/to/file` anywhere in CLAUDE.md; relative paths resolve from the importing file; absolute and `~/` paths allowed; max depth **four hops**; ignored inside code spans/blocks; escape spaces with `\ `.
- Imports outside the working directory in project files trigger a one-time approval dialog.
```text
See @README for project overview and @package.json for available npm commands.
- git workflow @docs/git-instructions.md
```

### 4.3 Rules directory
- `.claude/rules/*.md` (recursive) load like `.claude/CLAUDE.md`. User rules: `~/.claude/rules/`.
- Path-scoped rules with frontmatter:
```markdown
---
paths:
  - "src/api/**/*.ts"
---
# API Development Rules
- All API endpoints must include input validation
```

### 4.4 `/memory`
Lists CLAUDE.md, CLAUDE.local.md and other memory files (user and project), opens them in your editor (creating if missing), toggles auto memory, and opens the auto-memory folder.

### 4.5 Auto memory
- Notes Claude writes for itself (types `user`, `feedback`, `project`, `reference`). On by default in local sessions.
- Stored at `~/.claude/projects/<project>/memory/` (one per git repo, shared across worktrees; machine-local). Contains `MEMORY.md` (index) plus topic files.
- First **200 lines or 25KB** of `MEMORY.md` load each session; topic files are read on demand.
- Turn off: `/memory` toggle, `"autoMemoryEnabled": false`, or `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`. Relocate: `autoMemoryDirectory`.
- Saying "remember that..." saves to auto memory; to put it in CLAUDE.md, ask explicitly or edit via `/memory`.

---

## 5. Skills and custom slash commands

Source: https://code.claude.com/docs/en/skills

### 5.1 Locations

| Location | Path |
|---|---|
| Enterprise | `.claude/skills/<skill-name>/SKILL.md` inside the managed settings directory |
| Personal | `~/.claude/skills/<skill-name>/SKILL.md` |
| Project | `.claude/skills/<skill-name>/SKILL.md` |
| Nested | `<subdir>/.claude/skills/<skill-name>/SKILL.md` |
| Plugin | `<plugin>/skills/<skill-name>/SKILL.md` (invoked as `/plugin-name:skill-name`) |

Name clashes: enterprise > personal > project; a skill beats a same-named `.claude/commands/` file. Don't name a skill folder `synced` or `anthropic-skills`.

### 5.2 Format
`SKILL.md` = YAML frontmatter between `---` lines + Markdown instructions. All fields optional; `description` recommended.

```yaml
---
name: deploy
description: Deploy the application to production
disable-model-invocation: true
---

Deploy $ARGUMENTS to production:
1. Run the test suite
2. Build the application
```

Frontmatter fields: `name`, `description`, `when_to_use`, `argument-hint`, `arguments`, `disable-model-invocation`, `user-invocable`, `allowed-tools`, `disallowed-tools`, `model`, `effort`, `context` (`fork`), `agent`, `background`, `hooks`, `paths`, `shell` (`bash`/`powershell`), `metadata`, `license`, `compatibility`. Unknown fields are silently ignored. `description` + `when_to_use` are truncated at 1,536 characters in the listing.

Substitutions: `$ARGUMENTS`, `$ARGUMENTS[N]`, `$N`, `$name`, `${CLAUDE_SESSION_ID}`, `${CLAUDE_EFFORT}`, `${CLAUDE_SKILL_DIR}`, `${CLAUDE_PROJECT_DIR}`, `${CLAUDE_PLUGIN_ROOT}`, `${CLAUDE_PLUGIN_DATA}`. Dynamic context: `` !`command` `` lines run before Claude sees the skill.

### 5.3 Invocation
- Default: you can type `/skill-name` and Claude can load it automatically when the description matches (only the description sits in context until invoked).
- `disable-model-invocation: true`: only you can invoke.
- `user-invocable: false`: only Claude can invoke (hidden from `/` menu).
- `/skills` lists available skills. (commands)

### 5.4 Supporting files
Extra files in the skill directory (e.g. `reference.md`, `examples.md`, `scripts/helper.py`) are loaded/executed only when `SKILL.md` points Claude to them.

### 5.5 Custom slash commands (`.claude/commands/`)
- **Still supported, but merged into skills.** "A file at `.claude/commands/deploy.md` and a skill at `.claude/skills/deploy/SKILL.md` both create `/deploy` and work the same way." Command files accept the same frontmatter except `name` and `paths`; skills are preferred for new work.
- `.claude/commands/frontend/component.md` becomes `/frontend:component`.
- Plugins may still ship `commands/` (flat Markdown files, "the older form of skills"). (plugins/create)

---

## 6. Subagents

Source: https://code.claude.com/docs/en/sub-agents

### 6.1 Locations (priority, highest first)
1. Managed settings directory `.claude/agents/`
2. `--agents '<json>'` CLI flag (session only)
3. `.claude/agents/` (project; scanned recursively, walking up to repo root)
4. `~/.claude/agents/` (user)
5. Plugin `agents/` directory

### 6.2 File format
```markdown
---
name: code-reviewer
description: Reviews code for quality and best practices
tools: Read, Glob, Grep
model: sonnet
---

You are a code reviewer. When invoked, analyze the code and provide
specific, actionable feedback on quality, security, and best practices.
```
The body is the subagent's system prompt. Only `name` and `description` are required.

Frontmatter fields (camelCase): `name`, `description`, `tools`, `disallowedTools`, `model` (`sonnet`, `opus`, `haiku`, `fable`, full ID, or `inherit`), `permissionMode`, `maxTurns`, `autoCompactWindow`, `skills`, `mcpServers`, `hooks`, `memory` (`user`/`project`/`local`), `background`, `omitClaudeMd`, `effort`, `isolation` (`worktree`), `color`, `initialPrompt`, `experimental`. Plugin subagents ignore `hooks`, `mcpServers`, `permissionMode`.

CLI form:
```bash
claude --agents '{"code-reviewer": {"description": "Expert code reviewer.", "prompt": "You are a senior code reviewer.", "tools": ["Read", "Grep", "Glob", "Bash"], "model": "sonnet"}}'
```

### 6.3 Built-in subagents
- **Explore**: fast, read-only codebase search (Write/Edit denied).
- **Plan**: read-only research during plan mode.
- **general-purpose**: all tools, multi-step tasks.
- Others: `claude` (catch-all), `statusline-setup` (Sonnet, used by `/statusline`), `claude-code-guide` (Haiku, answers Claude Code questions).
- Disable one with `"permissions": {"deny": ["Agent(Explore)"]}`.

### 6.4 `/agents`
**Surprise:** per https://code.claude.com/docs/en/commands, `/agents` now only "Print[s] a reminder to ask Claude to create or manage subagents, or to edit `.claude/agents/` or `~/.claude/agents/` directly. On v2.1.197 and earlier, opens an interactive interface." Older tutorials that describe an `/agents` wizard are out of date. Files are hot-reloaded within seconds.

---

## 7. Hooks

Source: https://code.claude.com/docs/en/hooks , https://code.claude.com/docs/en/hooks-guide

### 7.1 Where hooks live
`~/.claude/settings.json`, `.claude/settings.json`, `.claude/settings.local.json`, managed settings, plugin `hooks/hooks.json`, skill frontmatter, subagent frontmatter. Hooks merge across levels. Browse with `/hooks` (read-only).

### 7.2 Config shape (event -> matcher group -> handlers)
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          { "type": "command", "command": "/path/to/lint-check.sh" }
        ]
      }
    ]
  }
}
```

### 7.3 All hook events (as of 2.1.319 docs)
`SessionStart`, `Setup`, `InstructionsLoaded`, `UserPromptSubmit`, `UserPromptExpansion`, `MessageDisplay`, `PreToolUse`, `PermissionRequest`, `PermissionDenied`, `PostToolUse`, `PostToolUseFailure`, `PostToolBatch`, `Notification`, `SubagentStart`, `SubagentStop`, `TaskCreated`, `TaskCompleted`, `Stop`, `StopFailure`, `TeammateIdle`, `ConfigChange`, `CwdChanged`, `DirectoryAdded`, `FileChanged`, `WorktreeCreate`, `WorktreeRemove`, `PreCompact`, `PostCompact`, `PreModelSwitch`, `PostModelSwitch`, `SessionEnd`, `Elicitation`, `ElicitationResult` (33 events).

### 7.4 Matchers
- `"*"`, `""` or omitted = all. Letters/digits/`_`/`-`/spaces/`,`/`|` only = exact names (`Edit|Write`). Any other character = unanchored JavaScript regex (`mcp__memory__.*`, `^Notebook`).
- Tool events match `tool_name`; `SessionStart` matches `startup|resume|clear|compact|fork`; `PreCompact` matches `manual|auto`; `Notification` matches types like `permission_prompt`, `idle_prompt`; `UserPromptSubmit`, `Stop`, etc. have no matcher.
- Per-handler `if` field uses permission-rule syntax (`"Bash(git *)"`), tool events only.

### 7.5 Handler types
`command`, `http`, `mcp_tool`, `prompt`, `agent` (agent hooks are experimental). Common fields: `type`, `if`, `timeout` (defaults: 600s command/http/mcp_tool, 30s prompt, 60s agent), `statusMessage`, `once` (skills only). Command hooks also support `async: true`.

Prompt hook example (response schema `{ "ok": true }` or `{ "ok": false, "reason": "..." }`):
```json
{
  "hooks": {
    "Stop": [
      { "hooks": [ { "type": "prompt", "prompt": "Evaluate if Claude should stop: $ARGUMENTS. Check if all tasks are complete." } ] }
    ]
  }
}
```

### 7.6 Input
JSON on stdin (command) or POST body (http). Common fields: `session_id`, `prompt_id`, `transcript_path`, `cwd`, `scratchpad_dir`, `permission_mode`, `effort`, `hook_event_name`, plus `agent_id`/`agent_type` in subagents. Tool events add `tool_name`, `tool_input`, `tool_use_id`. `CLAUDE_PROJECT_DIR` is available to reference scripts.

### 7.7 Exit codes
- **0** = success; JSON on stdout is applied. Plain stdout becomes context for Claude only on `UserPromptSubmit`, `UserPromptExpansion`, `SessionStart`, `PostModelSwitch` (and compaction instructions on `PreCompact`).
- **2** = blocking error; stderr is the reason. Blocks on e.g. `PreToolUse`, `UserPromptSubmit`, `Stop` (keeps Claude going), `SubagentStop`, `PreCompact`, `ConfigChange`, `PostToolBatch`, `TaskCreated`, `TaskCompleted`, `TeammateIdle`, `PreModelSwitch`, `Elicitation`. On `PostToolUse` it only shows stderr to Claude. Not honored on `PermissionRequest`.
- **Other** = non-blocking error; action proceeds.

### 7.8 JSON output
Universal: `continue`, `stopReason`, `suppressOutput` (now has no effect), `systemMessage`, `terminalSequence`. Many events use top-level `"decision": "block", "reason": "..."`. `PreToolUse` uses:
```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Database writes are not allowed"
  }
}
```
`permissionDecision` values: `allow`, `deny`, `ask`, `defer` (precedence deny > defer > ask > allow). Old top-level `approve`/`block` for PreToolUse are deprecated. `PermissionRequest` uses `hookSpecificOutput.decision.behavior` (`allow`/`deny`).

---

## 8. MCP

Source: https://code.claude.com/docs/en/mcp ; `claude mcp --help`, `claude mcp add --help` (local)

### 8.1 Adding servers
```bash
# HTTP (recommended for remote)
claude mcp add --transport http notion https://mcp.notion.com/mcp
claude mcp add --transport http secure-api https://api.example.com/mcp --header "Authorization: Bearer your-token"

# SSE (deprecated; http now auto-falls back to SSE on v2.1.265+)
claude mcp add --transport sse asana https://mcp.asana.com/sse

# stdio: options BEFORE the name, server command AFTER --
claude mcp add --env AIRTABLE_API_KEY=YOUR_KEY --transport stdio airtable -- npx -y airtable-mcp-server

# From JSON (also the only way to add WebSocket "type": "ws")
claude mcp add-json weather-api '{"type":"http","url":"https://api.weather.com/mcp"}'
```
Local help: `-t, --transport` choices `stdio, sse, http` (defaults to stdio); `-s, --scope` `local, user, project` (default `local`). Other subcommands: `list`, `get <name>`, `remove <name>`, `add-from-claude-desktop`, `login <name>`, `logout <name>`, `reset-project-choices`. In-session: `/mcp`.

### 8.2 Scopes

| Scope | Loads in | Stored in |
|---|---|---|
| `local` (default) | current project, only you | `~/.claude.json` under that project's path |
| `project` | current project, shared | `.mcp.json` at project root (commit it) |
| `user` | all your projects | `~/.claude.json` |

Precedence on name clash: local > project > user > plugin servers > claude.ai connectors. Project `.mcp.json` servers require approval in interactive sessions.

### 8.3 `.mcp.json` format
```json
{
  "mcpServers": {
    "api-server": {
      "type": "http",
      "url": "${API_BASE_URL:-https://api.example.com}/mcp",
      "headers": { "Authorization": "Bearer ${API_KEY}" }
    }
  }
}
```
Supports `${VAR}` and `${VAR:-default}` in `command`, `args`, `env`, `url`, `headers`. An entry with `url` but no `type` is an error (no `type` means stdio). `streamable-http` is an alias for `http`.

### 8.4 OAuth
Add the server, then run `/mcp` in a session and follow the browser flow, or `claude mcp login <name>` from the shell (`--no-browser` for SSH). `claude mcp logout <name>` clears credentials. Tokens are stored securely and refreshed automatically. `-p` runs cannot do the OAuth flow.

### 8.5 Resources and prompts
- Resources: type `@` to see them; reference as `@server:protocol://resource/path`, e.g. `@github:issue://123`.
- Prompts: appear as commands `/servername:promptname (MCP)`; `/mcp__servername__promptname` also works, e.g. `/mcp__github__pr_review 456`.

### 8.6 Tool naming for permissions
`mcp__<server>__<tool>`; whole server `mcp__<server>__*`; claude.ai connectors `mcp__claude_ai_<server>__<tool>`; plugin servers `mcp__plugin_<plugin>_<server>__*`. (permissions)

---

## 9. Plugins

Source: https://code.claude.com/docs/en/plugins/create , /plugins/manifest-reference , /plugins/marketplace-reference , /plugins/install ; `claude plugin --help` (local)

### 9.1 Directory layout
| Location | Contents |
|---|---|
| `.claude-plugin/plugin.json` | Manifest (only this file goes in `.claude-plugin/`) |
| `skills/<name>/SKILL.md` | Skills |
| `commands/` | Flat Markdown commands (older form) |
| `agents/` | Subagent Markdown files |
| `hooks/hooks.json` | `{"hooks": {...}}`, same shape as settings |
| `.mcp.json` | MCP server definitions |
Also documented: `output-styles/`, LSP servers (`.lsp.json`), monitors, themes.

### 9.2 Minimal `plugin.json`
```json
{
  "name": "my-first-plugin",
  "description": "A greeting plugin to learn the basics",
  "version": "1.0.0",
  "author": { "name": "Your Name" }
}
```
Only `name` is required (and the manifest itself is optional). Other fields include `displayName`, `homepage`, `repository`, `license`, `keywords`, `defaultEnabled`, `dependencies`, `skills`, `commands`, `agents`, `hooks`, `mcpServers`, `lspServers`, `outputStyles`, `userConfig`. Use `${CLAUDE_PLUGIN_ROOT}` for bundled paths.

Test and validate:
```bash
claude plugin validate ./my-first-plugin
claude --plugin-dir ./my-first-plugin     # then run /my-first-plugin:hello
```

### 9.3 Marketplaces
File: `.claude-plugin/marketplace.json` at the marketplace root. Required: `name`, `owner` (with `name`), `plugins` (each entry needs `name` and `source`).
```json
{
  "name": "my-marketplace",
  "owner": { "name": "Your Name" },
  "plugins": [
    { "name": "formatter", "source": "./plugins/formatter" }
  ]
}
```
(This combined example is assembled from the documented required fields and the documented relative-path entry; it was not copied verbatim from one docs block.) Plugin source types: relative path, `github`, `url`, `git-subdir`, `npm`, `archive`, `command`.

### 9.4 Commands
```text
/plugin                                          # browse (Discover / Installed tabs)
/plugin marketplace add anthropics/claude-plugins-official
/plugin install commit-commands@claude-plugins-official
```
```bash
claude plugin marketplace add your-org/plugins
claude plugin install formatter@your-org --scope project
claude plugin enable formatter@your-org
claude plugin disable formatter@your-org
claude plugin uninstall formatter@your-org --scope project
```
Install scopes: user (`enabledPlugins` in `~/.claude/settings.json`), project (`.claude/settings.json`), local (`.claude/settings.local.json`). `/reload-plugins` loads newly installed plugins. Local CLI also lists `plugin init|new`, `details`, `configure`, `eval`, `validate`.

---

## 10. Output styles, status line, headless mode, Agent SDK, CI

### 10.1 Output styles (https://code.claude.com/docs/en/output-styles)
- Built-ins: Default, **Proactive**, **Concise**, **Explanatory**, **Learning**. (Proactive and Concise are newer; older material lists only Default/Explanatory/Learning.)
- Switch: `/output-style <style>` (or `/config` > Output style); saves to `.claude/settings.local.json`. Or set `"outputStyle": "Explanatory"` (case-sensitive).
- Custom style: Markdown file in `~/.claude/output-styles/`, `.claude/output-styles/`, or managed dir. Frontmatter: `name`, `description`, `keep-coding-instructions`, `force-for-plugin` (plugins only).
```markdown
---
name: Diagrams first
description: Lead every explanation with a diagram
keep-coding-instructions: true
---
When explaining code, start with a Mermaid diagram, then explain in prose.
```

### 10.2 Status line (https://code.claude.com/docs/en/statusline)
- `/statusline <description>` generates a script and updates settings.
- Manual: script receives session JSON on stdin, prints the line to stdout.
```bash
#!/bin/bash
input=$(cat)
MODEL=$(echo "$input" | jq -r '.model.display_name')
DIR=$(echo "$input" | jq -r '.workspace.current_dir')
PCT=$(echo "$input" | jq -r '.context_window.used_percentage // 0' | cut -d. -f1)
echo "[$MODEL] ${DIR##*/} | ${PCT}% context"
```
```json
{ "statusLine": { "type": "command", "command": "~/.claude/statusline.sh", "padding": 2 } }
```
(`chmod +x ~/.claude/statusline.sh`.) The status line command runs outside the sandbox.

### 10.3 Headless / print mode (https://code.claude.com/docs/en/headless)
```bash
claude -p "What does the auth module do?"
claude -p "Summarize this project" --output-format json | jq -r '.result'
claude -p "Explain recursion" --output-format stream-json --verbose --include-partial-messages
claude -p "Extract function names" --output-format json --json-schema '{"type":"object","properties":{"functions":{"type":"array","items":{"type":"string"}}},"required":["functions"]}'
claude -p "Run the tests and fix failures" --allowedTools "Bash,Read,Edit"
claude -p "Now focus on the database queries" --continue
claude -p "Continue that review" --resume "$session_id"
```
- `--output-format`: `text` (default), `json`, `stream-json`. `--input-format`: `text` or `stream-json`. Structured output lands in `structured_output`.
- `--bare` skips auto-discovery of hooks, skills, plugins, MCP, CLAUDE.md, auto memory (good for CI).
- `--permission-prompts none` (v2.1.259+) for unattended runs. `--append-system-prompt` / `--system-prompt` customize the prompt.
- Exit code 0 on success, non-zero on failure.

### 10.4 Claude Agent SDK (https://code.claude.com/docs/en/agent-sdk/overview , /agent-sdk/quickstart)
- TypeScript: `npm install @anthropic-ai/claude-agent-sdk` -> `import { query } from "@anthropic-ai/claude-agent-sdk";`
- Python: `pip install claude-agent-sdk` (or `uv add claude-agent-sdk`) -> `from claude_agent_sdk import query, ClaudeAgentOptions`
```python
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions

async def main():
    async for message in query(
        prompt="Review utils.py for bugs.",
        options=ClaudeAgentOptions(allowed_tools=["Read", "Edit", "Glob"], permission_mode="acceptEdits"),
    ):
        print(message)

asyncio.run(main())
```
(Shortened from the quickstart's example, which also branches on `AssistantMessage`/`ResultMessage`.) Repos: `anthropics/claude-agent-sdk-typescript`, `anthropics/claude-agent-sdk-python`.

### 10.5 GitHub Actions (https://code.claude.com/docs/en/github-actions)
- Quick setup: run `/install-github-app` in Claude Code (github.com repos only). It installs the Claude GitHub App, adds the secret, and opens a workflow PR.
- Action: `anthropics/claude-code-action@v1` (repo https://github.com/anthropics/claude-code-action). Mention `@claude` in a PR/issue comment.
```yaml
name: Claude Code
on:
  issue_comment:
    types: [created]
  pull_request_review_comment:
    types: [created]
jobs:
  claude:
    if: contains(github.event.comment.body, '@claude')
    runs-on: ubuntu-latest
    permissions:
      contents: write
      pull-requests: write
      issues: write
      id-token: write
      actions: read
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 1
      - uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
```
- Common inputs: `prompt`, `claude_args`, `anthropic_api_key`, `claude_code_oauth_token` (from `claude setup-token`), `github_token`, `plugin_marketplaces`, `plugins`, `settings`, `trigger_phrase` (default `@claude`), `use_bedrock`, `use_vertex`, `use_foundry`.

### 10.6 GitLab CI/CD (https://code.claude.com/docs/en/gitlab-ci-cd)
- Documented, **beta**, and "maintained by GitLab". Setup: add masked CI/CD variable `ANTHROPIC_API_KEY`, then a job in `.gitlab-ci.yml` that installs Claude Code (`curl -fsSL https://claude.ai/install.sh | bash`) and runs `claude -p "..." --permission-mode acceptEdits --allowedTools "Bash Read Edit Write mcp__gitlab"`. Supports Claude API, Amazon Bedrock and Google Cloud's Agent Platform.

---

## UNVERIFIED / caveats
- The combined `marketplace.json` example in 9.3 is assembled from documented required fields, not copied from one block; the field rules are verified.
- I did not read every key in the 450 KB settings reference; only the keys described above were checked one by one. Keys named only in the "Other documented keys" row were confirmed to exist as headings but their details were not read.
- MCP `--transport ws` is **not** supported; WebSocket servers are configured only through `.mcp.json` or `add-json` (verified). WebSocket authentication details beyond headers were not checked.
- Fast-moving: many behaviours carry version notes (e.g. auto as built-in default from v2.1.283; `/agents` UI removed after v2.1.197). Re-check if the textbook targets a different version.
