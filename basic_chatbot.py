# =====================================================
# CodeAlpha Internship - Task 4: Basic Chatbot
# Language: Python
# Description: A simple rule-based chatbot
# =====================================================

import random
import re
import webbrowser
from urllib.parse import quote_plus


JOKES = [
    "Why did the computer go to the doctor? It had a virus!",
    "Why was the math book sad? It had too many problems!",
    "What do you call a bear with no teeth? A gummy bear!",
]

COMPLIMENTS = [
    "You bring something special just by being yourself. 😊",
    "Your effort matters, even when progress feels small. 🌟",
    "The way you keep learning is worth celebrating. 🎉",
]

HAPPY_ACTIVITIES = [
    "Send someone a kind message and let them know you appreciate them.",
    "Take a short stretch break and give yourself credit for showing up.",
    "Write down one small thing that went well today.",
    "Share a silly joke with someone who might enjoy a laugh.",
]


def _contains_phrase(user_input, phrases):
    """Check for whole-word phrases, so 'hi' does not match 'high'."""
    words = re.findall(r"[a-z0-9']+", user_input.lower())
    for phrase in phrases:
        phrase_words = re.findall(r"[a-z0-9']+", phrase.lower())
        phrase_length = len(phrase_words)
        if any(
            words[index:index + phrase_length] == phrase_words
            for index in range(len(words) - phrase_length + 1)
        ):
            return True
    return False


def chatbot_response(user_input):
    """
    Generate a response based on the user's input.
    """

    user_input = user_input.lower().strip()

    if _contains_phrase(user_input, ["hello", "hi", "hey"]):
        return "Hi! 👋 Welcome! How can I help you today?"

    elif _contains_phrase(user_input, ["how are you"]):
        return "I'm fine, thank you! 😊 How are you?"

    elif _contains_phrase(user_input, ["i am fine", "i'm fine", "fine", "good"]):
        return "That's great to hear! 😄"

    elif _contains_phrase(
        user_input,
        ["what is your name", "what's your name", "tell me your name"],
    ):
        return "I'm ChatBot, your friendly Python assistant! 🤖"

    elif _contains_phrase(user_input, ["who are you", "tell me about yourself"]):
        return "I'm a simple rule-based chatbot created using Python."

    elif _contains_phrase(user_input, ["what can you do", "help"]):
        return (
            "I can greet you, answer simple questions, "
            "have a basic conversation with you, and search the web. "
            "Try /joke, /compliment, or /activity for a little happiness, "
            "or type 'search <query>' to search."
        )

    elif _contains_phrase(user_input, ["thank you", "thanks"]):
        return "You're welcome! 😊 Happy to help."

    elif _contains_phrase(user_input, ["bye", "goodbye", "exit", "quit"]):
        return "Goodbye! 👋 Have a wonderful day!"

    else:
        return (
            "Sorry, I didn't understand that. 🤔\n"
            "Try 'hello', 'help', '/joke', '/compliment', "
            "'/activity', 'search <query>', or 'bye'."
        )


def search_web(query):
    """Open a web search for the supplied query in the default browser."""
    search_url = "https://www.google.com/search?q=" + quote_plus(query)
    if webbrowser.open(search_url, new=2):
        return f"Opening a web search for: {query}"
    return "I couldn't open a browser. Please check your default browser settings."


def main():
    """
    Main function to run the chatbot.
    """

    conversation_history = []

    print("=" * 50)
    print("       WELCOME TO THE PYTHON CHATBOT")
    print("=" * 50)
    print("ChatBot: Hello! 👋 I'm your friendly chatbot.")
    print("ChatBot: Type /help to see available commands.")
    print("-" * 50)

    # Loop continues until the user exits
    while True:
        try:
            user_input = input("You: ").strip()

            # Handle empty input
            if not user_input:
                print("ChatBot: Please enter something!")
                continue

            command = user_input.lower()
            if command == "/help":
                print(
                    "ChatBot: Commands: /help, /history, /clear-history, "
                    "/joke, /compliment, /activity, /quit. "
                    "You can also type 'search <query>' to search the web."
                )
                continue

            if command in ["/joke", "/compliment", "/activity"]:
                if command == "/joke":
                    response = random.choice(JOKES)
                elif command == "/compliment":
                    response = random.choice(COMPLIMENTS)
                else:
                    response = random.choice(HAPPY_ACTIVITIES)
                print("ChatBot:", response)
                conversation_history.append((user_input, response))
                continue

            if command == "/history":
                if not conversation_history:
                    print("ChatBot: No conversation history yet.")
                else:
                    print("ChatBot: Conversation history:")
                    for index, (past_input, past_response) in enumerate(
                        conversation_history, start=1
                    ):
                        print(f"  {index}. You: {past_input}")
                        print(f"     ChatBot: {past_response}")
                continue

            if command == "/clear-history":
                conversation_history.clear()
                print("ChatBot: Conversation history cleared.")
                continue

            if command == "/quit":
                print("ChatBot: Goodbye! 👋 Have a wonderful day!")
                break

            if command == "search":
                print("ChatBot: Enter a search term after 'search'.")
                continue

            # Search requests are recorded in history like other exchanges.
            if command.startswith("search "):
                query = user_input[len("search "):].strip()
                if not query:
                    print("ChatBot: Enter a search term after 'search'.")
                    continue
                response = search_web(query)
            else:
                response = chatbot_response(user_input)

            print("ChatBot:", response)
            conversation_history.append((user_input, response))

            # Stop the conversation when the user exits
            if _contains_phrase(command, ["bye", "goodbye", "exit", "quit"]):
                break

        except (KeyboardInterrupt, EOFError):
            print("\nChatBot: Goodbye! Have a wonderful day! 👋")
            break


# Run the chatbot
if __name__ == "__main__":
    main()
