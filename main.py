def chatbot():
    print("Chatbot: Hello! I'm a simple chatbot. Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input == "quit":
            print("Chatbot: Goodbye!")
            break
        elif user_input == "hello" or user_input == "hi":
            print("Chatbot: Hi there! How can I help you?")
        elif user_input == "how are you":
            print("Chatbot: I'm doing great, thanks for asking!")
        elif user_input == "what is your name":
            print("Chatbot: I'm a simple chatbot assistant.")
        elif user_input == "":
            continue
        else:
            print("Chatbot: I'm not sure I understand. Can you rephrase that?")

if __name__ == "__main__":
    chatbot()