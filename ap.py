def proper(number):
    divisors = {1}
    if number % 2 == 0:
        n = tuple(range(2,int((number/2))+1))
        for m in n:
            if number % m == 0:
                divisors.add(m)
            else:
                continue
    elif number % 3 == 0:
        n = tuple(range(3,int((number/3))+1))
        for m in n:
            if number % m == 0:
                divisors.add(m)
            else:
                continue
    elif number % 5 == 0:
        n = tuple(range(5,int((number/5))+1))
        for m in n:
            if number % m == 0:
                divisors.add(m)
            else:
                continue
    else:
        n = tuple(range(7,int((number/7))+1))
        for m in n:
            if number % m == 0:
                divisors.add(m)
            else:
                continue
    return sum(divisors)

def amicable(num1, num2):
    if proper(num1) == num2 and proper(num2)==num1:
        return True
    else:
        return False

amic = {220,284}
naturals10000 = tuple(range(2,10000))
for n in naturals10000:
    for m in naturals10000:
        if amicable(n,m):
            amic.update([n,m])
            break
        else:
            continue