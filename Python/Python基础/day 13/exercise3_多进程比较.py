'''
exercise: exercise3_多进程比较
描述：

Author  : 郑超轩
Date    : 2020.02.28
'''
from time import time
from multiprocessing import Process,Queue
#1.473秒
"""
def main():
    total = 0
    number_list = [x for x in range(1, 10000001)]
    start = time()
    for number in number_list:
        total += number
    print(total)
    end = time()
    print('Execution time: %.3fs' % (end - start))
"""

def target_add(current_number,total_queue):
    totals = 0 
    for x in current_number:
        totals += x
    total_queue.put(totals) 

def main():
    processes =[]
    number_list = [x for x in range(1, 10000001)]
    total  = 0
    total_queue = Queue()
    index = 0
    """进行8个进程分配"""
    for _ in range(8):
        p = Process(target = target_add,args = (number_list[index:index+1250000],total_queue,))
        index+=1250000
        processes.append(p)
        p.start()
    start = time()
    for _ in processes:
        p.join()
    
    while not total_queue.empty():
        total+=total_queue.get()
    end = time()
    print(total)
    print('Execution time: %.3fs' % (end - start))




if __name__ == '__main__':
    main()
