import re

def main():
    print(count(input("Text: ")))

def count(s):
    return len(re.findall(r'(^um|\Wum\W|\bum\b)', string=s, flags=re.IGNORECASE))

if __name__ == "__main__":
    main()
