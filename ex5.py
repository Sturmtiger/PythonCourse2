def add(namespace, var):
    nss[namespace]['vars'].append(var)
def create(namespace, parent):
    nss[namespace] = {'parent': parent, 'vars': []}
def get(namespace, var):
    if var in nss[namespace]['vars']:
        print (namespace)
        return namespace
    if nss[namespace]['parent'] == None:
        print(None)
        return
    get(nss[namespace]['parent'], var)
nss = {'global': {'parent': None, 'vars': []}}
for i in range(int(input())):
    query = input().split()
    if query[0] == 'add':
        add(query[1], query[2])
    if query[0] == 'create':
        create(query[1], query[2])
    if query[0] == 'get':
        get(query[1], query[2])