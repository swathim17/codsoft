import re

# Define your response dictionary
responses = {
    "hello": "Hello! How can I assist you today?",
    "bye": "Goodbye! Have a great day!",
    "how are you": "I'm just a chatbot, but I'm here to help!",
    "thank you": "You're welcome!",
    "what is your name": "My name is ChatBot.",
    "where are you from": "I am an AI developed by IBM. My primary function is to provide information and answer user queries.",
    "who created you": "I was developed by a team of software engineers and data scientists.",
    "I need a help": "Sure! Just let me know how I can assist you.",
    "what is the weather": "I'm sorry,I am not equipped to provide weather information at the moment.",
    "what is the time now": "I am sorry, I cannot give you the current time as I don't have access to real-time clocks",
    "tell me a joke": "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "good morning": "Good morning! It's always a beautiful day.",
    "good afternoon": "Good afternoon! The sun is shining brightly.",
    "good evening": "Good evening! It's getting dark outside.",
    "good night": "Good night! Sleep tight and dream big."
}
    # Add more key phrases and responses here

def chatbot_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Search for keywords in user input
    for keyword, response in responses.items():
        if re.search(r'\b' + re.escape(keyword) + r'\b', user_input):
            return response

    # If no match found, provide a default response
    return "I'm sorry, I didn't understand. Could you please rephrase?"

def main():
    print("Welcome to the Chatbot! you can start chatting.Type 'bye' to exit.")
    while True:
        user_query = input("you: ")
        if user_query.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        bot_reply = chatbot_response(user_query)
        print("Chatbot:", bot_reply)

if __name__ == "__main__":
    main()
