
def lerDadosEntrada(dadosStr):
    return dict(map(lambda par: (int(par.split(':')[0]), float(par.split(':')[1])), dadosStr.split()))

def criarTesteLimite(limite):
    return lambda x: x[1] > limite

def calcularVariacaoPercentual(dados):

    diasOrdenados = sorted(dados.keys())
    return dict(map(
        lambda i: (
            diasOrdenados[i],
            round(((dados[diasOrdenados[i]] - dados[diasOrdenados[i - 1]]) / dados[diasOrdenados[i - 1]]) * 100, 2)
        ),
        range(1, len(diasOrdenados))
    ))

def compararComMedia(media):
    return lambda x: ("📈 acima da média" if x[1] > media else "📉 abaixo da média", x[1])

def solicitarEntradaUsuario():

    print("📥 Digite os dados no formato Dia:valor (ex: 1:23.5 2:24.0 ...):")
    return input("> ")

def mostrarDiasAcimaDoLimite(fechamentos, limite):

    filtro = criarTesteLimite(limite)
    dias = list(map(lambda x: x[0], filter(filtro, fechamentos.items())))
    print(f"\n📅 Dias com valor acima de R$ {limite:.2f}:")
    print("👉", dias)
    return dias

def mostrarVariacaoPercentual(variacoes):

    print("\n📊 Variação percentual diária:")
    list(map(lambda x: print(f"Dia {x[0]}: {x[1]}%"), variacoes.items()))

def mostrarResumoVariacoes(variacoes):

    maiorAlta = max(variacoes.items(), key=lambda x: x[1])
    maiorQueda = min(variacoes.items(), key=lambda x: x[1])
    print(f"\n🚀 Maior alta: Dia {maiorAlta[0]} - {maiorAlta[1]}%")
    print(f"📉 Maior queda: Dia {maiorQueda[0]} - {maiorQueda[1]}%")

def calcularMedia(fechamentos):
    return round(sum(fechamentos.values()) / len(fechamentos), 2)

def mostrarClassificacaoMedia(fechamentos, media):

    classificador = compararComMedia(media)
    classificacoes = dict(map(lambda item: (item[0], classificador(item)), fechamentos.items()))
    print(f"\n📈 Média dos preços: R$ {media}")
    print("\n📝 Classificação de cada dia em relação à média:")
    list(map(lambda x: print(f"Dia {x[0]}: {x[1][0]}, R$ {x[1][1]}"), classificacoes.items()))
    return classificacoes

def main():
    
    entradaUsuario = solicitarEntradaUsuario()
    fechamentos = lerDadosEntrada(entradaUsuario)
    mostrarDiasAcimaDoLimite(fechamentos, 25.0)
    variacoes = calcularVariacaoPercentual(fechamentos)
    mostrarVariacaoPercentual(variacoes)
    mostrarResumoVariacoes(variacoes)
    media = calcularMedia(fechamentos)
    mostrarClassificacaoMedia(fechamentos, media)

if __name__ == "__main__":
    main()
