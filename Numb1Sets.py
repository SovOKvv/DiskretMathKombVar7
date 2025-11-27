# Даны множества A, B, C, D. Найти значение заданных выражений.(Вариант 7)

A = [1, 2, 3, 4, 6, 7, 9, 10, 11, 13, 14, 17, 24, 26, 28, 29, 31, 32, 34, 35, 37, 38, 39]
B = [1, 2, 4, 10, 12, 13, 15, 17, 18, 19, 25, 30, 33, 34, 35, 36, 37]
C = [2, 7, 9, 14, 16, 21, 23, 25, 27, 28, 29, 32, 34, 35, 36, 37, 38]
D = [1, 3, 5, 6, 9, 10, 14, 15, 19, 21, 23, 28, 29, 31, 34, 35, 36, 37]

def union(s1, s2):
    # Объединение
    result = s1.copy()
    for i in s2:
        if i not in result:
            result.append(i)
    return sorted(result)

def intersection(s1, s2):
    # Пересечение
    result = []
    for i in s1:
        if i in s2:
            result.append(i)
    return sorted(result)

def differ(s1, s2):
    # Симметрическая разность множеств
    result = []
    for i in s1:
        if i not in s2:
            result.append(i)
    for i in s2:
        if i not in s1:
            result.append(i)
    return sorted(result)

def minus(s1, s2):
    # Разность множеств s1 \ s2
    result = []
    for i in s1:
        if i not in s2:
            result.append(i)
    return sorted(result)

# Выражение 1: ((B ∪ C) Δ ((C ∪ A) Δ D)) \ ((C ∩ A) ∪ (C ∩ B))

BunionC = union(B,C)
CunionA = union(C,A)
CunionAdeltD = differ(CunionA,D)
leftpart = differ(BunionC,CunionAdeltD)
CinterA  = intersection(C,A)
CinterB = intersection(C,B)

rightpart = union(CinterA,CinterB)

res1 = minus(leftpart,rightpart)
print('Результат 1 выражения:', res1)

# Выражение 2: ((D \ B) ∪ C) ∩ (((C ∪ B) ∩ A ∩ D) Δ ((C ∪ D) ∩ (A ∪ B)))
DminusB = minus(D, B)
leftpart2 = union(DminusB, C)
CunionB = union(C, B)
temp1 = intersection(CunionB, A)
part1 = intersection(temp1, D)
CunionD = union(C, D)
AunionB = union(A, B)
part2 = intersection(CunionD, AunionB)

rightpart2 = differ(part1, part2)

res2 = intersection(leftpart2, rightpart2)
print('Результат 2 выражения:', res2)