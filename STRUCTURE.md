# Structure of burundi-law

The law text in this repository comes from the **Bulletin Officiel du Burundi (BOB)**, the official gazette, as published on the
Ministry of Justice's legal portal *Mémoire du Droit Burundais* (https://amategeko.gov.bi). Each act printed in a BOB issue
is one folder; each article is one file.

| Folder | What it holds | Path pattern | Example |
| --- | --- | --- | --- |
| `constitution/` | The Constitution in force (2018), one file per article | `constitution/article-NNN.md` | `constitution/article-001.md` |
| `codes/` | Codes enacted or recast as a whole (Code pénal, Code de procédure pénale, Code du travail, …); each new full text is a new version of the same folder | `codes/<code>/article-NNN.md` | `codes/code-penal/article-001.md` |
| `lois/` | Lois, lois organiques and lois constitutionnelles | `lois/<année>/<numéro>-<objet>/` | `lois/2023/1-23-ratification-par-la-republique-du-burundi-de-l/` |
| `decrets-lois/` | Décrets-lois and arrêtés-lois | `decrets-lois/<année>/<numéro>-<objet>/` | |
| `decrets/` | Décrets of the President | `decrets/<année>/<numéro>-<objet>/` | `decrets/2023/100-193-modalites-pratiques-de-levee-du-gel-d-avancement/` |
| `ordonnances/` | Ordonnances (ministérielles, conjointes), by ministry code (first part of the number) | `ordonnances/<année>/<ministère>/<numéro>-<objet>/` | `ordonnances/2023/610/610-1209-agrement-des-filieres-.../` |
| `arretes/`, `autres-actes/` | Arrêtés, décisions, règlements | `arretes/<année>/<numéro>-<objet>/` | |
| `catalogue/`, `treaties/`, `un-treaties/`, `legal-system/` | Earlier metadata (law titles, treaty actions, legal-system facts) | unchanged | |

Inside each act folder:

- `preambule.md`: the heading (kind, number, date), the title, the visas and the enacting formula;
- `article-NNN.md` (`article-001.md`, `article-012-bis.md`, …): one article each; the signature block stays with the last article.

No folder holds more than 1,000 entries: years split the acts, and ordonnances are further split by ministry.

## Commits

- One commit per act (one per version for codes), dated **12:00 Africa/Bujumbura** on the date of the act (signature or
  promulgation, as printed in its heading). Acts before 1970 carry the real date in the subject and the trailers (git
  cannot hold earlier dates).
- Trailers: `In-force` (the date used), `In-force-basis` (why; quotes the act's own entry-into-force clause where it has
  one, for example "entre en vigueur le jour de sa promulgation"), `Source` (BOB issue, page, PDF), `Text-source`.
- Author: the act itself (`Décret n°100/193 du 1er septembre 2023 <…@amategeko-gov-bi.invalid>`); committer Lexifina.

## Not included

- The *Divers* part of each BOB (court notices served on named private persons, company notices): not legislation.
- BOB issues that are scans: only issues whose PDF has the publisher's own text layer are used. Issues whose only text
  is the publisher's OCR (mostly before 2010) are listed in REPRODUCE.md and held for a later pass; we run no OCR.
