#Creates a word list
import random

def get_secret_word():
    word_bank = ["HAIR","T-POSE","MARKER","DAB","ROCK","FORTNITE","PASTA","COPY","HELLO","INTERNET","PYTHON","MONTY","TOMMY","GOOGLE","BING","MONEY","CAR","PLANE","BOAT","TRAIN","MOVIE"]
    num = random.randint(0,20)
    return word_bank[num]
