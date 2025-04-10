# chatbot.py
def chatbot_response(user_input):
    # Basic emotional responses based on keywords
    if "sad" in user_input.lower():
        return "I'm sorry you're feeling sad. I'm here for you. 💖 Do you want to talk about it?"
    elif "happy" in user_input.lower():
        return "That's great to hear! 😄 What made you happy today?"
    elif "anxious" in user_input.lower():
        return "I'm here with you. 🌸 Let's take a deep breath together."
    else:
        return "I’m here to listen, feel free to share how you’re feeling. 😊"
