# Reproducing burundi-law

## Law text from the Bulletin Officiel du Burundi (build of 26 November 2026 onwards)

- Source: the BOB issue PDFs on https://amategeko.gov.bi (Ministry of Justice). The list of issues comes from the portal's RSS feed (`/feed/?post_type=bob`); each issue's PDF from its attachment page.
- Requests: at most 5 in flight to the portal, back-off on 429/5xx, every answer cached by the SHA-256 of its URL.
- Text: the PDF text layer read with PyMuPDF. Born-digital issues (Word, FrameMaker, Distiller and the like) are tagged `publisher PDF text layer (born-digital)`. Scanned issues that carry the publisher's OCR layer (Paper Capture, scanner metadata or full-page images) are taken as that layer reads them and tagged `publisher OCR (known reading errors)`; pages where fewer than half the tokens read as words are skipped, and a mixed-case heading counts only when an enacting formula (Le Président de la République, Vu, Décrète, Arrête, ...) follows it. Scans with no text layer are left out. No OCR is run by us.
- Publisher-OCR pages skipped as unusable: 625 pages in 180 issues.
- Split: each act starts at an upper-case heading `<KIND> N°<number> DU <date>`; the title is the upper-case lines after it; articles start at `Article N` / `Art. N`; text before the first article is `preambule.md`. Lines of the printed columns are joined into paragraphs. The issue's table of contents and its *Divers* part are left out.
- Paths: see STRUCTURE.md. Commits: one per act, 12:00 Africa/Bujumbura on the act's date (UTC+2).
- Status at this write: 964 PDFs parsed, 8174 acts committed (ordonnance ministerielle: 4038, decret: 2665, ordonnance: 926, loi: 287, ordonnance ministerielle conjointe: 126, decret loi: 34, arrete ministeriel: 26, ordonnance conjointe: 22, loi organique: 19, decision: 15, arrete: 12, reglement: 2, arrete loi: 2), 142 held.

### Held

| Reason | Acts |
| --- | ---: |
| date not read | 116 |
| no text | 26 |

- "date not read": the heading's date could not be read, is impossible, or is more than three years from the issue's year (usually an earlier act quoted or annexed inside a later one).
- "no text": a heading with no article and almost no text after it (often the act is printed only in Kirundi, or the heading is a cross-reference).

Scanned BOB issues from which no act was read (no text layer, or OCR text with no readable act heading) (483):

