while True:
    user_input = input("Please enter a text: ")
    if user_input.isdigit():
        print("Error: Please enter a valid text.")
    else:
        reversed_text = user_input[::-1]
        print("The reversed text is: ", reversed_text)
        break