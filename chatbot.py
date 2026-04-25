def chatbot():
    print("AI Chatbot (type 'exit' to stop)")
    
    responses = {
        "hello": "Hello! How can I help you?",
        "name": "I am your AI chatbot.",
        "bye": "Goodbye!",
        "help": "You can ask me simple questions."
    }

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("Bot: Goodbye!")
            break

        response_found = False

        for key in responses:
            if key in user_input:
                print("Bot:", responses[key])
                response_found = True
                break

        if not response_found:
            print("Bot: Sorry, I don't understand.")

chatbot()