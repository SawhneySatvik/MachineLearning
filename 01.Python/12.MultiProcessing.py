import multiprocessing
import multiprocessing.process
import time

def square_numbers():
    for i in range(5):
        time.sleep(2)
        print("Square:",i**2)
        
def cube_numbers():
    for i in range(5):
        time.sleep(2)
        print("Cube:i",i**3)


if __name__ == '__main__':
    time1 = time.time()
            
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(time.time()-time1)