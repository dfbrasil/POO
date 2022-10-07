
a = input()

mai = []
min = []
num = []
num_par = []
num_impar = []

for i in a:

    if  ord(i) >= 65 and ord(i) <= 90:
        mai.append(i)
    elif ord(i) >= 97 and ord(i) <= 122:
        min.append(i)
    elif ord(i) >= 48 and ord(i) <= 57:
        num.append(i)

int_map = map(int, num)
int_list = list(int_map)

for i in int_list:
    if (i%2 == 0):
        num_par.append(i)
    else:
        num_impar.append(i)

mai_sort = ''.join(sorted(mai))
min_sort = ''.join(sorted(min))

str_map_par = map(str, num_par)
str_list_par = list(str_map_par)

str_map_impar = map(str, num_impar)
str_list_impar = list(str_map_impar)

num_par_sort = ''.join(sorted(str_list_par))
num_impar_sort = ''.join(sorted(str_list_impar))

print(f'{min_sort}{mai_sort}{num_impar_sort}{num_par_sort}')


