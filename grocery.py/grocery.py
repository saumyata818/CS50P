dict = {}

while True:
    try:
        food = input().upper()
        if food not in dict:
            dict[food] = 1
        else:
            dict[food] += 1
    except EOFError:
            break

lst = sorted(dict.items())
for k,v in lst:
    print(v,k)
