
# 3.2. Напишите программу, которая считывает строку с числом n, которое задаёт количество чисел, которые нужно считать. Далее считывает n строк с числами x i​, по одному числу в каждой строке. Итого будет � + 1 n+1 строк.

# При считывании числа � � x i​программа должна на отдельной строке вывести значение � ( � � ) f(x i​). Функция f(x) уже реализована и доступна для вызова.

# Функция вычисляется достаточно долго и зависит только от переданного аргумента � x. Для того, чтобы уложиться в ограничение по времени, нужно избежать повторного вычисления значений.

# Sample Input:

# 5 5 12 9 20 12 Sample Output:

# 11 41 47 61 41 

def f(num):
  return num ** 2
n = int(input()) # количество чисел, которые нужно считать
results = {}
for i in range(n):
  x = int(input())
  if x not in results:
    results[x] = f(x)
  print(results[x])
