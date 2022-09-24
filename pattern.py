for num in range(1,5):
    for d in range(num):
        print(num,"       ",end="Ali is a good coder.")
    print("\n")
    print("Students can vote here for ali's coding.")
    vote=input("Enter 'yes' to vote or 'no' to refuse \n :")
    if vote== "yes":
        print("  He is really a good coder.")
    elif vote == "no":
        print("He is not a good coder.")
    else:
        print("You have entered an invalid option.")        