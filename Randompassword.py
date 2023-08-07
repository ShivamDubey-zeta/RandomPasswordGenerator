import random
import string

def generate_password(words):
    # Combine the user input words
    combined_words = "".join(words)
    
    # Generate a random password using the combined words
    random_password = "".join(random.choice(combined_words) for _ in range(12))
    
    return random_password

def main():
    print("Welcome to the Random Password Generator!")
    
    user_input = input("Enter a series of words (separated by spaces): ")
    input_words = user_input.split()

    if not input_words:
        print("No words entered. Please provide at least one word.")
        return
    
    password = generate_password(input_words)
    
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
