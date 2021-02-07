from random import *

A = []
for i in range (int(input("Введіть скільки потрібно додати в список елементів: "))):
    A.append(input("Введіть елемент для списку: "))

for elem in A:
    print(elem, end = ' ')

print('')

print(A[1:2])

print('')

print(' '.join(map(str, A)))


print('')


B = [0] * int(input("Введіть скільки потрібно додати в список елементів: "))
for i in range (len(B)):
    B[i] = int(input("Введіть елемент для списку: "))

for i in range (len(B)):
    print(B[i])


C = input("Введіть потрібні елементи через пробіл: ").split()
for i in range (len(C)):
    C[i] = int(C[i])
print(C)

D =['red', 'green', 'blue']
print(' '.join(D))
print(''.join(D))
print('***'.join(D))

E = [i ** 2 for i in range (1, 9 + 1)]
print(E)

G = [randint(-99, 99) for i in range(10)]
print(G)

H = [x for x in G if x > 0]
print(H)
