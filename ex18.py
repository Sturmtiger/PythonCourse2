#   #1
# with open('inp(ex18).txt', 'r') as r, open('out(ex18).txt', 'w') as w:
#     w.write('\n'.join(reversed(r.read().splitlines())))


#   #2
with open('dataset\\inp(ex18).txt', 'r') as r, open('dataset\\out(ex18).txt', 'w') as w:
    [w.write(f'{line}\n') for line in reversed([i.rstrip() for i in r])]