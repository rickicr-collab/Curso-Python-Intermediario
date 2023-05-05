# #############Nivel Intermediario Estrutura de repetição WHILE##################
#trabalhando com estrutura de repetição while
# opção 01 para utilização de while
c = 1
while c < 11:
  print(c)
  c = c + 1
print('FIm!!!') 
#-------------------------------------------------------------------
# Opção 02 para utilização da condição de repetição while 
n = 1
while n != 0:
  n = int(input('digite um valor:'))
print('FIm!')
#--------------------------------------------------------------------
# Opção 03 para utilização da condição de repetição while
r = 'S'
while r == 'S':
  n = int(input('Digite um valor :'))
  r = str(input('Quer continuar [S/N] : ')).upper()
print('FIm!')
#---------------------------------------------------------------------
#opção 04 para utilização da condição de repetição while
num  = 1
par = 0
impar = 0
while num != 0:
  num = int(input('Digite um valor:'))
  if num != 0:
    if num % 2 == 0:
      par += 1
    else:
      impar += 1     
print('OS numeros pares digitados foram {}'.format(par))
print('os numeros impares digitados foram {}'.format(impar))
print('ACABOU!!')