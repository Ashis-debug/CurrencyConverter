# put your python code here
number = int(input())
result = number * number
if number == 0:
    print(0)
else:
    summ = number
    while True:
        number = int(input())
        summ = summ + number
        result = result + (number * number)
        if summ == 0:
            break
print(result)






