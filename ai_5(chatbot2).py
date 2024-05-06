import random
import datetime
import re           #for regular expression matching

# Define responses for the chatbot
responses = {
    "hi": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "bye": ["Goodbye!", "See you later!", "Have a great day!"],
    "how are you": ["I'm good, thank you!", "I'm doing well, thanks for asking!"],
    "what is your name": ["I'm just a humble chatbot!", "I'm ChatBot, nice to meet you!"],
    "who created you": ["I was created by OpenAI.", "My creator is a team of talented developers at OpenAI."],
    "what is your purpose": ["My purpose is to assist you with any questions or tasks you have!",
                             "I'm here to help you with anything you need."],
    "what is the weather like today": ["I'm sorry, I don't have access to real-time weather information.",
                                       "You might want to check a weather website or app for that."],
    "what is the capital of France": ["The capital of France is Paris.", "Paris is the capital city of France."],
    "what is the current time": ["The current time is {time}.", "It's currently {time}."],
    "what is the current date": ["Today's date is {date}.", "It's {date} today."],
    "default": ["I'm sorry, I didn't understand that.", "Could you please repeat that?", "I'm not sure what you mean."]
}


def get_current_time():
    """
    Get the current time.
    """
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return current_time


def get_current_date():
    """
    Get the current date.
    """
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    return current_date


def evaluate_expression(expression):
    """
    Evaluate arithmetic expressions.
    """
    try:
        result = eval(expression)       #eval used for arithmetic opression evaluation, below in resp func
        return str(result)
    except Exception as e:
        return "Error: " + str(e)


def chatbot_response(message, user_name):
    """
    Generate a response from the chatbot based on the user's message, their name, real-time information, and basic functionalities.
    """
    message = message.lower()

    if "bye" in message:
        return random.choice(responses["bye"])
    elif "name" in message:
        return random.choice(responses["what is your name"])
    elif "time" in message:
        return random.choice(responses["what is the current time"]).format(time=get_current_time())
    elif "date" in message:
        return random.choice(responses["what is the current date"]).format(date=get_current_date())
    elif any(op in message for op in ['+', '-', '*', '/']): #evaluating arithmetic expression
        expression = re.findall(r"[-+]?\d*\.\d+|\d+|[-+*/]", message) #finds and extracts all arithmetic opression
        expression = ''.join(expression) #joins the arithmetic operators with expression 
        return evaluate_expression(expression) #evaluate and give answer
    else:
        for key in responses:
            if key in message:
                return random.choice(responses[key])
        return random.choice(responses["default"])


def main():
    print("Welcome to the ChatBot!")
    user_name = input("What's your name? ")
    print(f"Hi, {user_name}!")

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input, user_name)
        print("ChatBot:", response)
        if "bye" in user_input:
            break


if __name__ == "__main__":  #ensuring that script runs directly
    main()
