preço = float(input('Preço dos produtos: R$ '))
print('''Escolha uma das opções de pagamento:
( 1 ) À vista no dinheiro.
( 2 ) À vista no cartão.
( 3 ) 2x no cartão.
( 4 ) 3x ou mais no cartão.''')
opção = int(input('QUAL A SUA OPÇÃO? '))
if opção == 1:
    desc = preço - (preço * 10 / 100)
    print('O valor da compra ficou {:.2f} e com o pagamento à vista você terá 10% de desconto. O valor total é de '
          'R${:.2f} reais.'.format(preço, desc))
elif opção == 2:
    desc = preço - (preço * 5 / 100)
    print('Você ganhou 5% de desconto!! Sua compra ficou R${:.2f} reais.'.format(desc))
elif opção == 3:
    saldo = preço / 2
    print('A sua compra de R${:.2f} reais, ficou R${:.2f} reais em 2x vezes no cartão SEM JUROS.'.format(preço, saldo))
elif opção == 4:
    juros = preço + (preço * 20 / 100)
    perc = int(input('Vamos parcelar em quantas vezes? '))
    total = juros / perc
    print('A sua compra fica {}x de R${:.2f} reais, COM JUROS.'.format(perc, total, perc))
else:
    print('Opção inválida, tente novamente!')

