# Writing brief for chapter authors

You are writing chapters of the **AI & Claude Mastery**. It is an AI textbook with an exceptionally deep Claude specialisation, built for a QA engineer and their team. Readers include non-technical testers, analysts, managers and developers with 1–2 years' experience.

Source folder: the repository root (all paths below are relative to it).

## Before you write

1. Read `README.md` (build, layout, template).
2. Read two finished chapters to learn the house style and markup exactly:
   - `src/chapters/ch101.html` (Playwright and MCP: practical)
   - `src/chapters/ch6.html` (history and concepts: teaching)
   Skim `src/chapters/ch120.html` for code-heavy style.
3. Read `src/curriculum.json` for every chapter's number, title and level. Read `notes/CHAPTER-NOTES.md` for what your chapters must cover and what neighbouring chapters cover, so you don't overlap.
4. For anything that changes (models, prices, products, plans, commands, flags, settings, API syntax, company facts), use the verified research in `research/` first:
   - `anthropic-claude-facts.md`
   - `ai-industry-facts.md`
   - `claude-code-interface.md`
   - `claude-code-config.md`
   - `local-cli-help.md`

   After that, use official documentation (WebFetch/WebSearch). Never invent a command, flag, setting, URL, package, API field, model name, price, statistic, quote or date. If you can't verify something, leave it out or say plainly that it's unverified.

## Audience and voice

- Plain words first: short sentences, everyday language, active voice. Explain every technical term the first time it appears.
- Build depth gradually: plain idea → everyday analogy → correct terms → how it works inside (in `details.deep`) → real use.
- Use real QA and workplace examples: Jira stories, test cases, Playwright, API testing, CI, bug reports, release readiness.
- Keep a clear line between three skills: **understanding** a concept, **using** a tool, and **building** a system.
- Opinions and predictions go in `.box.opinion`, with the person or group who holds them. Never present an opinion as fact.
- Any numbers you invent for examples must be labelled "illustrative". Never present invented figures as data.
- British spelling is fine. No emoji. No hype.

## Required structure, in this order

Your file contains only the chapter body. The build adds the chapter header, number, labels, bookmark and navigation. Use ids `chN-1`, `chN-2`, … for sections and `chN-r` for Review, where N is your chapter number.

```html
<div class="objectives"><span class="tag">What you'll learn</span><ul><li>…</li></ul></div>
<div class="prereq"><b>Before you start:</b> … (link earlier chapters: <a href="#ch14">Chapter 14</a>)</div>
<div class="bigidea"><p>The whole chapter in 3–5 plain sentences.</p></div>

<h3 id="chN-1"><span class="num">N.1</span>Section title</h3>
<p>…</p>
<div class="box analogy"><span class="tag">In everyday life</span><p>…</p></div>
<div class="box example"><span class="tag">Real-world example</span><p>…</p></div>
<details class="deep"><summary>Title of the optional deeper explanation</summary><div class="body"><p>…</p></div></details>
<div class="box note"><span class="tag">…</span><p>…</p></div>
<div class="box warn"><span class="tag">…</span><p>…</p></div>
<div class="box opinion"><span class="tag">Opinion · …</span><p>…</p></div>
<div class="flow"><div><b>Step</b>text</div><div class="hl"><b>Key step</b>text</div><div><b>Step</b>text</div></div>
<div class="tbl"><table><tr><th>…</th></tr><tr><td>…</td></tr></table></div>
<div class="code"><span class="cap">Terminal</span><pre>command  <span class="c"># comment</span></pre></div>
<ol class="timeline"><li class="key"><span class="yr">2017</span><span class="ev"><b>Name</b> text</span></li></ol>
<div class="cols2"><div><h4>…</h4><p>…</p></div><div><h4>…</h4><p>…</p></div></div>
<div class="figure" role="img" aria-label="…"><div class="bars"><div class="bt">Title</div>
  <div class="bar-row"><span>Label</span><span class="track"><span class="fill hl" style="width:58%">15.3%</span></span></div></div>
  <div class="cap">Caption with source</div></div>
<div class="person"><span class="ini">AT</span><b>Name (years)</b><span>One-line description.</span></div>

<!-- searchable table: rows with class="group" are group headers -->
<input class="filter" data-filter="#myTable" data-empty="#myEmpty" type="search" placeholder="Filter…" aria-label="Filter">
<div class="tbl"><table id="myTable"><tr><th>…</th></tr><tr class="group"><td colspan="3">Group</td></tr><tr><td>…</td></tr></table></div>
<p id="myEmpty" hidden>No rows match.</p>

<div class="lab"><div class="lab-h"><b>Lab title</b><span>30 min · where</span></div><ol>
<li>Step…<span class="expect">what the reader should see.</span></li></ol></div>

<div class="box mistakes"><span class="tag">Common misunderstandings</span><dl><dt>"Myth."</dt><dd>Truth.</dd></dl></div>

<h3 id="chN-r"><span class="num">N.k</span>Review</h3>
<div class="box takeaways"><span class="tag">Key takeaways</span><ul><li>…</li></ul></div>
<div class="quiz"><div class="quiz-h">Check yourself</div>
<div class="qz"><p class="q">Question?</p><div class="opts"><button>Wrong</button><button data-ok>Right</button><button>Wrong</button></div><p class="why" hidden>Explanation (don't start with "Correct").</p></div>
</div>
<div class="box assignment"><span class="tag">Assignment</span><p>…</p></div>
<div class="box teach"><span class="tag">Teach it</span><p>"A two-minute explanation to give a colleague, in quotes."</p></div>
<div class="sources"><h4>Sources and further reading</h4><ol><li>…official links with target="_blank" rel="noopener"…</li></ol>
<p class="verified">Verified 9 November 2026 against … (or "Content type: established … · Last reviewed 9 November 2026")</p></div>
```

## Requirements

- **Length:** roughly 22–32 KB of HTML per chapter (reference or project chapters may be longer). These are textbook chapters, not summaries.
- **Coverage:** every chapter needs at least one diagram or table, one hands-on lab with expected results, 4–5 quiz questions (each with **exactly one** `data-ok`), an assignment, a "Teach it" box and sources.
- **Projects and labs must be completable:** give setup instructions, complete runnable source code (no "…" gaps in code), the expected output, and a short troubleshooting list. Use free and local options where possible, and offer an alternative when a lab needs company access.
- **Code:** test small code yourself when you can (Python 3 and Node are installed). Never hard-code secrets; use environment variables.
- **Escaping:** inside HTML, write `<` as `&lt;` and `&` as `&amp;` in text and code.
- **Glossary links:** `<a class="gl" href="#g-slug">word</a>`. The slug is the term in lower case with non-alphanumerics turned into `-`. Only link terms that already exist in `src/glossary.json` or `src/glossary.d/*.json`, or that you add yourself in `src/glossary.d/chN.json`, where N is your first chapter's number. Format: `{"Term": {"d": "plain definition", "see": "chN"}}`.
- **Cross-references:** `<a href="#chN">Chapter N</a>`, using the numbers in `src/curriculum.json`. Links to unwritten chapters are fine; the build handles them.
- **Files you may write:** your own `src/chapters/chN.html` files and your one `src/glossary.d/chN.json`. Do not edit any other file.

## Finish

1. Run `python3 build.py --check`. This is check-only; never run the full build.
2. Fix any problem in your own files. Problems in other authors' files are not yours: ignore them.
3. Reply in under 120 words: what each chapter covers, anything you couldn't verify, and the glossary terms you added.
