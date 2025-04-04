def gabarito():
    return ["A", "C", "D", "B", "A"]

def adicionar_candidatos() -> list:
    n_candidatos = int(input("Digite a quantidade de candidatos: "))
    candidatos = []
    for i in range(n_candidatos):
        print(f"\nCandidato {i + 1}:")
        nome = input("Digite o nome do candidato: ")
        respostas_input = input("Digite as respostas do candidato (ex: A C D B A): ")
        respostas = respostas_input.strip().upper().split()
        candidatos.append({"nome": nome, "respostas": respostas})
        print(f"Candidato {nome} adicionado com sucesso!")
    return candidatos

def avaliador(gabarito: list):  
    return lambda respostas: sum([1 for i, j in zip(respostas, gabarito) if i == j]) / len(gabarito) * 10

def calcular_notas(candidatos: list, avaliador_func) -> list:
    return list(map(lambda candidato: (candidato["nome"], avaliador_func(candidato["respostas"])), candidatos))

def filtrar_aprovados(resultados: list) -> list:
    return list(filter(lambda candidato: candidato[1] >= 7, resultados))

def info_candidatos(candidatos: list) -> None:
    print("\nNotas dos candidatos:")
    list(map(lambda c: print(f"{c[0]}: {c[1]:.2f}"), candidatos))

def mostrar_maior_nota(resultados: list) -> None:
    if not resultados:
        print("Nenhum resultado para analisar.")
        return
    maior_nota_valor = max(map(lambda x: x[1], resultados))
    melhores = list(filter(lambda x: x[1] == maior_nota_valor, resultados))
    print("Candidato(s) com a maior nota:")
    print(f'- {melhores[0][0]}: {maior_nota_valor:.2f}')

def main():
    gabarito_respostas = gabarito()
    candidatos = adicionar_candidatos()
    avaliador_func = avaliador(gabarito_respostas)
    resultados = calcular_notas(candidatos, avaliador_func)
    info_candidatos(resultados)

    aprovados = filtrar_aprovados(resultados)
    print(f"Total de candidatos aprovados: {len(aprovados)}")
    for candidato in aprovados:
        print(f"- {candidato[0]}: {candidato[1]:.2f}")
    mostrar_maior_nota(resultados)

if __name__ == "__main__":
    main()
