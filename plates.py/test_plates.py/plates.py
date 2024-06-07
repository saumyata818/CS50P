def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not 2 <= len(s) <= 6 or not s[0:2].isalpha() or not s[2:].isalnum():
        return False

    stack = []
    for i in s[2:]:
        if i.isdigit():
            stack.append(i)
            if stack[0] == '0':
                return False

        elif stack and i.isalpha():
            return False

    return True

if __name__ == "__main__":
    main()
