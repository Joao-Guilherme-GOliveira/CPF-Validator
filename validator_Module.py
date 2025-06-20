def clean_cpf(cpf):
    cpf = str(cpf)
    cpf_clean = cpf.replace(".","").replace("-","").replace(" ","")
    return cpf_clean


def validate_length(cpf):
    return len(cpf) == 11


def validate_number(cpf):
    return not (cpf == cpf[0] * len(cpf))


def calc_digit(cpf, position):
    sum = 0

    for i in range(position - 1):
        sum += int(cpf[i]) * position
        position -=1 

    rest = sum % 11

    if rest < 2:
        return 0
    
    else:
        return 11 - rest


def validate_cpf(cpf):
    final_cpf = clean_cpf(cpf)

    if not validate_length(final_cpf):
        return False
    
    first_digit = calc_digit(final_cpf,10)
    cpf_to_second = final_cpf[:9] + str(first_digit)
    second_digit = calc_digit(cpf_to_second,11)

    if not validate_number(final_cpf):
        return False
    
    if first_digit == int(final_cpf[9]) and second_digit == int(final_cpf[10]):
        return True
    else:
        return False