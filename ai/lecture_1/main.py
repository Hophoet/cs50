from logic import *

rain = Symbol('rain')
hagrid = Symbol('hagrid')
dumbledore = Symbol('dumbledore')

a = And(rain, hagrid)

print(a.formula())
