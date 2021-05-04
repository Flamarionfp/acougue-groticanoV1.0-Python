from time import sleep
print('\033[1;34mMercado Groticano\033[m')
print('-'*84)
print('\033[4;32mTabela de preços\033[m')
print('Filé duplo: R$ 4.90 por kg até 5 kg. R$ 5.80 por kg acima de 5kg')
print('Alcatra: R$ 5.90 por kg até 5kg. R$ 6.80 por kg acima de 5kg')
print('Picanha: R$ 6.90 por kg até 5g. R$ 7.80 por kg acima de 5kg')
print('-'*84)
print('\033[0;32mOBS:\033[mCompras feitas através do \033[1;32mCartão Groticano\033[m recebem \033[1;32m5% de desconto\033[m sobre o total!')
print('-'*84)
nome = str(input('Olá, bem vindo ao \033[1;34mMercado Groticano!\033[m Qual o seu nome? ')).strip()
if len(nome) == 0:
    print('É necessário que você informe seu nome para que possamos continuar o atendimento')
else:
    carne = str(input('Qual tipo de carne você deseja {}? '.format(nome))).upper().strip()
    preco = 0
    if carne != 'FILÉ DUPLO' and carne != 'FILE DUPLO' and carne != 'ALCATRA' and carne != 'PICANHA':
        print(
            'Não Trabalhamos com o que pediu {}. Você deve informar o tipo de carne desejada\nde acordo com os cortes disponíveis na lista acima.'.format(nome))
    else:
        quant = float(input('Quantos kg você gostaria? '))
        if quant <= 0:
            print('Erro! A quantidade de kg deve ser maior que 0')
        else:
            pag = int(input('Qual a forma de pagamento? Digite 1 para Dinheiro ou 2 para Cartão Groticano: '))
            if pag == 1:
                forma = 'Dinheiro'
                if carne == 'FILÉ DUPLO' or carne == 'FILE DUPLO':
                    if quant < 5:
                        desconto = 0
                        preco_total = 4.90 * quant
                    else:
                        desconto = 0
                        preco_total = 5.80 * quant
                elif carne == 'ALCATRA':
                    if quant < 5:
                        desconto = 0
                        preco_total = 5.90 * quant
                    else:
                        desconto = 0
                        preco_total = 6.80 * quant
                elif carne == 'PICANHA':
                    if quant < 5:
                        desconto = 0
                        preco_total = 6.90 * quant
                    else:
                        desconto = 0
                        preco_total = 7.80 * quant
            else:
                if pag == 2:
                    forma = 'Cartão Groticano'
                    if carne == 'FILÉ DUPLO' or carne == 'FILE DUPLO':
                        if quant < 5:
                            desconto = 4.90 * quant * 5 / 100
                            preco_total = quant * 4.90 - desconto
                        else:
                            desconto = 5.80 * quant / 100
                            preco_total = quant * 5.80 - desconto
                    elif carne == 'ALCATRA':
                        if quant < 5:
                            desconto = 5.90 * quant * 5 / 100
                            preco_total = quant * 5.90 - desconto
                        else:
                            desconto = 6.80 * quant * 5 / 100
                            preco_total = quant * 6.80 - desconto
                    elif carne == 'PICANHA':
                        if quant < 5:
                            desconto = 6.90 * quant * 5 / 100
                            preco_total = quant * 6.90 - desconto
                        else:
                            desconto = 7.80 * quant * 5 / 100
                            preco_total = quant * 7.80 - desconto
                else:
                    print('Erro, digite uma forma de pagamento válida.')
            print('\033[0;32mAguarde enquanto emitimos sua nota fiscal...\033[m')
            sleep(2)
            print('Nome do cliente: {}'.format(nome))
            print('Tipo de carne: {}'.format(carne))
            print('Quantidade de carne: {:.1f} kg'.format(quant))
            print('Forma de pagamento: {}'.format(forma))
            print('Desconto R$ {:.2f}\nTOTAL: R$ {:.2f}'.format(desconto, preco_total))
            input()
