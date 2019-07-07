# Importando função do arquivo function.py
from function import readMyFileAndReturnContentInArray, checkHeader

result1 = readMyFileAndReturnContentInArray("clientes.txt")
result2 = readMyFileAndReturnContentInArray("txtbonus.txt")

# Declarando e inicializando as variaveis
result =  []
r1     =  []
r2     =  []

'''
 Checando e definindo qual é o maior array
 para a partir dele poder realizar a verifcação dos
 valores da primeira coluna
'''
if len(result1) >= len(result2) :
    r1 = result1
    r2 = result2
else :
    r1 = result2
    r2 = result1

'''
 Iniciando o loop a partir do maior array, em seguida
 entrando no segundo array para checar
 se o valor da primeira coluna do array 01
 é igual ao valor da primeira coluna do array 02
'''
for r in r1:
    for y in r2:
        if r[0] == y[0] :
            s = int(r[1])+int(y[1])
            result.append(r[0] + " " + r[1] + " + " + y[1] + " = " + str(s))
'''            
 Aqui abrimos e criamos o arquivo ao mesmo 
 tempo caso não exista
'''
with open("DADOS.txt", 'w') as c:
    checkHeader("DADOS.txt")
    for r in result:
        print(r)
        c.write(r + "\n")



            
            
        