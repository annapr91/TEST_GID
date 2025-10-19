import numpy as np

""""""
number = np.random.randint(1,101)
print(number  )
count = 0

while True:
    count+=1
    predict_number = int(input('Guess the number'))
    
    if predict_number > number :
        print('Number should be less ')
        
    elif predict_number < number:
        print('Numebr should be higher ')
    else:
        print(f'You gues the number {number}, count number {count}')
        break