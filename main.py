import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?"]
    ],
    [
        r"hi|hello|hey",
        ["Hello", "Hey there"]
    ],
    [
        r"what is your name?",
        ["I am a bot created by OpenAI. You can call me ChatGPT."]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you! How can I help you today?"]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day."]
    ],
    [
        r"(.*)",
        ["I'm not sure about that. Can you please rephrase or ask something else?"]
    ],
]

def chatbot():
    print("Hi! I'm TestingBot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()


