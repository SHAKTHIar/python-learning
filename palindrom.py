user_input=input("ENTER YOUR INPUT:")
reversed_input=user_input[::-1]
if user_input==reversed_input:
    print(f"Yes This input {user_input} is a palindrome because we got the answer as {reversed_input}")
else:
    print(f"No this input {user_input} is not a palindrome because we got the answer as {reversed_input}")
