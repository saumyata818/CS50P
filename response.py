from validator_collection import checkers
print('Valid') if checkers.is_email(input("What's your email address? ")) == True else print('Invalid')


