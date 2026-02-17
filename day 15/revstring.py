def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# Example usage
if __name__ == "__main__":
    user_input = input("Enter a string: ")
    result = reverse_string(user_input)
    print(f"Original: {user_input}")
    print(f"Reversed: {result}")
