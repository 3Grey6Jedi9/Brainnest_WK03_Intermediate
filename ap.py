naturals = range(25, 28123)
not_abundants = set()
abundants = set()
for i in range(12, 28123):
    if sum(j for j in range(1, i//2 + 1) if i % j == 0) > i:
        abundants.add(i)
        print(j)
    if not any(i - j in abundants for j in abundants):
        not_abundants.add(i)

sum(not_abundants)


