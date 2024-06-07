def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    time = 0
    cost = 0
    while True:
        try:
            order = input("Item: ").title().strip()
            cost = float(cost) + float((menu[order]))
            time+=1
        except EOFError:
            print()
            exit()
        except KeyError:
            pass
        else:
            print("Total :$"+"%.2f" % cost)

if __name__ == "__main__":
    main()
