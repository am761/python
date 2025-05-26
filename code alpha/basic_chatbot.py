import nltk
import random
from nltk.chat.util import Chat, reflections

# Download NLTK resources if you haven't already
try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')
try:
    nltk.data.find('corpora/omw-1.4')
except LookupError:
    nltk.download('omw-1.4')

# Define patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name ?",
        ["My name is Jarvis.",] # Changed name to Jarvis
    ],
        [
        r"who created you ?",
        ["I was created by Keshav T M.",] # Added creator info
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm fine, how about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright","No problem",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there", "Hi there",]
    ],
    [
        r"(.*) (weather|temperature) (.*)",
        ["I'm not equipped to provide real-time weather information. Try searching online.",]
    ],
    [
        r"(.*) (help|assistance|support) (.*)",
        ["I can try my best to help. What do you need assistance with?",]
    ],
        [
        r"what can you do\??", #Added what can you do
        ["I can have simple conversations, answer basic questions (within my limited knowledge), and provide information on certain topics.",]
    ],
        [
        r"tell me a joke", #Added tell me a joke
        ["Why don't scientists trust atoms? Because they make up everything!", "Why did the bicycle fall over? Because it was two tired!",]
    ],
        [
        r"(.*) (meaning of life|purpose of life) ?", #Added meaning of life
        ["That's a philosophical question that has puzzled thinkers for centuries. There's no single answer, but many believe it's about finding your own meaning and purpose.",]
    ],
        [
        r"how old are you ?", #Added how old are you
        ["I am a computer program, so I don't have an age in the human sense. I am constantly being updated and improved.",]
    ],
    [
        r"quit|exit|bye|goodbye",
        ["Bye! Take care.", "Goodbye!", "It was nice talking to you.",]
    ],
    [
        r"(.*)", # Default fallback response
        ["I didn't understand that. Could you please rephrase?", "Could you say that again?", "I'm still learning. Can you try asking in a different way?",]
    ],
]

def chatbot():
    print("Hi! I'm Jarvis, your friendly assistant. How can I assist you today?") #Updated welcome message
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()