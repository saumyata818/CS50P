def main():
    message=input("input:")
    msg_wo=shorten(message)
    print("Output:" + msg_wo)
def shorten(word):
    wo_vowels = ""
    for letter in word:
        if not letter.lower() in ["a", "e", "i", "o", "u"]:
            wo_vowels += letter
    return wo_vowels



if __name__ == "__main__":
    main()
