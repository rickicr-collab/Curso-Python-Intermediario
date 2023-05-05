
# Pythron INtermerdiario Estrutura de repetição For
# primeiro exemplo usando o laço FOR 
for c in range(0, 6): # criando um laça for de uma variavel qualquer em intervalo(range) exemplo 0, 6
  print('oi') # ele vai printar a palavra ou no intervalo sugerindo na linha anterior 
print('FIM!!') # aqui ele vai printar a palavra fim ao finalizar o laço no intervalo de valor 6

#--------------------------------------------------
# 2 opção usando laço for 
for c in range(6, 0, -1): # criando um laça for de uma variavel qualquer em intervalo(range) exemplo 0, 6 mais com intervalo -1  em que ele executa a operação na direção contraria do laço
  print(c) # imprimir o conteudo da variavel c do laço for informado anteriomento 
print('FIM!!') # imprimir a palavra fim ao final do laço criavel
# -------------------------------------------------------
# 3 opção usando laço for
for c in range(0, 7, 2): # criando um laço for de uma variavel qualquer em intervalo(range) exemplo 0, 7 , 2 - ele irá o laço normalmente mais pulando dois numeros para cada repetição 
  print(c) # imprimir o valor da variavel qualquer declarada no laço for 
print('FIM!!') # imprimir a palavra
# --------------------------------------------------------------
# 04 opção usando laço for 
n = int(input('Digite um numero:')) # criando uma variavel que recebe função input com valor determinado inserido no terminal
for c in range(0, n): # atribuido um lnço com intervalo de inicio 0 ao limite inserido na variavel n
  print(c)
print('FIM!!') 
#---------------------------------------------------------------
# -5 opção o laço de repetição for 
i = int(input('Inicio:'))
f = int(input('Fim:'))
p = int(input('Passo:'))
for c in range(0, f+1, p):
  print(c)
print('FIM!!')
#-----------------------------------------------------------
# 06 opção utilizando o laço de repetição for
s = 0 # atribuido o valor 0 a variavel s
for c in range(0, 4): # criado um laço for de range ( 0, 4)
  num = int(input('digite um numero: ')) # criado uma variavel num que recebeu uma função input que está dentro da condição do for se repetindo o numero de intervalo determinado
  s = s + num # dentro do laço for realiza a soma dos valores atribuidos a variavel num dentro do laço for e mostra na tela 
print('O somatório dos valores foi {}'.format(s))
