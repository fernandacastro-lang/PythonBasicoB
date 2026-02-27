from enemigo import *
from zombie import *
from hogro import *

zombie = zombie(10, 1)
ogro = ogro(20, 3)

print(f"{zombie.get_tipo_enemigo()}tiene{zombie.puntos_energia} de energia y puede hacer ataques de {zombie}")
print(f"{zombie.habla()}")
print(f"{ogro.get_tipo_enemigo()}tiene{ogro.puntos_energia} de energia y puede hacer ataques de {ogro.ataque}")
print(f"{ogro.habla()}")