BOB No1/1970, BOB No1/1971, BOB No1/1972, BOB No1/1974, BOB No1/1975, BOB No1/1977, BOB No1/1979, BOB No1/1981, BOB No1/1984, BOB No1/1985, BOB No1/1986, BOB No1/1987, BOB No1/1989, BOB No1/1991, BOB No1/1994, BOB No1/1995, BOB No1/1996, BOB No1/1997, BOB No1/1998, BOB No1/1999, BOB No1/2002, BOB No1/2003, BOB No1/2004, BOB No1/2005, BOB No1/2006, BOB No10/1964, BOB No10/1971, BOB No10/1972, BOB No10/1973, BOB No10/1974, BOB No10/1975, BOB No10/1977, BOB No10/1979, BOB No10/1980, BOB No10/1985, BOB No10/1988, BOB No10/1989, BOB No10/1991, BOB No10/1992, BOB No10/1993, BOB No10/1995, BOB No10/1996, BOB No10/1997, BOB No10/1999, BOB No10/2001, BOB No10/2003, BOB No10/2005, BOB No10/2006, BOB No10/2007, BOB No10BIS/2001, BOB No10BIS/2003, BOB No10BIS/2004, BOB No10BIS/2005, BOB No10BIS/2006, BOB No10BIS/2007, BOB No10a12/1983, BOB No10a12/1984, BOB No10a12/1986, BOB No10a12/1986bis, BOB No10bis/1979, BOB No10bis/1999, BOB No10bis1/1993, BOB No10bis4/1993, BOB No11/1962, BOB No11/1965, BOB No11/1970, BOB No11/1971, BOB No11/1973, BOB No11/1974, BOB No11/1975, BOB No11/1978, BOB No11/1979, BOB No11/1980, BOB No11/1985, BOB No11/1987, BOB No11/1988, BOB No11/1989, BOB No11/1991, BOB No11/1992, BOB No11/1993, BOB No11/1994, BOB No11/1995, BOB No11/1996, BOB No11/1998, BOB No11/1999, BOB No11/2000, BOB No11/2003, BOB No11/2004, BOB No11/2005, BOB No11/2006, BOB No11/2007, BOB No11BIS/2003, BOB No11BIS/2004, BOB No11BIS/2007, BOB No11TER/2006, BOB No11bis/1965, BOB No11bis/1966, BOB No11bis/1977, BOB No11bis1/1993, BOB No11bis2/1993, BOB No11bis3/1993, BOB No12/1965, BOB No12/1966, BOB No12/1971, BOB No12/1972, BOB No12/1973, BOB No12/1974, BOB No12/1975, BOB No12/1977, BOB No12/1978, BOB No12/1979, BOB No12/1985, BOB No12/1987, BOB No12/1988, BOB No12/1989, BOB No12/1991, BOB No12/1992, BOB No12/1993, BOB No12/1994, BOB No12/1995, BOB No12/1996, BOB No12/1997, BOB No12/1998, BOB No12/2000, BOB No12/2003, BOB No12/2004, BOB No12/2008, BOB No12BIS/2003, BOB No12BIS/2004, BOB No12BIS/2006, BOB No12BIS/2007, BOB No12BIS/2007, BOB No12QUATER/2000, BOB No12TER/2006, BOB No12TER/2007, BOB No12TER1/2003, BOB No12TER2/2004, BOB No12TER3/2004, BOB No12TER4/2004, BOB No12bis/1972, BOB No12bis/1996, BOB No12bis/1998, BOB No12bis1/1993, BOB No12bis2/1993, BOB No12bis3/1993, BOB No12quater/1995, BOB No12ter/1995, BOB No1BIS/2000, BOB No1BIS/2003, BOB No1BIS/2006, BOB No1BIS/2007, BOB No1a2/1976, BOB No1a2/1982, BOB No1a3/1983, BOB No1a3/1988, BOB No1bis/1963, BOB No1bis/1964, BOB No1bis/1972, BOB No1bis/1973, BOB No1bis/1995, BOB No1ter/1972, BOB No1ter/2007, BOB No2/1962, BOB No2/1971, BOB No2/1972, BOB No2/1974, BOB No2/1975, BOB No2/1977, BOB No2/1978, BOB No2/1979, BOB No2/1980, BOB No2/1981, BOB No2/1984, BOB No2/1985, BOB No2/1986, BOB No2/1987, BOB No2/1989, BOB No2/1991, BOB No2/1992, BOB No2/1993, BOB No2/1994, BOB No2/1995, BOB No2/1997, BOB No2/1998, BOB No2/1999, BOB No2/2000, BOB No2/2003, BOB No2/2005, BOB No2/2006, BOB No2/2007, BOB No2BIS/2005, BOB No2BIS/2006, BOB No2BIS/2007, BOB No2TER/2005, BOB No2TER/2007, BOB No2a6/1973, BOB No2bis/2016, BOB No2bis/2016, BOB No3/1964, BOB No3/1965, BOB No3/1971, BOB No3/1972, BOB No3/1974, BOB No3/1975, BOB No3/1976, BOB No3/1977, BOB No3/1978, BOB No3/1979, BOB No3/1980, BOB No3/1981, BOB No3/1985, BOB No3/1986, BOB No3/1987, BOB No3/1989, BOB No3/1991, BOB No3/1992, BOB No3/1993, BOB No3/1994, BOB No3/1996, BOB No3/1997, BOB No3/1999, BOB No3/2000, BOB No3/2003, BOB No3/2004, BOB No3/2007, BOB No3BIS/2003, BOB No3BIS/2004, BOB No3BIS/2005, BOB No3BIS/2007, BOB No3QUATER/2005, BOB No3TER/2005, BOB No3TER/2006, BOB No3TER/2007, BOB No3bis/1965, BOB No3bis/1981, BOB No4/1962, BOB No4/1965, BOB No4/1971, BOB No4/1972, BOB No4/1974, BOB No4/1975, BOB No4/1977, BOB No4/1978, BOB No4/1979, BOB No4/1980, BOB No4/1981, BOB No4/1984, BOB No4/1986, BOB No4/1987, BOB No4/1988, BOB No4/1989, BOB No4/1991, BOB No4/1994, BOB No4/1995, BOB No4/1996, BOB No4/1997, BOB No4/1998, BOB No4/1999, BOB No4/2000, BOB No4/2001, BOB No4/2002, BOB No4/2003, BOB No4/2004, BOB No4/2005, BOB No4/2006, BOB No4/2007, BOB No4BIS/2001, BOB No4BIS/2003, BOB No4BIS/2005, BOB No4BIS/2006, BOB No4TER/2005, BOB No4TER/2006, BOB No4TER/2007, BOB No4bis/1965, BOB No4bis/1966, BOB No4bis/1971, BOB No4bis/1972, BOB No4bis/1988, BOB No5/1963, BOB No5/1971, BOB No5/1972, BOB No5/1974, BOB No5/1975, BOB No5/1978, BOB No5/1979, BOB No5/1980, BOB No5/1981, BOB No5/1984, BOB No5/1985, BOB No5/1986, BOB No5/1988, BOB No5/1989, BOB No5/1990, BOB No5/1991, BOB No5/1992, BOB No5/1994, BOB No5/1995, BOB No5/1997, BOB No5/1998, BOB No5/1999, BOB No5/2000, BOB No5/2001, BOB No5/2003, BOB No5/2004, BOB No5/2005, BOB No5BIS 4/2005, BOB No5BIS/2003, BOB No5BIS/2005, BOB No5BIS/2006, BOB No5BIS/2006, BOB No5BIS/2007, BOB No5BIS1/2005, BOB No5BIS2/2005, BOB No5BIS3/2005, BOB No5TER/2006, BOB No5TER/2007, BOB No5bis/1965, BOB No5bis/1971, BOB No5bis/1972, BOB No5ter/1972, BOB No6/1966, BOB No6/1967, BOB No6/1971, BOB No6/1972, BOB No6/1974, BOB No6/1977, BOB No6/1978, BOB No6/1979, BOB No6/1980, BOB No6/1981, BOB No6/1985, BOB No6/1986, BOB No6/1988, BOB No6/1989, BOB No6/1992, BOB No6/1994, BOB No6/1995, BOB No6/1997, BOB No6/1998, BOB No6/1999, BOB No6/2000, BOB No6/2001, BOB No6/2003, BOB No6/2004, BOB No6/2005, BOB No6/2007, BOB No6/2018, BOB No6BIS/2001, BOB No6BIS/2003, BOB No6BIS/2005, BOB No6BIS/2006, BOB No6BIS/2007, BOB No6BIS1/2005, BOB No6BIS2/2005, BOB No6BIS3/2005, BOB No6BIS4/2005, BOB No6BIS5/2005, BOB No6TER/2001, BOB No6TER/2003, BOB No6TER/2006, BOB No6bis/1965, BOB No6bis/1972, BOB No6bis/1999, BOB No7/1962, BOB No7/1966, BOB No7/1971, BOB No7/1972, BOB No7/1973, BOB No7/1974, BOB No7/1975, BOB No7/1978, BOB No7/1979, BOB No7/1980, BOB No7/1981, BOB No7/1985, BOB No7/1987, BOB No7/1988, BOB No7/1989, BOB No7/1991, BOB No7/1992, BOB No7/1994, BOB No7/1995, BOB No7/1996, BOB No7/1998, BOB No7/1999, BOB No7/2000, BOB No7/2001, BOB No7/2003, BOB No7/2004, BOB No7/2005, BOB No7/2006, BOB No7/2007, BOB No7BIS/2001, BOB No7BIS/2003, BOB No7BIS/2005, BOB No7BIS/2006, BOB No7BIS/2007, BOB No7TER/2005, BOB No7TER/2006, BOB No7a8bis1977, BOB No7a9/1983, BOB No7bis/1971, BOB No8/1962, BOB No8/1964, BOB No8/1966, BOB No8/1971, BOB No8/1972, BOB No8/1973, BOB No8/1974, BOB No8/1975, BOB No8/1978, BOB No8/1979, BOB No8/1980, BOB No8/1981, BOB No8/1985, BOB No8/1988, BOB No8/1989, BOB No8/1991, BOB No8/1992, BOB No8/1994, BOB No8/1995, BOB No8/1996, BOB No8/1997, BOB No8/1998, BOB No8/1999, BOB No8/2000, BOB No8/2001, BOB No8/2003, BOB No8/2004, BOB No8/2006, BOB No8BIS/2000, BOB No8BIS/2001, BOB No8BIS/2003, BOB No8BIS/2004, BOB No8BIS/2006, BOB No8BIS/2007, BOB No8TER/2001, BOB No8TER/2007, BOB No8a10/1987, BOB No9/1966, BOB No9/1968, BOB No9/1971, BOB No9/1973, BOB No9/1974, BOB No9/1975, BOB No9/1977, BOB No9/1978, BOB No9/1979, BOB No9/1980, BOB No9/1985, BOB No9/1988, BOB No9/1989, BOB No9/1991, BOB No9/1992, BOB No9/1993, BOB No9/1994, BOB No9/1996, BOB No9/1998, BOB No9/1999, BOB No9/2001, BOB No9/2003, BOB No9/2004, BOB No9/2005, BOB No9/2006, BOB No9/2007, BOB No9BIS/2000, BOB No9BIS/2001, BOB No9BIS/2003, BOB No9BIS/2006, BOB No9BIS/2007, BOB No9TER/2001, BOB No9a12/1981, BOB No9bis/1962, BOB No9bis/1971, BOB N°6/2006, BOB_No1-1993, BOB_No10bis2-1993, BOB_No10bis3-1993, BOB_No4-1993, BOB_No5-1993, BOB_No6-1993, BOB_No7-1993, BOB_No8-1993

