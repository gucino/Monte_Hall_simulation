# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 12:13:49 2021

@author: Tisana
"""
import numpy as np
import matplotlib.pyplot as plt


#input parameter
num_trial = 1000
num_door = 10
################################################################
################################################################
################################################################
#functions
def select_function():
    return np.random.randint(1,num_door + 1) #randint 1 to num_door

def car_location_function():
    return np.random.randint(1,num_door + 1) #randint 1 to num_door

def open_door(car_location,select_location):
    o_list = []
    for _ in range(num_door - 2):
        o = np.random.randint(1,num_door + 1)
        
        while o == car_location or o == select_location or o in o_list:
            #repeat until not open the car and selected location
            o = np.random.randint(1,num_door + 1)
        o_list.append(o)
    return o_list

def switch(open_location,select_location):
    o = np.random.randint(1,num_door + 1)
    
    while o in open_location or o == select_location:
        #repeat until not open the car and selected location
        o = np.random.randint(1,num_door + 1)
    return o   

def check_win_condition(select_location,car_location):   
    if car_location == select_location:
        return 1
    else:
        return 0
################################################################
################################################################
################################################################

stay_list = []
switch_list = []
door_list = np.arange(1,num_door)

for i in range(0,num_trial):
    print(i)
    select_location = select_function()
    car_location = car_location_function()
    open_location = open_door(car_location,select_location)
    
    #if stay
    stay_list.append(check_win_condition(select_location,car_location))
    
    #if switch
    select_location = switch(open_location,select_location)
    switch_list.append(check_win_condition(select_location,car_location))


stay_list = np.cumsum(stay_list)
switch_list = np.cumsum(switch_list)

    
#visualisation
plt.plot(stay_list,label = "stay (" + str(num_door) + " doors)")
plt.plot(switch_list,label = "switch (" + str(num_door) + " doors)")
plt.ylabel("cumulative sum of number of wins")
plt.xlabel("number of trail")
plt.legend()
plt.show()
    

