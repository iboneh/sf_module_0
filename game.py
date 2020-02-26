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
    count_sc = 0
    while True:
        count_sc < 1000
        count_sc = count_sc + 1
        print (count_sc, number, predict)
#    score = int(np.mean(count_ls))
#    print(score)
#    return(score)

score_game(gamecore)
