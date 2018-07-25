#   #1
# def add(namespace, var):
#     nss[namespace]['vars'].append(var)
# def create(namespace, parent):
#     nss[namespace] = {'parent': parent, 'vars': []}
# def get(namespace, var):
#     if var in nss[namespace]['vars']:
#         print(namespace)
#         return namespace
#     if nss[namespace]['parent'] == None:
#         print(None)
#         return None
#     get(nss[namespace]['parent'], var)
# nss = {'global': {'parent': None, 'vars': []}}
# for i in range(int(input())):
#     query = input().split()
#     if query[0] == 'add':
#         add(query[1], query[2])
#     if query[0] == 'create':
#         create(query[1], query[2])
#     if query[0] == 'get':
#         get(query[1], query[2])

#   #2
nss = dict({'global': [None]})

def create(namespace, parent):
    nss.update({namespace: [parent]})

def add(namespace, var):
    nss[namespace].append(var)

def get(namespace, var):
    while namespace != None and var not in nss[namespace][1:]:
        namespace = nss[namespace][0]
    print(namespace)

functions = {'create': create, 'add': add, 'get': get}
for i in range(int(input())):
    query = input().split()
    functions[query[0]](query[1], query[2])
