def random_number():
    for i in range(3):
        yield i

def random_numbers_100():
    for i in range(100,110):
        yield i
        
def generator():
    yield from random_number()
    print("Next generator..")
    yield from random_numbers_100()


if __name__ == "__main__":
    gen = generator()
    
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(list(gen))