import pdb



number_day = ''

#Checking that the day is Sunday
def is_sunday(number_day):
    if number_day % 7 == 0:
        return True
    else:
        return False

month = [31,28,31,30,31,30,31,31,30,31,30,31]
month_leap = [29 if x == 28 else x for x in month]

y = tuple(range(1901,2001))
years = []

for x in y:
    if x % 4 == 0:
        years.append(366)
    else:
        years.append(365)

#add leapmonths
def is_first(number_day, leap):
    if leap == False:
        i = 0
        while number_day > 28:
            number_day = number_day - month[i]
            i += 1
        if number_day == 1:
            return True
        else:
            return False
    elif leap == True:
        i = 0
        while number_day > 29:
            number_day = number_day - month_leap[i]
            i += 1
        if number_day == 1:
            return True
        else:
            return False


#pdb.set_trace()

# 1904
counter = 0

for y in years:
    k = 1
    if k % 4 == 0:
        leap = True
    else:
        leap = False
    x = tuple(range(1,y+1))
    for n in x:
        if is_first(n,leap):
            if is_sunday(n):
                counter +=1
            else:
                pass
        else:
            continue
    k += 1


print(counter)