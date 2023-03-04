import pdb
my_set = {13,40,20,10,5,16,8,4,2,1}


def func(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3*n + 1

naturals = tuple(range(14,int(1e6+1)))


pdb.set_trace()

for s in naturals:
    new_set = set()
    new_set.add(s)
    n = s
    while n != 1:
        n = func(n)
        new_set.add(n)
    if len(new_set) > len(my_set):
        my_set = new_set


print(list(my_set)[0])