import base64

from brutils import cnpj

a = 11188926000179
sad = bytes(str(a * 33).encode('utf-8'))

print(sad)

s = base64.b64encode(sad)

print(s)

c = base64.b64decode(s)
d = c.decode('utf-8')

r = int(int(d) / 33)

print(r, r == a)


from utils import CNPJUtil

x = CNPJUtil.encode('11.1l88.926/0001-79')

print('x ::',x)