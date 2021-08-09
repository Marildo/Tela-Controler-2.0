print(eval('4 * 6'))

from utils.cnpj_util import Encoder

enco = Encoder(operation='-', value='33')
v = 194
print(eval(f'{v}{enco.operation}{enco.value}'))