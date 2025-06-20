import validator_Module
def main():
    cpf_input = input("Digite o CPF(Com pontos e traços): ")

    if validator_Module.validate_cpf(cpf_input):
        print("CPF válido!")
    else:
        print("CPF inválido.")

if __name__ == "__main__":
    main()