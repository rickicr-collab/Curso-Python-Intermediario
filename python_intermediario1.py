#------ nivel Intermediario------------#
# condicoes Aninhadas #
# condicionais aninhadas #
nome = str(input('Qual é o seu nome :')).capitalize()
if nome == 'Ricardo': # função obrigatoria dentro da função que tambem não possui limites 
  print('que nome lindo demais ! ')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Anna': #função opcional dentro de uma função mais não ha limites para se terem 
  print('Seu nome é bem popular!')
elif nome in 'Ana Claudia Jessica Juliana':
  print('Belo nome feminino')
else: # condiçõa opcional mais so podento conter apenas uma dentro de uma funcão ou classe 
  print('Seu nome é bem normal')
print('Tenha um bom dia , {} ! '.format(nome))
