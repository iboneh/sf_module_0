import numpy as np
def gamecore(number):
    number = np.random.randint(1,100)
    count = 0
    left = 0
    right = 100

    while True:
        count += 1
        predict = (right + left)/2
#        print (number, count, left, right, predict)
        if number == predict: break
        elif number > predict:
            left = (right + left)/2
        elif number < predict:
            right = (right + left)/2
    print (number, count)

def score_game(gamecore):
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(gamecore(number))
    score = int(np.mean(count_ls))
    print(score)
    return(score)

score_game(gamecore)
