from collections import deque
import random
import time
links = deque(['https://www.xss1.com'])

"""
Listas são ótimas para transportar valores.

 [HEAD] -> [NODE] -> [NODE]-> [NODE] -> NULL

 São otímas para deletar e inserir valores novos.
 São mais pesadas por contas de seus nós.

 Podem funcionar como Pilhas ou Filas
"""

a = 2
while True:

    linkss = f'https://www.xss{a}.com'
    links.appendleft(linkss)
    a +=1

    if a == 5000:
        break

for i in range(0,len(links)):

    print(f'O item {links.popleft()} foi deletado')