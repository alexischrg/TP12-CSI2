def pow(a,b):
    p=1
    if b == 0 :
        return p
    return a * pow(a,b-1)

print(pow(42, 0)) # 1
print(pow(1, 10)) # 1
print(pow(2, 5)) # 32
print(pow(7, 2)) # 49