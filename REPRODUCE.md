# How this repository was made (Burundi)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| WIPO Lex member profile | <https://www.wipo.int/wipolex/en/members/profile/BI> | 2026-10-30 | WIPO content: CC BY 4.0 (https://www.wipo.int/web/terms-of-use); only facts copied |
| Wikidata | <https://www.wikidata.org/> | 2026-10-30 | CC0 |
| Assemblée nationale du Burundi, media index | <https://assemblee.bi/> | 2026-10-30 | Facts only (law number, date, link); no text copied. |
| UN Treaty Collection (MTDSG status pages) | <https://treaties.un.org/> | 2026-10-29 | Facts only (treaty action, date, depositary); no text copied |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `treaties` | Treaty actions of Burundi recorded by WIPO Lex (facts only; no treaty text) | 38 | 1968-01-19 to 2025-06-09 |
| `catalogue` | Catalogue of laws of Burundi recorded by WIPO Lex (title, date, link only; no law text) | 123 | 2003-03-28 to 2015-01-16 |
| `legal-system` | Legal system of Burundi: open facts (Wikidata, WIPO Lex) | 1 | 2026-10-30 to 2026-10-30 |
| `un-treaties` | Treaty actions of Burundi on multilateral treaties deposited with the UN Secretary-General (UN Treaty Collection; no treaty text) | 46 | 1962-10-22 to 2018-01-17 |

The build made 234 commits:

| Commits | Kind |
| ---: | --- |
| 4 | first version of an act |
| 230 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-30.
- 6 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 233 laws in the record.
- 439 tags.

## Dates

Each commit is dated at noon (Africa/Bujumbura) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: This repository holds metadata only, no law text. Each treaty is dated by the party's own action (ratification, accession or similar instrument; failing that its entry into force for the party, then signature); each catalogue entry by the date WIPO Lex records for the law. https://www.wipo.int/wipolex/en/members/profile/BI

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `660fcd344f9858930fbd468dac8201734cae1dc3d14037473d8216d523301e3d` (818907 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3e59cb6f05eccb94a9ec14431a7f6781221e83ef`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- Metadata only, no law text: the official online copies of Burundi's Constitution and statutes (presidence.gov.bi, assemblee.bi) are image scans with no text layer, and OCR was not available; no text-layer official copy was found.
- Treaty versions are dated by the party's instrument date (ratification, accession or similar), else its entry-into-force date for the party, else signature; treaties with none of these are left out.
- Catalogue entries use the date WIPO Lex records (promulgation, entry into force, commencement or adoption, in that order); WIPO Lex gives some laws only "January 1" of a year, which is a placeholder, not a known date; a law with no date is added on the retrieval date.
- No treaty or law text is included: titles, dates, administering organisation and links only.
- Catalogue extended with the laws of 2003-2012 listed as PDFs on assemblee.bi (WordPress media index). Number and promulgation date are read from the file names; two typos corrected by hand (1/3 of 9 April 2003; 1/19 of 26 May 2006); duplicate uploads of one number and date counted once. The PDFs are image scans, so titles and gazette citations are not recorded and nothing was OCR'd.
- UN Treaty Collection: 48 multilateral treaties deposited with the UN Secretary-General, with the state's signature, ratification, accession, succession, acceptance or approval dates. Facts only; one version per action date, with the first version credited to the action. Treaties outside the 78 status pages read are not listed.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none
