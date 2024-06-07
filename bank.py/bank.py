greet_input=input("Greeting:").strip()

if greet_input.startswith("Hello"):
   print("$0")
elif  greet_input.startswith("h") or greet_input.startswith("How"):
    print("$20")
else:
    print("$100")


