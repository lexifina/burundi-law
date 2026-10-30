"""Burundi: dated list of assemblee.bi law PDFs from the file names (number and date). Writes .tmp/laws_bi.json."""
import json, re, unicodedata
from urllib.parse import quote
M = {'janvier':1,'fevrier':2,'fevr':2,'mars':3,'avril':4,'avri':4,'mai':5,'mail':5,'juin':6,'juillet':7,'aout':8,'aoutt':8,'septembre':9,'octobre':10,'novembre':11,'decembre':12}
MANUAL = {'N°1_3_09-avri_l2003': (3, '2003-04-09'), 'loi_n1-19_du_26_mai-2': (19, '2006-05-26')}  # typos in the file names; 1/19 sits between 1/17 (29 Apr) and 1/20 (26 May 2006)
def parse(stem):
    s = unicodedata.normalize('NFKD', stem.lower()).encode('ascii', 'ignore').decode()
    s = s.replace('n?', 'n').replace('_', '-').replace(' ', '-')
    s = re.sub(r'^loi-?', '', s); s = re.sub(r'^n-?', '', s)
    s = re.sub(r'^1-(?=\d)', '', s) if re.match(r'^1-\d+-', s) else s
    m = re.match(r'^0*(\d+)-(?:du-?)?(1er|\d{1,2})-?(?:du-)?([a-z]+?)(?:-|l)?(\d{4})', s)
    if not m: return None
    num, d, mon, y = m.groups()
    d = 1 if d == '1er' else int(d)
    mon = M.get(mon)
    if not mon: return None
    return int(num), f'{int(y):04d}-{mon:02d}-{d:02d}'
if __name__ == '__main__':
    items = json.load(open('.tmp/media.json', encoding='utf8'))
    out, fail, seen = [], [], {}
    for i in items:
        u = i['source_url']; stem = u.rsplit('/', 1)[1][:-4]
        if not re.search(r'(?:^|[^a-z])(?:loi|n)', stem.lower()): continue
        r = MANUAL.get(stem) or parse(stem)
        if not r:
            fail.append(stem); continue
        num, date = r
        if not ('2003' <= date[:4] <= '2012'): continue
        k = (num, date)
        if k in seen: continue
        seen[k] = 1
        out.append({'number': num, 'date': date, 'url': quote(u, safe=':/%'), 'file': u.rsplit('/', 1)[1], 'uploaded': i['date'][:10]})
    out.sort(key=lambda x: (x['date'], x['number']))
    json.dump(out, open('.tmp/laws_bi.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    print(len(out), 'parsed;', len([o for o in out if o['date'] < '2013']), 'in 2003-2012')
    print('unparsed:', fail)
