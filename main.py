produtos = [
    'Milka com oreo', 'Nutella', 'Laka', 'Doce de Leite',
    'Biscoito Passa-tempo', 'Dentaduras Fini', 'Bis Chocolate Branco',
    'Amendoim Japones', 'Sonho de Valsa', 'Ouro Branco', 'Baton', 'Kinder ovo',
    'Tortuguita', 'Fandangos', 'Pringles', 'Ruffles'
]
precos = [13.50, 9.00, 5.00, 6.00, 2.30, 4.99, 3.99, 2.00, 1.00, 1.00, 0.75, 7.40,
    1.20, 6.60, 13.00, 7.00]
sacola = []
sacolaPreco = []
sacolaQuantidade = []
estoque = [2, 2, 13, 4, 23, 6, 15, 8, 40, 34, 20, 12, 21, 5, 3, 7]
comprasStatus = True
returnCompras = 0
valor = 0

def listarProdutos():
    i = 0
    for produto in produtos:
        if estoque[i] != 0:
            print(f'{i + 1} - {produto}, R$ {precos[i]}')
        elif estoque[i] == 0:
            produtos.pop(i)
            precos.pop(i)
            estoque.pop(i)
        i += 1

def listarCarrinho():
    global valor
    i = 0

    for sacolaItens in sacola:
        print(f'{i + 1} - {sacolaItens}, preço unitário R$ {sacolaPreco[i]} X {sacolaQuantidade[i]}(quand) = R$ {sacolaPreco[i] * sacolaQuantidade[i]} ')
        valor += sacolaPreco[i] * sacolaQuantidade[i]
        i += 1
    print(f'Valor da sua compra {valor}')
def verificarContinuar():
    global comprasStatus

    while comprasStatus:
        listarProdutos()
        adcionarItens()
        returnCompras = input(
            'Aberte "espaço" para continuar e "n" para finalizar\n'
        )

        if (returnCompras == 'n'):
            comprasStatus = False
        else:
            comprasStatus = True

def adcionarItens():
    produtoSelecinado = int(input('Qual o código do seu produto, que vc quer adicionar ?\n'))-1
    print(f'{produtos[produtoSelecinado],[precos[produtoSelecinado]], [estoque[produtoSelecinado]]},')
    quantidadeSelecinado = 0

    quantidadeIndisponivel = True
    while (quantidadeIndisponivel):
            quantidadeSelecinado = int(input(f'Temos {[estoque[produtoSelecinado]]} do {[produtos[produtoSelecinado]]} informe a quantidade !\n'))
            quantidadeRestante = estoque[produtoSelecinado] - quantidadeSelecinado
            if (quantidadeRestante >= 0):
                estoque[produtoSelecinado] = quantidadeSelecinado
                estoque[produtoSelecinado] = quantidadeRestante
                quantidadeIndisponivel = False
            else:
                print('Essa quantidade não está disponivel!!')

    naoexisteitem = True
    for item in sacola:
        i = 0
        if (item == produtos[produtoSelecinado]):
            sacolaQuantidade[i] = sacolaQuantidade[i] + quantidadeSelecinado
            naoexisteitem = False
        i += 1
    if(naoexisteitem):
        sacola.append(produtos[produtoSelecinado])
        sacolaPreco.append(precos[produtoSelecinado])
        sacolaQuantidade.append(quantidadeSelecinado)

def modoPagamento():
    global valor
    modoPg = input("Qual a forma de pagamento ?? 'D' para dinheiro e 'C' para cartão\n")
    if (modoPg == 'd'):
        valor = valor*0.10
        print(f'Com Desconto de 10%, a sua comprar fica = R$ {valor:.2f}')
        valorRecebido = int(input('Informe o valor passado pelo cliente !!\n'))

        troco = valorRecebido - valor
        print(f'\nSeu troco é: R${troco}')

        re = True
        céd = 100
        totcéd = 0
        while re:
            if troco >= céd:
                troco -= céd
                totcéd += 1
            else:
                if totcéd > 0:
                    print(f'Total de {totcéd} cédulas de  R${céd}')
                if céd == 100:
                    céd = 50
                elif céd == 50:
                    céd = 20
                elif céd == 20:
                    céd = 10
                elif céd == 10:
                    céd = 5
                elif céd == 5:
                    céd = 1
                totcéd = 0
                if troco == 0:
                    break
    else:
        print(f'A sua comprar fica = R$ {valor:.2f}')

verificarContinuar()
listarCarrinho()
modoPagamento()
print("Obrigado pela preferência, volte sempre !!")

