import random

def generate_number():
    # Задаем вероятности выпадения чисел от 1 до 8
    probabilities = [0.01, 0.02, 0.04, 0.08, 0.16, 0.32, 0.64, 0.99]
    
    # Генерируем случайное число с заданными вероятностями
    number = random.choices(range(1, 9), weights=probabilities)[0]
    
    return number