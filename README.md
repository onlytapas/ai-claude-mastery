# AI & Claude Mastery

A self-paced textbook on artificial intelligence, with a deep specialisation in Claude and Claude Code. It starts from zero, written in plain words for testers, analysts, managers and newer developers, and builds up to designing, configuring, testing, securing and teaching AI systems.

**Live:** https://onlytapas.github.io/ai-claude-mastery/

## What it covers

18 parts and 145 chapters, in five stages:

| Stage | Parts | You will be able to |
| --- | --- | --- |
| Foundation | I–VI | Explain how modern AI works, compare companies and models, and use the Claude apps well |
| Practical | VII–X | Work confidently in the terminal and Claude Code, and configure memory, settings, skills, hooks and MCP |
| Builder | XI–XIII | Build and deploy API-based applications, connect tools with MCP, and create agents |
| Professional | XIV–XVI | Apply AI across software, QA and business, safely and within the law |
| Expert | XVII–XVIII | Understand training, fine-tuning and serving, then practise with exams and projects |

Part XV, **AI-Powered QA**, is a full specialisation for testers: test design, automation, data, exploratory and non-functional testing, testing AI itself, measuring value, and building your own QA tools.

Every chapter has the same shape: what you'll learn, the big idea in plain words, everyday analogies, real examples, optional "Under the hood" depth, diagrams, a hands-on lab with the expected result, common misunderstandings, key takeaways, a quiz, an assignment, a "Teach it" summary and dated sources.

The site has search, a glossary with pop-up definitions, self-check quizzes, bookmarks, and light and dark themes. Bookmarks and the theme choice are kept in your own browser (`localStorage`); there is no backend, account, analytics or third-party script apart from Google Fonts.

## Accuracy

Facts that change (model names, prices, plans, commands, flags, settings, API details, laws) were checked against official sources and Claude Code 2.1.319 on 9 November 2026; each chapter shows its date and sources. The verified fact sheets are in `research/`. Predictions and opinions are kept in labelled boxes. Where something could not be confirmed, the text says so.

## Run it locally

No dependencies: only Python 3.

```
python3 build.py                                 # builds docs/index.html and audits it
python3 -m http.server 8000 --directory docs     # then open http://localhost:8000
```

`python3 build.py --check` audits without writing anything: broken links, duplicate ids, unbalanced tags and quiz questions without exactly one correct answer.

## Test

```
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest
ruff check . && ruff format --check .      # lint and formatting
```

GitHub Actions runs the lint, formatting, build and tests on every push (`.github/workflows/tests.yml`), and also checks that the committed `docs/index.html` matches the source.

The tests check that every chapter exists and follows the template, that section numbers and quizzes are correct, that every complete code file in the book parses (Python, JSON, shell, YAML), that nothing private is committed (no real keys, email addresses or home-folder paths), and, when Google Chrome is installed, that the site loads in headless Chrome with no errors, no broken links and no sideways scrolling.

## Personal offline copy

```
python3 export.py
```

Writes `share/AI-Claude-Mastery.html` (one offline file with the fonts embedded) and `share/AI-Claude-Mastery.pdf` (needs Google Chrome). Both are for your own use and are listed in `.gitignore`, so they are never committed.

## Updating the book

1. Edit a chapter in `src/chapters/`, or the curriculum in `src/curriculum.json`.
2. Run `python3 build.py`, then `pytest`.
3. Commit the source and the rebuilt `docs/index.html`; GitHub Pages serves `docs/` from `main`.

`notes/WRITING-BRIEF.md` describes the chapter template, markup and writing rules; `notes/CHAPTER-NOTES.md` lists what each chapter covers.

## Files

| Path | Purpose |
| --- | --- |
| `docs/index.html` | The built book, served by GitHub Pages from `docs/` |
| `src/curriculum.json` | Parts and chapters (id, title, level, reading and practice minutes), optional chapters, author details |
| `src/chapters/` | One HTML file per chapter (the chapter body only) |
| `src/front/`, `src/back/` | Welcome and "Where to start" pages; glossary and sources pages |
| `src/glossary.json`, `src/glossary.d/` | Glossary terms with plain definitions |
| `src/shell.html` | Page frame: header, contents rail, cover, footer |
| `assets/style.css`, `assets/app.js` | Theme (Sage, light and dark, print) and all interactivity |
| `build.py` | Assembles the book and audits the result |
| `export.py` | Optional personal offline HTML and PDF |
| `tests/` | pytest suite (`helpers.py` holds shared paths and parsers) |
| `pyproject.toml` | pytest and ruff (lint and format) settings |
| `.github/workflows/tests.yml` | Runs lint, build and tests on GitHub for every push |
| `requirements.txt` | Test and lint tools only; building needs nothing beyond Python 3 |
| `research/` | Verified fact sheets used when writing |
| `notes/` | Writing brief and chapter notes |

## Author

Written by Tapas Saha · [github.com/onlytapas](https://github.com/onlytapas) · [onlytapas.github.io](https://onlytapas.github.io/)

© 2026 Tapas Saha
