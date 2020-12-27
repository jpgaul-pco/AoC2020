import re

datafile = 'input.txt'

with open(datafile) as fh:
    txt = fh.read()
    rulestxt, datatxt = txt.split('\n\n')

data = [y for y in (x.strip() for x in datatxt.split('\n')) if y]

def make_rules(lines):
    D = {}
    for line in lines:
        if not line:
            continue
        k, v = line.strip().split(':')
        v = v.replace('"', '')
        if '|' in v:
            v = '(?: ' + v + ' )'
        D[k] = v.split()
    return D

rules = make_rules(rulestxt.split('\n'))

def rules_to_re(rules):
    L = rules['0'].copy()
    while any(x.isdigit() for x in L):
        i, k = next((i,x) for (i, x) in enumerate(L) if x.isdigit())
        L[i:i+1] = rules[k].copy()
    L.insert(0, '^')
    L.append('$')
    return re.compile(''.join(L))

rules_re_1 = rules_to_re(rules)

print(bool(rules_re_1.match('abbabaaaababbbbbababaaba')))