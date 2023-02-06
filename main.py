import random

def start():
    print(‘Hello, I'm a magic ball, and I know the answer to any question you have’)
    print(What’s your name?')
    name = input()
    print("Hello, " + name)
    magic_ball_8()


def magic_ball_8():
    answers = ["Undoubtedly," "Predetermined," "No doubt," "Definitely yes," "You can be sure of it," "I think so," "Most likely," "Good prospects," "Signs say yes," "Yes," "It's not clear yet, try again, "Ask later", "Better not tell", "Can't predict now", "Concentrate and ask again", "Don't even think", "My answer is no", "Not according to me", "Prospects are not good", "Very doubtful"]
    print(‘Ask your question’)
    question = input()
    print(random.choice(answers))
    print(‘Do you want to ask one more question? Write yes or no’)
    final = input()
    if final == 'yes' :
        return magic_ball_8()
    else:
        print(‘Come back if you have any questions!’)

start()