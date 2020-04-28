print("para todos os meus caros colegas de mul2 \n")
print("arithmetic encoding of the night\n")
print("by capella 😎\n")


while True:
    try:
        print("Quantas letras a tabela tem, oh maluco?")
        numero_letras = int(input(">"))
        break
    except Exception as e:
        print("Escreve um número inteiro , 😡")

tabelita = {}
alfabetinho = []
for x in range(0,numero_letras):
    #busca letra
    while True:
        print("Escreve a letra numero" ,'\033[1m', x+1 ,'\033[0m',"da palavra")
        letra = str(input(">"))
        if len(letra) == 1:
            break
        print('\033[93m',"Oh zé maluco , escreve só 1 letra , tenta outra vez.",'\033[0m')
    #busca numero
    while True:
        print("Escreve a probabilidade da letra" ,'\033[1m', letra ,'\033[0m',"da palavra")
        try:
            prob = float(input(">"))
            break
        except Exception as e:
            print('\033[93m',"Float inválido, tenta outra vez. (ex: 0.2)",'\033[0m')

    tabelita[letra] = prob
    alfabetinho.append(letra)

def build_my_prob(codes):
    anterior = 0
    current = 0
    arr = {}
    for x in alfabetinho:
        largura = tabelita[x]
        current += largura
        current = round(current,2)
        #print("letra= " , x, "int_baixo=" , anterior , "int_alto=",current)
        arr[x] = anterior , current
        anterior = current
    return arr
 
def make_exercise(string, probs):
    lista = list(string)
    tamanho = len(string)
    a_alto = 1
    a_baixo = 0
    largura = 1
    print("a_alto = a_baixo + largura + subint_alto")
    print("a_baixo = a_baixo + largura + subint_baixo")
    print("largura = a_alto - a_baixo")
    print("========================")
    for x in range(0,tamanho):
        print("Iteracao numero ", x+1) 
        subint_baixo , subint_alto = probs[lista[x]] #vai buscar valores a tabela
        print("a_alto = " , a_baixo , "+",largura,"*",subint_alto)
        a_alto = a_baixo + largura * subint_alto
        a_alto = round(a_alto,10)
        print('\033[93m',"a_alto =" ,a_alto , '\033[0m')
        print("a_baixo = " , a_baixo , "+",largura,"*",subint_baixo)
        a_baixo = a_baixo + largura * subint_baixo
        a_baixo = round(a_baixo,10)
        print('\033[94m' ,"a_baixo =" ,a_baixo, '\033[0m')
        largura = a_alto - a_baixo
        largura = round(largura,10)
        print("========================")

prob = build_my_prob(alfabetinho)

make_exercise("UUSSAC!",prob)

