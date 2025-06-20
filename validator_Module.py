CPF_LENGTH = 11


def clean_cpf(cpf):
    cpf = str(cpf)
    clean_cpf = cpf.replace('.', '').replace('-', '').replace(' ', '')
    return clean_cpf


def validate_length(cpf):
    return len(cpf) == CPF_LENGTH


def is_uniform_digits(cpf):
    return cpf == cpf[0] * len(cpf)


def calc_digit(cpf, position):
    result = 0

    for i in range(position - 1):
        result += int(cpf[i]) * position
        position -=1 

    rest = result % CPF_LENGTH

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

    if is_uniform_digits(final_cpf):
        return False
    
    return first_digit == int(final_cpf[9]) and second_digit == int(final_cpf[CPF_LENGTH - 1])