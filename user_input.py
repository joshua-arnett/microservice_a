user_input = input("Enter 1-2 dates and a NHL team code in the form 'MM/DD/YYYY MM/DD/YYYY CODE': ")

if user_input != "":
    with open("user_input.txt", "w") as f:
        f.write(user_input)
