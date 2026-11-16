# Burundi: law history in git

<picture>
<source media="(prefers-color-scheme: dark)" srcset="data/effort-dark.svg">
<img alt="Burundian law in this repository: what it holds, changes by the year they took effect, completeness against the official sources, and the correctness of what is held" src="data/effort-light.svg" width="880">
</picture>

The law of Burundi as a git history, so far as a record of its laws and treaties without their text: one file per law or treaty, one commit per entry on the day recorded for it, and a key naming the record as the commit's author. `git log` lists every entry with its day; picking a date gives what the record held that day.

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is Burundi's national law, which global-law reads at `burundi/national/acts/`.

**What is in it now:** a catalogue of 206 laws and orders with no text: 14 WIPO Lex records (title, subject, dates), among them the 2005 Post-transition Interim Constitution, the 2009 Criminal Code and the 2015 Commercial Code, and the 192 laws of 2003-2012 listed on the National Assembly's site (number, promulgation date and a link to the scan); Burundi's signatures, ratifications and accessions for 45 treaties recorded by WIPO Lex and 48 multilateral treaties deposited with the UN Secretary-General (the two lists overlap); and five pages of facts on the legal system (constitution, legislature, courts, official languages, sources). No law or treaty text. [`catalogue/README.md`](catalogue/README.md) lists every law in the catalogue.

Each entry is one file: `catalogue/law-13386.md` is WIPO Lex's record of the Criminal Code (Law No. 1/05 of 22 April 2009), `catalogue/loi-2003-001.md` the National Assembly's entry for Loi n° 1/01 of 28 March 2003, and `treaties/treaty-19793.md` and `un-treaties/untc-xxvii-7-d.md` the Paris Agreement in each list. The facts on the legal system are in `legal-system/`.

The record is in English, as WIPO Lex and the UN Treaty Collection print it, with the National Assembly's law numbers in French. The laws themselves are in French.

## Questions as git commands

| Question | Command |
| --- | --- |
| What has Burundi signed, ratified or joined, and on what day? | `git log --format="%h %(trailers:key=In-force,valueonly,separator=) %an" -- treaties un-treaties` |
| Every change to the record of one treaty (the Paris Agreement) | `git log -p -- treaties/treaty-19793.md un-treaties/untc-xxvii-7-d.md` |
| The UN treaty actions on record on 1 January 2010 | `python tools/on.py 2010-01-01 un-treaties` |

**Outside git**, we also host this record publicly, for free:

