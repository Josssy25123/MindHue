import chatbot  # Import the chatbot

def main_menu():
    while True:
        print("\nWelcome to Mood Mate!")
        print("1. Write a Daily Journal Entry")
        print("2. Chat with the Mood Mate Bot")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            journal.write_journal()
        elif choice == "2":
            user_input = input("Say something to the bot: ")
            response = chatbot.chatbot_response(user_input)
            print(response)
        elif choice == "3":
            print("Goodbye! Take care. 💖")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
