def recurring_cycle_len(n):
    """
    Returns the length of the recurring cycle of the decimal representation of 1/n.
    If there is no recurring cycle, returns 0.
    """
    remainder = 1
    remainders = {}
    i = 0
    while remainder not in remainders and remainder != 0:
        remainders[remainder] = i
        remainder = (remainder * 10) % n
        i += 1
    if remainder == 0:
        return 0
    else:
        return i - remainders[remainder]

max_len = 0
max_d = 0
for d in range(1, 1000):
    len_d = recurring_cycle_len(d)
    if len_d > max_len:
        max_len = len_d
        max_d = d

print(recurring_cycle_len(7))

