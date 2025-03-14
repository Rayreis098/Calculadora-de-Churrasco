#Crie um app para simular os custos de um churrasco.
#Front| Quantidade de adultos(homens e mulheres) e crianças
#Retorne a quantidade de carne, frango, carvão, refrigerente e cerveja com os custos, individuais totais
#Back| Faça uma simulação atribuindo gramas para cada tipo de pessoa
#Valores diferentes para homens, mulheres e crianças
#Faça uma simulação atribuindo ml ou litros.
#Faça os cálculos atribuindo valores para cada item
#Multiplique tudo e some para calcular o valor total do churrasco.


qtdCarneH = 0.4
qtdFrangoH = 0.2
qtdCervejaH = 3.5 #homem bebe 4 latas
qtdRefrigeranteH = 0.25 #500ml de refrigerante
qtdCarvaoH = 1 #um pacote para cada 10 pessoas

qtdCarneM = 0.3
qtdFrangoM = 0.1
qtdCervejaM = 2#homem bebe 4 latas
qtdRefrigeranteM= 0.25 #500ml de refrigerante
qtdCarvaoM= 1 #um pacote para cada 10 pessoas

qtdCarneC= 0.4
qtdFrangoC= 0.2
qtdCervejaC = 0
qtdRefrigeranteC= 0.125                    
qtdCarvaoC= 1 



precoCarne = 50.0
precoFrango = 23.0
precoCerveja = 3.99 #lata heineken 269ml
precoRefri = 8.0 #garrafa 2 litros
precoCarvao = 25.0 #pacote 4 kg

#Capturar informações
while True: #laço de repetição para o app continuar rodando
    try: #tratamento de erro
        print('Bem vindos a calculadora de churrasco')
        print()
        homens = float(input('Quantos homens irão para o churrasco?: '))
        mulheres =float(input('Quantas mulheres aparecerão no churrasco?: '))
        crianças = float(input('Quantas crianças aparecerão no churrasco?: '))

        #Criar calculos de peso:

        carneH =homens * qtdCarneH
        carneM = mulheres * qtdCarneM
        carneC = crianças * qtdCarneC

        frangoH = homens * qtdFrangoH
        frangoM = mulheres * qtdFrangoM
        frangoC = crianças * qtdFrangoC

        cervejaH = homens * qtdCervejaH
        cervejaM = mulheres * qtdCervejaM

        refriH = homens * qtdRefrigeranteH
        refriM = mulheres * qtdRefrigeranteM
        refriC = crianças * qtdRefrigeranteC

        carvaoPacotes = (homens + mulheres + crianças) / 10

        #Criar calculos de gastos

        valorCarneH = carneH * precoCarne
        valorCarneM = carneM * precoCarne
        valorCarneC = carneC * precoCarne

        valorFrangoH = frangoH * precoFrango
        valorFrangoM = frangoM * precoFrango
        valorFrangoC = frangoC * precoFrango

        valorRefriH = refriH * precoRefri
        valorRefriM = refriM * precoRefri
        valorRefriC = refriC * precoRefri
        valorCarvao = carvaoPacotes * precoCarvao

        valorCervejaHomem = cervejaH * precoCerveja
        valorCervejaMulher = cervejaM* precoCerveja

        total = valorCarneC + valorCarneH + valorCarneM + valorFrangoC + valorFrangoH + valorFrangoM + valorRefriC + valorRefriH + valorRefriM + valorCervejaHomem + valorCervejaMulher + valorCarvao

        # apresentar os resultados    

    except ValueError:
        print('Por favor digite apenas números inteiros')

    else: #resultados das contas devem ser colocados no else em laço de repetição do while
        print(f'Total de pessoas Homens: {homens}, Mulheres: {mulheres}, Crianças: {crianças}')   
        print()
        print(f'Total de {homens + mulheres + crianças} convidados.')
        print()
        print(f'Lista de Compras: {carneC + carneH + carneM} kg de Carne.')
        print(f'                  {frangoC + frangoH + frangoM} kg de Frango.')
        print(f'                  {refriC + refriH + refriM} garrafas de refrigerante.')
        print(f'                  {cervejaH + cervejaM} latas decerveja.')
        print(f'                  {carvaoPacotes} pacotes de carvão.')
        print()
        print(f'Valor total da Compra: {total} reais.')
        print(f'Valor por convidado: {total / (homens + mulheres + crianças)} reais.')


    #apresentar os resultado