- **[Ask Claude about Burundian law](https://global-law.lexifina.com/v1/try_claude?country=burundi)**: opens Claude with a first question ready.
- **[Ask ChatGPT](https://global-law.lexifina.com/v1/try_chatgpt?country=burundi)**: the same question in ChatGPT.
- **[Search the Burundi record on our site](https://lexifina.com/law?country=burundi&q=copyright)**: a search for "copyright" in its catalogue of titles, no account needed.
- **[Developer REST API](https://global-law.lexifina.com/v1/search_law?query=copyright&jurisdiction=burundi)**: the same search as JSON, with no key. See the [documentation here](https://lexifina.com/api/global-law).

Both assistants read the record through the free Global law connector (MCP, `https://global-law.lexifina.com/mcp`); the first time, the chat gives you the link that adds it. Ask in English or in French.

**Host it yourself easily.** All it takes is git and Python, and the tools run on your machine:

```sh
git clone --depth 1 https://github.com/lexifina/global-law && cd global-law
python3 tools/countries.py add burundi/national/acts
python3 tools/law.py show 2026-01-01 burundi/national/acts/treaties/treaty-19793.md
```

Opened in Claude Code, Cursor, VS Code or Codex, the clone also starts a local MCP server with the same tools ([MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md)).

## Dates

Each commit is dated at noon, Africa/Bujumbura, on the day recorded for the entry, and carries it in its `In-force:` trailer:

- a treaty, by Burundi's own action: its ratification, accession or similar instrument, else the treaty's entry into force for Burundi, else its signature; the UN list has one version per action;
- a WIPO Lex law, by the date WIPO Lex records (promulgation, entry into force, commencement or adoption, in that order); where WIPO Lex gives only 1 January of a year, that day is a placeholder;
- a National Assembly law, by the promulgation date in its PDF's file name;
- git cannot store dates before 1970, so the 6 earlier commits are dated from 1970-01-01, one second apart, with the real day in `In-force:`. Ask for a date with `tools/on.py`, not `git log --before`.

Each entry is credited to a key naming its record, with an e-mail address that cannot exist: a treaty action to the treaty (`treaty-932@wipo-int.invalid`), catalogue entries to their day (`Catalogue entries of 2009-04-22`); these are not laws. The first UN treaty action and the legal-system page are credited to the publishers. The committer is always Lexifina.

## How it is checked

- `tools/check_repo.py` reads every version back from git on the day it took effect and on the day before, and both must match the corpus the history was built from; it also checks that every commit's trailers parse, that there are no merge commits and that no commit is dated in the future.
- `tools/build.py` writes the history from that corpus in one pass, and the same corpus always gives the same commit hashes. The corpus is not in the repository; [`data/corpus.sha256`](data/corpus.sha256) gives its hash.
- [`REPRODUCE.md`](REPRODUCE.md), written at the build on 2026-10-30, records the checks as not yet run for that build and no second build compared.
- [vulnerabilities/](vulnerabilities/): possible drafting mistakes in this law, found by global-law's detectors and checked by hand. Not run yet.

## What it does not show

- **Any law or treaty text.** The official online copies of the Constitution and statutes (presidence.gov.bi, assemblee.bi) are image scans with no text layer, and no official copy with text was found. The 2018 Constitution and the 2017 Penal Code come next, from an official copy with text or from the official scans.
- **The Constitution in force.** The record names the 2005 Post-transition Interim Constitution, as WIPO Lex does; the 2018 Constitution is not in it.
- **Titles of the National Assembly's laws.** The 192 entries of 2003-2012 carry a number, a date and a link only; the laws posted there from 2013 on are not listed.
- **Treaties outside the two lists.** WIPO Lex lists only the treaties it tracks, and the UN list covers the 78 status pages read.

## Sources

| Source | Kind | Past versions | Notes |
| --- | --- | --- | --- |
| [WIPO Lex](https://www.wipo.int/wipolex/en/members/profile/BI) (World Intellectual Property Organization) | Catalogue of laws; treaty actions; the constitution's dates | no, one record per law or treaty | Title, subject, dates and link; no text |
| [Assemblée nationale du Burundi](https://assemblee.bi/) | Laws of 2003-2012, as PDFs | no | Number and promulgation date from each file name; the PDFs are image scans |
| [UN Treaty Collection](https://treaties.un.org/) | Multilateral treaties deposited with the UN Secretary-General | each action by Burundi | Burundi's signature, ratification, accession and other action dates |
| [Wikidata](https://www.wikidata.org/) | Legal system: legislature, courts, official languages | no | Open facts |

## Licence

See [`LICENSE`](LICENSE). Only facts are copied (titles, numbers, dates, links), and no text of any law or treaty: WIPO Lex content is published under CC BY 4.0 and credited to WIPO, which does not endorse this repository; Wikidata's facts are CC0. The history, commit messages, tables and tools are CC0 1.0.

No AI model wrote, translated or corrected legal text, and none runs when the history is built; the scripts were written by an AI model (see [`REPRODUCE.md`](REPRODUCE.md)).

## Visualisations

- [visualisations/](visualisations/): charts drawn from this repository. Not drawn yet.

## More

From [lexifina/global-law](https://github.com/lexifina/global-law):

- [FEATURES.md](https://github.com/lexifina/global-law/blob/main/FEATURES.md): every feature, and what every corpus must support (`git blame`, `law.py`, the MCP tools)
- [FAQ.md](https://github.com/lexifina/global-law/blob/main/FAQ.md): questions and answers · [CONTRIBUTING.md](https://github.com/lexifina/global-law/blob/main/CONTRIBUTING.md): proposing changes · [MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md): the MCP server · [REPRODUCE.md](https://github.com/lexifina/global-law/blob/main/REPRODUCE.md): how it was built · [CHANGELOG.md](https://github.com/lexifina/global-law/blob/main/CHANGELOG.md)
- [FRESHNESS.md](https://github.com/lexifina/global-law/blob/main/FRESHNESS.md): how current each corpus is · [Monitoring](https://github.com/lexifina/global-law/tree/main/monitoring): whether updates are running · [WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md): how each official source is watched for changes
- [performance/](https://github.com/lexifina/global-law/tree/main/performance): how fast the tools are, measured
- [visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations): charts and bridges across the world's law
- [Vulnerabilities](https://github.com/lexifina/global-law/tree/main/vulnerabilities): mistakes in legislation as published
