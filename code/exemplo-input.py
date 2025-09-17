"""
Recebendo dados do usuário
"""
# Entrada de dados
nome = input('Qual o teu nome? ') # Input -> Entrada

# Exemplo de print antigo 2.x
#print('Seja bem-vindo(a) %s' % nome)

# Exemplo de print moderno
#print('Seja bem-vindo(a) {0}'.format(nome))


print(f'Seja bem vindo, {nome.title()}!')

idade = int(input('Qual a tua idade? '))

# Processamento

# Saída de dados
# Exemplo de print antigo:
#print('A %s tem %s anos' % (nome, idade))
#print(' A {0} tem {1} anos'.format(nome, idade))

# Exemplo de print mais atual
print(f'A {nome.title()} tem {idade} anos')
