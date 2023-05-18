#Verificador de cpf

#calculo do primeiro digito do CPF
while True:#Solicita um novo CPF a cada CPF verificado
    cpf = input('Digite o seu cpf: ').replace('.','').replace(' ','').replace('-','')
    # Aqui eu tento verificar o CPF digitado pelo usuário
    try:
        cont = total = total_10 = 0
        for p in range(10, 1, -1):
            soma = p*(int(cpf[cont]))
            cont += 1
            total += soma
        total_10 = total*10
        resto = total_10 % 11
        if resto > 9:
            cpf_10 = 0
        else:
            cpf_10 = resto
#calculo do segundo digito do CPF
        cpf01 = cpf[0:9] + str(cpf_10)
        cont_02 = total_02 = total_11 = 0
        for n in range(11, 1, -1):
            soma_02 = n*(int(cpf01[cont_02]))
            cont_02 += 1
            total_02 += soma_02
        total_11 = total_02*10
        resto_02 = total_11 % 11
        if resto_02 > 9:
            cpf_11 = 0
        else:
            cpf_11 = resto_02
        cpf_09 = cpf[0:9]
        cpf_testado = cpf_09 + str(cpf_10) + str(cpf_11)
        print(f'O CPF a ser verificado é: {cpf_testado}')
        if cpf_testado == cpf:# Aqui o CPF criado é testado como CPF enviado pelo usuário
            print(f'O CPF {cpf} enviado pelo usuario é valido!!')
        else:
            print(f'Cpf {cpf} é invalido!!')
    except ValueError:
        print('ERRO! Digite os digitos corretos!!')
    except IndexError:
        print('ERRO!! CPF deve conter 11 digitos!!')