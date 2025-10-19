import numpy as np

def random (number: int=1)->int:
    """_summary_

    Args:
        number (int, optional): _description_. Defaults to 1.

    Returns:
        int: _description_
    """
    
    count = 0
    
    while True:
        count +=1
        predic_number = np.random.randint(1,101)
        if number == predic_number:
            print('You are right ')
            break
            
    return count

if __name__ == '__main__':            
    random()    