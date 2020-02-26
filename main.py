import numpy as np
number = np.random.randint(1,100)

def game_core(number):
    count = 0
    left = 0
    right = 100
    while True:
        count += 1
        otr = right - left
        predict = left + otr // 2
#        print (number, count, left, right, otr, predict)
        if number == predict: break          
        elif number > predict:
            if otr == 1: 
              count += 1
              break
            else: 
                left = (right + left)//2
        elif number < predict:
            if otr == 1: 
              count += 1
              break
            else: 
               right = (right + left)//2
    print (number, count)
    return(count)
  
  def score_game(game_core):
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)
  
  score_game(game_core)