BOB issues listed on the portal with no PDF found on their attachment pages (167):

BOB No1/1962, BOB No1/1963, BOB No1/1965, BOB No1/1967, BOB No1/1967, BOB No1/1968, BOB No1/1969, BOB No1/1992, BOB No1/2009, BOB No1/2010, BOB No1/2012, BOB No1/2016, BOB No1/2017, BOB No1/2018, BOB No1/2018, BOB No10/1967, BOB No10/1968, BOB No10/1969, BOB No10/1970, BOB No10/2011, BOB No10/2012, BOB No10/2018, BOB No10/2019, BOB No10BIS/1969, BOB No10BIS/2017, BOB No10bis/2018, BOB No11/1967, BOB No11/1968, BOB No11/1969, BOB No11/2016, BOB No11BIS/1969, BOB No11BIS/1969, BOB No11bis/1970, BOB No11bis/2012, BOB No12/1967, BOB No12/1968, BOB No12/1969, BOB No12/1970, BOB No12/2016, BOB No12TER/2001, BOB No12TER/2015, BOB No12bis/1962, BOB No12bis/1998, BOB No12bis/2018, BOB No1BIS/1967, BOB No1BIS/1967, BOB No1BIS/2010, BOB No1BIS/2018, BOB No1bis/2018, BOB No1bis/2019, BOB No2/1967, BOB No2/1968, BOB No2/1969, BOB No2/1970, BOB No2/2012, BOB No2/2017, BOB No2/2018, BOB No2BIS/2008, BOB No2bis/1970, BOB No2bis/2012, BOB No2bis/2016, BOB No2bis/2017, BOB No2bis/2018, BOB No2ter/2016, BOB No3/1967, BOB No3/1968, BOB No3/1969, BOB No3/1970, BOB No3/2008, BOB No3/2010, BOB No3/2012, BOB No3/2016, BOB No3/2016, BOB No3/2017, BOB No3/2019, BOB No3bis/2011, BOB No3bis/2016, BOB No3bis/2018, BOB No3quater/2019, BOB No4/1967, BOB No4/1968, BOB No4/1969, BOB No4/1970, BOB No4/2011, BOB No4/2016, BOB No4/2016, BOB No4/2017, BOB No4/2019, BOB No4BIS/1969, BOB No4bis/2018, BOB No5/1967, BOB No5/1968, BOB No5/1969, BOB No5/1970, BOB No5/2006, BOB No5/2016, BOB No5/2016, BOB No5BIS/1968, BOB No5bis/1970, BOB No5bis/2011, BOB No5bis/2017, BOB No5quater/2018, BOB No5quater/2019, BOB No6/1967, BOB No6/1968, BOB No6/1969, BOB No6/1970, BOB No6/2008, BOB No6/2012, BOB No6/2016, BOB No6/2017, BOB No6BIS/1967, BOB No6BIS/2015, BOB No6BIS/2017, BOB No7/1967, BOB No7/1968, BOB No7/1969, BOB No7/1970, BOB No7/2008, BOB No7/2015, BOB No7/2016, BOB No7/2017, BOB No7bis/2017, BOB No8/1967, BOB No8/1968, BOB No8/1969, BOB No8/1970, BOB No8/2007, BOB No8/2010, BOB No8/2012, BOB No8/2016, BOB No8/2017, BOB No8BIS/1969, BOB No8BIS/2010, BOB No8TER/2010, BOB No8bis/2016, BOB No8bis/2017, BOB No9/1967, BOB No9/1968, BOB No9/1969, BOB No9/1970, BOB No9/2000, BOB No9/2016, BOB No9bis/2017, BOB No9ter/2015, BOB N°1-2020, BOB N°11/2023, BOB N°12/2022, BOB N°1bis-2020, BOB N°1ter-2020, BOB N°2-2020, BOB N°2/2022, BOB N°3/2020, BOB N°3/2023, BOB N°3Ter/2023, BOB N°5bis/2022, BOB N°6bis/2021, BOB N°7/2023, BOB N°7bis/2021, BOB N°7bis/2023, BOB N°8/2021, BOB N°8/2022, BOB N°8/2023, BOB N°8bis/2023, BOB N°8ter/2023, BOB N°9bis/2022, Bob No3bis/2020

- The 2018 Constitution: BOB n°6/2018 and the copy on presidence.gov.bi are image scans with no text layer; not included.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction. No model wrote, translated or corrected legal text, and no model runs at build time.

## Earlier build
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
