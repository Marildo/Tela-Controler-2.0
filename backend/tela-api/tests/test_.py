from unicodedata import normalize

source = 'Usuários'
target = normalize('NFKD', source).encode('ASCII','ignore').decode('ASCII')
print(target)