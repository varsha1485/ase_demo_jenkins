def check_palindrome():
    # 🔧 Change this input string to test different cases
    input_string = "madam"

    # Normalize the input (remove spaces, make lowercase if needed)
    cleaned = input_string.replace(" ", "").lower()

    if cleaned == cleaned[::-1]:
        print("SUCCESS")
    else:
        raise Exception("ERROR")

# Run the function
check_palindrome()
