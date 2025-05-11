prim_val = input('Digite o primeiro valor: ')
segund_val = input('Digite o segundo valor: ')

int_prim_val = int(prim_val)
int_segund_val = int(segund_val)

if int_prim_val > int_segund_val:
    print(f'O primeiro valor {int_prim_val} e maior que o segundo {int_segund_val}.')
elif int_prim_val == int_segund_val:
    print('Os dois valores sao iguais.')
else:
    print(f'O segundo valor {int_segund_val} e maior que o primeiro {int_prim_val}.')
