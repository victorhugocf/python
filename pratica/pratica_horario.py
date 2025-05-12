horario = input('Que horas são? ')

horario_int = int(horario)

if horario_int >= 0 and horario_int <=5:
    print('Boa noite')
elif horario_int >= 0 and horario_int <=11:
    print('Bom dia')
elif horario_int >= 12 and horario_int <=17:
    print('Boa tarde')
elif horario_int >= 18 and horario_int <=23:
    print('Boa noite')


