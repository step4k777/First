import numpy as np

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число
    
    Args:
        number(int, optional): Загаданное число. Defaults to 1
        
    Returns:
        int: Число попыток
    """
    
    count = 0
    min_number, max_number = 1, 100
    predict_number = np.random.randint(1,101)
    
    while min_number <= max_number:
        count += 1
        mid_number = (min_number + max_number)//2
        
        if mid_number < predict_number:
            min_number = mid_number + 1
        elif mid_number > predict_number:
            max_number = mid_number - 1
        else:
            return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов алгоритм угадывает число
    
    Args:
        random_predict([type]): функция угадывания
        
    Returns:
        int: среднее количество попыток
    """
    
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1,101, size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Алгоритм в среднем угадывает число за {score} попыток')
    return score


if __name__ == "__main__":
    #RUN
    score_game(random_predict)
    