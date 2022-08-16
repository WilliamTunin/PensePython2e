q = int(input('Digite a quntidade de livros '))
n = float(input('Digite o valor do livro R$'))
d = n * 40 / 100
print('Valor do livro com desconto é R${:.2f}'.format(n-d))
f = (q-1) * 0.75 + 3
print('valor do frete para {} é R${:.2f}'.format(q, f))
v = (q*(n-d))+f
print('O valor de atacado para {} é R${:.2F}'.format(q, v))