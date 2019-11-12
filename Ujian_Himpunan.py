# A = himpunan (set) bilangan genap antara 1 dan 20.
# B = himpunan (set) bilangan ganjil antara 1 dan 20.
# C = himpunan (set) bilangan negatif lebih dari -10.
# D = himpunan (set) bilangan prima antara 1 dan 20.
# E = himpunan (set) bilangan komposit antara 1 dan 20.

# Buatlah sebuah file python (.py) yang dapat menyelesaikan permasalahan himpunan berikut:

# a. A ∪ B ∪ C ∪ D ∪ E

# b. (A ∩ B) ∪ (D ∩ E)

# c. (A ∪ B) ∩ (D ∪ E)

# d. (A ∪ B) - (D ∪ E)

# e. (A ∪ B ∪ C) - (A ∩ E)

A = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
B = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}
C = {-9, -8, -7, -6, -5, -4, -3, -2, -1}
D = {2, 3, 5, 7, 11, 13, 17, 19}
E = {4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20}

# a. A ∪ B ∪ C ∪ D ∪ E

soal1 = set(list(A) + list(B) + list(C) + list(D) + list(E))

print(f"a. A ∪ B ∪ C ∪ D ∪ E = {soal1} \n")

# b. (A ∩ B) ∪ (D ∩ E)

F = []
G = []

for i in A:
    if i in B:
        F.append(i)

for i in D:
    if i in E:
        G.append(i)

soal2 = set(F + G)

print(f"b. (A ∩ B) ∪ (D ∩ E) = {soal2} \n")

# c. (A ∪ B) ∩ (D ∪ E)

I = set(list(A) + list(B))
J = set(list(D) + list(E))
K = []

for i in I:
    if i in J:
        K.append(i)

soal3 = set(K)

print(f"c. (A ∪ B) ∩ (D ∪ E) = {soal3} \n")

# d. (A ∪ B) - (D ∪ E)

L = set(list(A) + list(B))
M = set(list(D) + list(E))

soal4 = L - M

print(f"d. (A ∪ B) - (D ∪ E) = {soal4} \n")

# e. (A ∪ B ∪ C) - (A ∩ E)

N = set(list(A) + list(B) + list(C))
O = []

for i in A:
    if i in E:
        O.append(i)

soal5 = N - set(O)

print(f"e. (A ∪ B ∪ C) - (A ∩ E) = {soal5} \n")