def registrar_funcionario():
    funcionarios = []
    while True:
        nome = input("Digite o nome do funcionário (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break
        cargo = input("Digite o cargo do funcionário: ")
        salario = float(input("Digite o salário do funcionário: "))
        funcionarios.append({"nome": nome, "cargo": cargo, "salario": salario})
    return funcionarios

def aumentar_percentual(percentual):
    return lambda salario: salario * (percentual / 100)

def calcular_novo_salario(funcionario):
    aumento_junior = aumentar_percentual(10)
    aumento_pleno = aumentar_percentual(7)
    aumento_senior = aumentar_percentual(5)
    
    if funcionario["cargo"].lower() == "junior":
        aumento = aumento_junior(funcionario["salario"])
    elif funcionario["cargo"].lower() == "pleno":
        aumento = aumento_pleno(funcionario["salario"])
    elif funcionario["cargo"].lower() == "senior":
        aumento = aumento_senior(funcionario["salario"])
    else:
        aumento = 0
    
    funcionario["novo_salario"] = funcionario["salario"] + aumento
    return funcionario

def aplicar_aumentos(funcionarios):
    return list(map(calcular_novo_salario, funcionarios))   

def exibir_funcionarios(funcionarios):
    print("\nFuncionários com aumento de salário:")
    for funcionario in funcionarios:
        print(f"Nome: {funcionario['nome']}, Cargo: {funcionario['cargo']}, Salário Atual: R${funcionario['salario']:.2f}, Novo Salário: R${funcionario['novo_salario']:.2f}")
        
def main():
    funcionarios = registrar_funcionario()
    funcionarios_com_aumento = aplicar_aumentos(funcionarios)
    exibir_funcionarios(funcionarios_com_aumento)
    
if __name__ == "__main__":
    main()        
        