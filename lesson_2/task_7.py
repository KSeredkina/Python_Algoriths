"""7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n - любое натуральное число. """

n = int(input('Введите натуральное число: '))
left_elements = 0
for i in range(1, n+1):
    left_elements += i
right_elements = n * (n + 1) // 2
if left_elements == right_elements:
    print(f'Для n = {n} равенство выполняется')
else:
    print(f'Для n = {n} равенство не выполняется')
