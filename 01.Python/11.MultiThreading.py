import threading
import time

def print_num():
    for i in range(5):
        time.sleep(2)
        print(i)
        
def print_letter():
    for letter in 'abcde':
        time.sleep(2)
        print(letter)
        
# t=time.time()
# print_num()
# print_letter()
# finished_time = time.time()-t
# print(finished_time)

t1 = threading.Thread(target=print_num)
t2 = threading.Thread(target=print_letter)

time1 = time.time()

t1.start()
t2.start()

t1.join()
t2.join()

print(time.time()-time1)