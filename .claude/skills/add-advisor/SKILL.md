---
name: add-advisor
description: Put a new advisor on Moksh's Meteoric Council by building their brain from everything they've put out — a YouTube channel or playlist, podcasts, books Moksh owns, or (for a private advisor like his mindset coach or CFO) recordings of his own sessions with them. Produces a council-ready brain in council/advisors/<slug>/, registers the seat in the roster and tests it. Use when Moksh says "add <name> to my council", "build a <name> brain", "make a <name> module", "put <name> on the board", or "build my mindset coach's brain".
---

> Meteoric Council · Add Advisor. Built for Moksh Vasant by Fulcrum Labs on FulcrumOS.

The council gets better every time Moksh seats someone whose thinking he trusts. This skill turns a person's public work (or his private sessions with them) into a brain that sits on the council the same way Alex Hormozi, Jeremy Haynes and Nik Setting already do.

The contract every brain follows is `council/docs/ADVISOR-BRAIN-SPEC.md`. Read it first. The finished Hormozi, Haynes and Setting brains in `council/advisors/` are the quality bar.

## Step 1: Who and from what

Ask, in one message, only what's missing:

1. **Who**, and the one job they'd do on the council ("funnels", "mindset", "deal structure").
2. **Public or private advisor?**
   - Public: YouTube channel or playlist, podcast feed, books he owns (PDF/EPUB in the OS), blog.
   - Private: a folder of call recordings or transcripts (mindset coach sessions, CFO calls). Private brains never leave the OS.
3. **How deep:** `quick` (10–15 videos, ~30 min) or `full` (30–40 videos plus books, ~1–2 hours). Default `full`.

Make the slug: lowercase, hyphenated (`iman-gadzhi`, `mindset-coach`).

## Step 2: Collect sources

Work in a scratch folder outside the repo: `~/.fulcrum/advisor-build/<slug>/`. Raw transcripts are never committed to the OS.

**YouTube (captions only, no video download):**

1. Check `yt-dlp` is installed (`yt-dlp --version`). If not, ask Moksh before installing it (`brew install yt-dlp` on Mac).
2. List the channel:
   `yt-dlp --flat-playlist --print "%(id)s|%(title)s|%(view_count)s|%(upload_date)s|%(duration)s" "https://www.youtube.com/@<handle>/videos"`
3. Pick the videos: most-viewed plus the most recent 12 months, long-form over Shorts, weighted to the council job from Step 1. Show Moksh the list (titles only) and let him add or drop any.
4. Fetch captions:
   `yt-dlp --skip-download --write-auto-subs --write-subs --sub-langs "en,en-orig,en-US" --sub-format json3 --sleep-requests 1 -i -o "<scratch>/%(id)s.%(ext)s" <urls>`
   Don't request translated tracks (it triggers rate limits). If YouTube starts asking for sign-in, stop and work with what you have.
5. Convert to timestamped text: `python3 council/scripts/captions_to_text.py <scratch>` writes `<id>.txt` files with `[mm:ss]` lines, then delete the `.json3` files.

**Books:** read the PDFs or EPUBs Moksh points to with the OS's PDF tools. Chapter by chapter, take notes into scratch with page numbers.

**Private sessions:** read every transcript in the folder Moksh names. If there are only recordings, use the OS's transcription setup (`grid.md`) or ask Moksh to export transcripts from Fathom.

## Step 3: Read and distil

For a full build, split the reading across sub-agents (one per 8–10 transcripts) so no single context bloats. Each returns notes in this shape: framework or idea, how they apply it, numbers with `[id mm:ss]`, mistakes they call out, short verbatim lines worth quoting with `[id mm:ss]`, stories with a confidence tag.

Then write the brain to the spec:

- `LENS.md` (always loaded; 4–8 KB): who, what they believe, what they check first, where they clash with the existing seats (read the other LENS files to know), how they talk, the file router, and how their thinking applies to Meteoric Boost.
- 3–8 topic files of framework cards.
- `quotes.md`, `stories.md` (with a do-not-state list), `sources.md`.

Private advisors also get, at the top of `LENS.md`: `privacy: private — built from Moksh's own sessions; never cite outside the OS`.

## Step 4: Register the seat

Add a row to the **Advisors** table in `council/ROSTER.md`: id, seat name, brain path, seat_when (from the LENS frontmatter), dissents_with, `status: live`. If the advisor fits a preset (finance / marketing / sales / fulfilment), ask Moksh whether to add them to it.

The advisor runs on the shared `council-advisor` agent, so no new agent file is needed.

## Step 5: Test before calling it live

Run three quick takes through `council-advisor` with `advisor: <slug>`:

1. A question squarely in their lane, about Meteoric.
2. A question outside their lane. The seat should say it's outside their lane, or reason carefully and lower its confidence.
3. A question where they'd disagree with an existing seat. Check the disagreement shows up.

Check each answer: it names a real framework from the brain, every quote exists in `quotes.md`, no invented numbers. Fix the brain if any test fails, then show Moksh the three answers.

## Step 6: Report

Tell Moksh: sources used (count), brain size, the five frameworks the seat leans on most, which presets it joined, and one example question to try. Delete the scratch folder's raw files once the brain is done, unless he wants them kept.

## Rules

- Captions and text only. Never download video or audio from YouTube.
- Distil in original words. Quotes under ~25 words, only in `quotes.md` or inline with a source.
- Every brain is labelled unofficial and simulated. A seat never claims to be the person.
- Private brains stay private.
