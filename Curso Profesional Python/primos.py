def run(num: int)-> bool:
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num > 2 and num % 2 == 0:
        return False
    else:
        for i in range(3, num):
            if num % i == 0:
                return False
    return True
        
    

if __name__ == '__main__':
    print(run(19))