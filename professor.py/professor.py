import random

def main():
    n = get_level()
    count = 0
    for _ in range(10):
        x, y = generate_integer(n)
        for i in range(3):
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                continue
            else:
                if answer == x + y:
                    count += 1
                    break
                else:
                    print("EEE")
                    if i == 2:
                        print(f"{x} + {y} = {x+y}")
                    continue
    print("Score: ",count)


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 0 < n < 4:
                return n
            else:
                raise ValueError
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        min_value = 10*(level - 1)
    else:
        min_value = 10**(level - 1)
    max_value = 10**level - 1
    x = random.randint(min_value, max_value)
    y = random.randint(min_value, max_value)
    return x, y

if __name__ == "__main__":
    main()
