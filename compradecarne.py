from time import sleep
print('Açougue Groticano')
print('-'*84)
print('Tabela de preços')
print('Filé duplo: R$ 4.90 por kg até 5 kg. R$ 5.80 por kg acima de 5kg')
print('Alcatra: R$ 5.90 por kg até 5kg. R$ 6.80 por kg acima de 5kg')
print('Picanha: R$ 6.90 por kg até 5g. R$ 7.80 por kg acima de 5kg')
print('-'*84)
print('OBS:Compras feitas através do Cartão Groticano recebem 5% de desconto sobre o total!')
print('-'*84)
nome = str(input('Olá, bem vindo ao Açougue Groticano! Qual o seu nome? ')).strip()
while len(nome) <= 2:
    print('Nome inválido! É necessário que você informe seu nome corretamente para que possamos\ncontinuar o atendimento')
    nome = str(input('Seu nome: ')).strip()
else:
    carne = str(input('Qual tipo de carne você deseja, {}? '.format(nome))).upper().strip()
    preco = 0
    while carne != 'FILÉ DUPLO' and carne != 'FILE DUPLO' and carne != 'ALCATRA' and carne != 'PICANHA':
        print('Não Trabalhamos com o que pediu.')
        print('Você deve informar o tipo de carne desejada de acordo com os cortes disponíveis na lista acima.')
        carne = str(input('Informe novamente o tipo de carne desejada: ')).upper().strip()
    else:
        quant = float(input('Quantos kg você gostaria? '))
        while quant <= 0:
            print('Erro! A quantidade de kg deve ser maior que 0')
            quant = float(input('Quantos kg você gostaria? '))
        else:
            pag = int(input('Qual a forma de pagamento? Digite 1 para Dinheiro ou 2 para Cartão Groticano: '))
            while pag != 1 and pag != 2:
                pag = int(input('Forma de pagamento inválida, digite novamente: '))
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
            print('Aguarde enquanto emitimos sua nota fiscal...')
            sleep(2)
            print('Nome do cliente: {}'.format(nome))
            print('Tipo de carne: {}'.format(carne))
            print('Quantidade de carne: {:.1f} kg'.format(quant))
            print('Forma de pagamento: {}'.format(forma))
            print('Desconto R$ {:.2f}\nTOTAL: R$ {:.2f}'.format(desconto, preco_total))
            input('Aperte enter para sair...')
