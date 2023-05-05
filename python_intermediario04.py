# Laços de repetição 
# interrompendo laços de repetição 
# ----- Exemplo 01 ----------#
cont = 0
while cont <= 10:
    print(cont, ' → ', end = ' ')
    cont += 1
print('Acabou')

# ---- Exemplo 02 ----------#
n = s = 0
while True:
    n =int(input('Digite um numero:'))
    if n == 999:
        break # utilizando o comando break para interromper o lação ao se digitar no terminal o valor 999 como condição do if saindo do loop e fechando o programa 
    s += n
print('A soma dos numeros será {}'.format(s))