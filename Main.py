import random
import string
#Generate a random password based on length and complexity.
def generate_password(length,complexity):
    if complexity=="low":
        chars=string.ascii_letters #only letters
    elif complexity=="medium":
        chars=string.ascii_letters+string.digits#Letters+Digits
    elif complexity=="high":
        chars=string.ascii_letters+string.digits+string.punctuation#letters+digit+symbols
    password=''.join(random.choice(chars) for _ in range(length))
    return password
def main():
    while True:
        print("STRONG RANDOM PASSWORD GENERATOR")
        try:
            length=int(input("Enter Password length:"))
        except ValueError:
            print("Invalid input!! Length should be a number.")
            return
        print("Select Complexity Level.")
        print("1.Low(letters only).")
        print("2.Medium(Letters+Numbers).")
        print("3.High(Letters+Numbers+Symbols).")
        print("4.Exit")
        choice=input("Enter your choice(1/2/3):")#do not use int here because choice always use string by defualt.
        if choice=="1":
            complexity="low"
        elif choice=="2":
            complexity="medium"
        elif choice=="3":
            complexity="high"
        elif choice=="4":
            print("Exiting the program!!God Bye!!!!")
            break
        else:
            print("Invalid Choice!!! Generating high by default")
            complexity="high"
        password=generate_password(length,complexity)
        print(f"Your Generated Password:{password}")
if __name__=="__main__":
    main()