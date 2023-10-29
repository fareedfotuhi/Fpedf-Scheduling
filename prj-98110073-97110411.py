from asyncio import tasks
from asyncio.windows_events import NULL
from pickle import TRUE
import random
from collections import deque
from math import gcd
from math import floor

class task:
    def __init__(self, period, utilization,id):
        self.id=id
        self.period = period
        self.utilization = utilization
        self.deadline = 0
        self.start=0
        self.end=0
        self.c =0
        self.x =0
        self.run = False

    def set_deadline(self, time):
        self.deadline = self.period -(time%self.period)
    def set_c(self,time):
        if time % self.period == 0:
            self.c=floor(self.utilization*self.period)
    def set_x(self):
        self.x = self.deadline/self.utilization

class Processor:
    def __init__(self, id):
        self.id = id
        self.task = NULL

    def assign_task(self, task):
        self.task= task

# class FpEDFAlgorithm:
#     def __init__(self, processors, tasks):
#         self.processors = processors
#         self.tasks = tasks

#     def schedule(self):
#         q = deque()
        
def Nmaxelements(list1, N):
    final_list = []
 
    for i in range(0, N):
        max1 = 0
 
        for j in range(len(list1)):
            if list1[j] > max1:
                max1 = list1[j]
 
        list1.remove(max1)
        final_list.append(max1)
 
    return final_list




######################################## main ##################################
def main():
    n = int(input("please enter number of tasks: "))
    u = float(input("please enter total utlization: "))
    if u > n:
        print("Invalid input")
        return 0 
    
    tasks = []
    sum_u = u
    next_sum_u = 0

    for i in range(1, n):
        next_sum_u = u * random.random() ** (1.0 / (n - i))
        tasks.append(task(utilization=sum_u - next_sum_u,period=random.choice(10,20,100),id=i))
        sum_u = next_sum_u

    tasks.append(task(utilization=sum_u,period=random.choice(10,20,100)),id=n)
    

    
    processors = []
    num_core = 16
    for i in range(num_core):
        processors[i].append(Processor(id=i+1))
        
    hyperperiod = tasks[0].period
    for i in tasks[1:]:
        hyperperiod = int(hyperperiod * i.period / gcd(hyperperiod, i.period))

    for i in tasks:
        i.set_c()
    
    curent_time = 0
    availabe_prosessors = []
    run_prosessors = []

    for i in processors:
        if i.task == 0:
            availabe_prosessors.append(i.id)
    for i in tasks:
        i.set_deadline(curent_time)
        i.set_x()
    mux_c = Nmaxelements(tasks,num_core)
    for i in tasks:
        for j in mux_c:
            if i.id == j.id:
                i.run = True
                i.c = i.c - 1
                break

    
    curent_time = curent_time + 1

    while curent_time <= hyperperiod:
        for i in tasks:
            i.set_deadline(curent_time)
            i.set_x()
        mux_c = Nmaxelements(tasks,num_core)
        for i in tasks:
            flag = 0
            for j in mux_c:
                if i.id == j.id:
                    flag = 1
                    i.run = True
                    i.c = i.c - 1
                    break
            if flag != 1:
                i.run = False



        curent_time = curent_time + 1

    # algorithm = FpEDFAlgorithm(processors, tasks)
    # algorithm.schedule()


if __name__ == "__main__":
    main()