def fizzbuzz(n):
    li = []
    for i in range (1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            li.append("FizzBuzz")
        elif i % 3 == 0:
            li.append("Fizz")
        elif i % 5 == 0:
            li.append("Buzz")
        else:
            li.append(i)
    return li

print(fizzbuzz(1))
print(fizzbuzz(2))
print(fizzbuzz(3))
print(fizzbuzz(4))
print(fizzbuzz(5))
print(fizzbuzz(6))
print(fizzbuzz(7))
print(fizzbuzz(8))
print(fizzbuzz(9))
print(fizzbuzz(10))
print(fizzbuzz(11))
print(fizzbuzz(12))
print(fizzbuzz(13))
print(fizzbuzz(14))
print(fizzbuzz(15))
print(fizzbuzz(16))
