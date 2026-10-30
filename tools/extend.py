"""Burundi: add the assemblee.bi laws of 2003-2012 (number and date from file names) to the catalogue act."""
import json, sys, hashlib
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'world-law'))
from cat_lib import merge_entries
MON = ['janvier','fevrier','mars','avril','mai','juin','juillet','aout','septembre','octobre','novembre','decembre']
c = json.load(open(HERE / 'corpus.json', encoding='utf8'))
laws = json.load(open(HERE / '.tmp/laws_bi.json', encoding='utf8'))
raw = (HERE / '.tmp/media.json').read_bytes()
sha = hashlib.sha256(raw).hexdigest()
entries = []
for l in laws:
    y, m, d = l['date'].split('-')
    dfr = ('1er' if int(d) == 1 else str(int(d))) + ' ' + MON[int(m) - 1] + ' ' + y
    label = f"Loi n° 1/{l['number']:02d} du {dfr}"
    text = (f"# {label}\nNumber: 1/{l['number']}\nDate (promulgation, from the file name): {l['date']}\n"
            f"Publisher of the index: Assemblée nationale du Burundi\nGazette citation: not given by the index\n"
            f"Title: not recorded (the PDF is an image scan with no text layer)\nRecord: {l['url']}\n")
    entries.append((l['date'], f"loi-{y}-{l['number']:03d}", label, text))
merge_entries(c, 'catalogue', entries, 'catalogue',
              'Catalogue entries dated by the promulgation date in the file name of the law on assemblee.bi; facts only, no law text.',
              'https://assemblee.bi/', sha, 'https://assemblee.bi/')
c['decisions'].append("Catalogue extended with the laws of 2003-2012 listed as PDFs on assemblee.bi (WordPress media index). Number and promulgation date are read from the file names; two typos corrected by hand (1/3 of 9 April 2003; 1/19 of 26 May 2006); duplicate uploads of one number and date counted once. The PDFs are image scans, so titles and gazette citations are not recorded and nothing was OCR'd.")
c['sources'].append({'name': 'Assemblée nationale du Burundi, media index', 'url': 'https://assemblee.bi/', 'retrieved': '2026-10-30',
                     'licence': 'Facts only (law number, date, link); no text copied. Site publishes no robots.txt (404).', 'notes': 'Public WordPress REST media listing; file names carry number and date.'})
json.dump(c, open(HERE / 'corpus.json', 'w', encoding='utf8', newline='\n'), ensure_ascii=False, indent=1)
print(len(entries), 'entries')
