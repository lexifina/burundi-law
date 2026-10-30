# Burundi: law history in git

The law of Burundi as a git history: one file per provision, one commit per law on the day it took effect, and the law that made each change as the commit's author. `git blame` names the law behind every paragraph; `git log` lists every change; picking a date gives the text in force that day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law).

**What is in it now (a first build, not complete)**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `treaties/` | Treaty actions of Burundi recorded by WIPO Lex (name, administering organisation, dates; no treaty text) | one per action date | From the earliest recorded action to the latest |
| `catalogue/` | Catalogue of laws of Burundi: WIPO Lex records (title, subject, date, link) and the 192 laws of 2003-2012 listed on assemblee.bi (number, promulgation date, link); no law text | one per recorded date | Dated by the date WIPO Lex or the assemblee.bi file name gives for each law |
| `un-treaties/` | Burundi's signature, ratification, accession or acceptance of 48 multilateral treaties deposited with the UN Secretary-General (UN Treaty Collection; no treaty text) | one per action date | From 1962 to the latest recorded action |
| `legal-system/` | Legal system of Burundi: constitution, legislature, courts, official languages (Wikidata, WIPO Lex) | 1 | Oldest version available, 30 October 2026 |

**Language.** English. This repository holds metadata only. (The laws themselves are in French.)

**Source.** Metadata only, no law text, because the official online copies of Burundi's Constitution and statutes (presidence.gov.bi, assemblee.bi) are image scans with no text layer, OCR was not available here, and no text-layer official copy was found. The copyright act (Loi n° 1/021 of 30 December 2005) is itself only a scan on assemblee.bi, so whether it excludes official texts could not be checked, and no third-party copy of a law is used. Treaty actions, the list of laws and the constitution date come from the WIPO Lex member profile (https://www.wipo.int/wipolex/en/members/profile/BI); open facts on the legal system come from Wikidata (CC0). The catalogue of 2003-2012 laws comes from the public media index of the National Assembly (https://assemblee.bi/): the law number and promulgation date are read from the PDF file names and the link points to the PDF. Those PDFs are image scans, so no title or gazette citation is recorded and nothing was OCR'd. Treaty actions in `un-treaties/` come from the UN Treaty Collection status pages (https://treaties.un.org/), facts only. All retrieved 30 October 2026.

## Dates

Each commit is dated at noon local time. A treaty is dated by the country's own action: its ratification, accession or similar instrument, else its entry into force for the country, else signature. A catalogue entry is dated by the date WIPO Lex records for the law (promulgation, entry into force, commencement or adoption); where WIPO Lex gives only 'January 1' of a year, that date is a placeholder, not a known date. A law with no recorded date is added on 30 October 2026, the retrieval date.

## How it is checked

Every version is read back from git on the day it took effect and on the day before (`tools/check_repo.py`) and must match `corpus.json`; results are in `REPRODUCE.md`.

## What "author" means

The author of a commit is the law that made the change, with an e-mail address that cannot exist (`<law key>@wipo-int.invalid`). Each treaty action or catalogue date is credited to a key that names the record (treaty-<WIPO id>, catalogue-<date>); these are not laws. The committer is always Lexifina.

## Limits

Metadata only: the Constitution, statutes and treaties are named, not reproduced. The treaty list is what WIPO Lex records and omits any treaty it does not track. The next step is a text-layer copy of the 2018 Constitution and the 2017 Penal Code from an official source, or OCR of the official scans (presidence.gov.bi, assemblee.bi), plus titles for the assemblee.bi laws (the 192 catalogue entries of 2003-2012 carry number, date and link only) and the laws posted there from 2013 on.
