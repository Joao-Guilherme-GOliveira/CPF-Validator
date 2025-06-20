CPF_LENGTH = 11


def clean_cpf(cpf):
    cpf = str(cpf)
    clean_cpf = cpf.replace('.', '').replace('-', '').replace(' ', '')
    return clean_cpf


def validate_length(cpf):
    return len(cpf) == CPF_LENGTH


def validate_number(cpf):
    return not (cpf == cpf[0] * len(cpf))


def calc_digit(cpf, position):
    sum = 0

    for i in range(position - 1):
        sum += int(cpf[i]) * position
        position -=1 

    rest = sum % CPF_LENGTH

    if rest < 2:
        return 0
    
    else:
        return CPF_LENGTH - rest


def validate_cpf(cpf):
    final_cpf = clean_cpf(cpf)

    if not validate_length(final_cpf):
        return False
    
    first_digit = calc_digit(final_cpf, CPF_LENGTH - 1)
    cpf_to_second = final_cpf[:9] + str(first_digit)
    second_digit = calc_digit(cpf_to_second, CPF_LENGTH)

    if not validate_number(final_cpf):
        return False
    
    return first_digit == int(final_cpf[9]) and second_digit == int(final_cpf[CPF_LENGTH - 1])