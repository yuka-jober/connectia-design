# QA_체크리스트.md -> qa.html  (md가 단일 기준, 페이지는 여기서 생성)
import re, html, hashlib, io, os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'QA_체크리스트.md')
OUT = os.path.join(HERE, 'qa.html')

def inline(t):
    t = html.escape(t)
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank" rel="noopener">\1</a>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    return t

def item_id(text):
    return 'q' + hashlib.md5(text.encode('utf-8')).hexdigest()[:10]

def render(lines, out, ids):
    """블록 단위로 훑으면서 HTML을 쌓는다"""
    i = 0
    while i < len(lines):
        ln = lines[i]

        # 인용 박스 — 안에 체크 항목이 들어있기도 하다
        if ln.startswith('>'):
            block = []
            while i < len(lines) and lines[i].startswith('>'):
                block.append(re.sub(r'^>\s?', '', lines[i])); i += 1
            out.write('<div class="note">')
            render(block, out, ids)
            out.write('</div>\n')
            continue

        # 표
        if ln.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')]); i += 1
            body = [r for r in rows[1:] if not set(''.join(r)) <= set('-: ')]
            out.write('<div class="table-wrap"><table><thead><tr>')
            for c in rows[0]: out.write('<th>' + inline(c) + '</th>')
            out.write('</tr></thead><tbody>')
            for r in body:
                out.write('<tr>' + ''.join('<td>' + inline(c) + '</td>' for c in r) + '</tr>')
            out.write('</tbody></table></div>\n')
            continue

        # 체크 항목
        m = re.match(r'^- \[ \] (.+)$', ln)
        if m:
            out.write('<ul class="checks">')
            while i < len(lines):
                m = re.match(r'^- \[ \] (.+)$', lines[i])
                if not m: break
                text = m.group(1); cid = item_id(text)
                ids.append(cid)
                out.write(
                    '<li class="check" data-id="' + cid + '">'
                    '<button class="mark mark-pass" type="button" aria-label="통과" onclick="mark(this,\'pass\')">'
                    '<i data-lucide="check"></i></button>'
                    '<button class="mark mark-fail" type="button" aria-label="실패" onclick="mark(this,\'fail\')">'
                    '<i data-lucide="x"></i></button>'
                    '<span class="check-text">' + inline(text) + '</span>'
                    '</li>')
                i += 1
            out.write('</ul>\n')
            continue

        # 일반 목록
        m = re.match(r'^(\d+)\. (.+)$', ln)
        if m:
            out.write('<ol class="plain">')
            while i < len(lines):
                m = re.match(r'^(\d+)\. (.+)$', lines[i])
                if not m: break
                out.write('<li>' + inline(m.group(2)) + '</li>'); i += 1
            out.write('</ol>\n')
            continue

        if ln.startswith('### '):
            out.write('<h3>' + inline(ln[4:]) + '</h3>\n'); i += 1; continue
        if ln.startswith('---'):
            i += 1; continue
        if ln.strip() == '':
            i += 1; continue

        # 굵은 글씨만 있는 줄은 소제목으로 (1-1 · … )
        if re.fullmatch(r'\*\*[^*]+\*\*', ln.strip()):
            out.write('<h4>' + inline(ln.strip()[2:-2]) + '</h4>\n'); i += 1; continue

        para = []
        while i < len(lines) and lines[i].strip() and not re.match(r'^(#|\||>|- \[|\d+\. |---)', lines[i]):
            para.append(lines[i]); i += 1
        if para:
            out.write('<p>' + inline(' '.join(x.strip() for x in para)) + '</p>\n')

md = open(SRC, encoding='utf-8').read().split('\n')

title = md[0].lstrip('# ').strip()
lead_end = next(k for k, l in enumerate(md) if l.startswith('## '))
lead = [l for l in md[1:lead_end] if l.strip() and not l.startswith('---')]

# ## 로 구간 자르기
marks = [k for k, l in enumerate(md) if l.startswith('## ')] + [len(md)]
sections = [(md[marks[j]][3:].strip(), md[marks[j] + 1:marks[j + 1]]) for j in range(len(marks) - 1)]

body = io.StringIO(); nav = io.StringIO(); total = 0
for n, (head, lines) in enumerate(sections):
    sid = 'sec' + str(n)
    inner = io.StringIO(); ids = []
    render(lines, inner, ids)
    total += len(ids)
    body.write('<section class="part" id="' + sid + '" data-items="' + ','.join(ids) + '">'
               '<div class="part-head"><h2>' + inline(head) + '</h2>'
               '<span class="part-count" data-for="' + sid + '"></span></div>'
               + inner.getvalue() + '</section>\n')
    nav.write('<a class="nav-item" href="#' + sid + '"><span>' + inline(head) + '</span>'
              '<span class="nav-count" data-for="' + sid + '"></span></a>')

TPL = open(os.path.join(HERE, 'qa-template.html'), encoding='utf-8').read()
out = (TPL.replace('{{TITLE}}', html.escape(title))
          .replace('{{LEAD}}', ' '.join(inline(l) for l in lead))
          .replace('{{NAV}}', nav.getvalue())
          .replace('{{BODY}}', body.getvalue())
          .replace('{{TOTAL}}', str(total)))
open(OUT, 'w', encoding='utf-8').write(out)
print('items', total, '| sections', len(sections))
