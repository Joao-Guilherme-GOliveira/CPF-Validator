import validarModule
def main():
    cpf_digitado = input("Digite o CPF(Com pontos e traços): ")

    if validarModule.validar_cpf(cpf_digitado):
        print("CPF válido!")
    else:
        print("CPF inválido.")

if __name__ == "__main__":
    main()