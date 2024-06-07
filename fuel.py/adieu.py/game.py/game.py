import sys
import random

def main():
    while True:
        try:
            n = input("level:")
            while int(n)<0:
                n = input("level:")
            guess = random.randint(1,int(n))

            respons = input("Guess:")
            while int(respons) <0:
                respons = input("Guess:")


            #cheking if the guess is equal to the respons
            if int(guess) == int(respons):
                print("Just right!")
                sys.exit()
            else:

                while int(respons)< int(guess):
                    print("Too small!")
                    respons = input("Guess:")

                while int(respons) > int(guess):
                    print("Too large!")
                    respons = input("Guess:")

        except (EOFError, ValueError):
            pass

main()
