def gamecore(number):
    import numpy as np
    number = np.random.randint(1,100)
    count = 0
    count_rnd = 0
    left = 0
    right = 100
    
    while True:
        count_rnd += 1
        predict_rnd = np.random.randint(1,100)
        if number == predict_rnd: break
    return (count_rnd)

    while True:
        count += 1
        predict = (right + left)/2
        if number == predict: break
        elif number > predict:
            left = (right + left)/2
        elif number < predict:
            right = (right + left)/2
    return (count)

    while True:
        count_l += 1
        predict_l = np.random.randint(1,100)
        if number == predict_l: break
        elif number > predict_l:
            left = (right + left)/2
        elif number < predict_l:
            right = (right + left)/2
    return (count_l)

def score_game(gamecore):
    count_sc = 0
    while True:
        count_sc < 1000
        count_sc += 1
        print (count_sc, number, predict, predict_rnd, predict_l)
#    score = int(np.mean(count_ls))
#    print(score)
#    return(score)

score_game(gamecore)
