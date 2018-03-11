'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

@author: Krzysztof Stezala
@email:  krzste09@outlook.com
'''

import sys, random, math

def manualInput(counter, dataList):                                 # specifing tasks manually
    for o in range(counter):
        print("Filling task no."+str(o+1))
        c = int(input("processing time> "))                         # computation time
        t = int(input("release period> "))                          # deadline
        d = int(input("deadline> "))                                # release period
        [dataList[o][0],dataList[o][1],dataList[o][2]]  = [c, t, d]
    print("Manual input complete!")

def generateInput(counter, dataList):                               # generating pseudo-random tasks
    print("Generating tasks...")
    for j in range(counter):
        c = random.randint(1,10)                                    # computation time
        d = random.randint(c,50)                                    # deadline
        t = random.randint(d,50)                                    # release period
        [dataList[j][0],dataList[j][1],dataList[j][2]]  = [c, t, d]
    print("Generating complete!")

def nww(num1, num2):
    num = num1 * num2
    while num2>0:
        t = num2
        num2 = num1%num2
        num1 = t
    nww = num/num1
    return nww

def main():
    print("# Schedulability tests #")
    print("Please enter number of tasks: ")                         # specifing number of tasks
    numOfTasks = input("> ")
    numOfTasks = int(numOfTasks)

    numOfParams = 3                                                 # number of parameters of the task
    tasksParams = [0] * numOfTasks                                  # defining the tasks' parameters array
    for i in range(numOfTasks):                                     # initialize the array to hold the tasks parameters
        tasksParams[i] = [0] * numOfParams
        
    ans = ''                                                        # variable to hold choice of the user
    while (ans!= 'y' and ans!= 'n'):
        print("Do you want to specify tasks parameters manually? (y/n)")
        ans = input("> ")

    if(ans == 'y'):
        manualInput(numOfTasks, tasksParams)
    else:
        generateInput(numOfTasks, tasksParams)
    
    u = 0                                                           # utilization of the processor
    for k in range(numOfTasks):                                     # calculating utilization of the processor
        u = u + tasksParams[k][0]/tasksParams[k][1]         
        
                                                                    
    hyperperiod = 0                                                 # hyperperiod calculation
    r = numOfTasks - 1
    temp = 0
    while r>=1:
        if r==(numOfTasks - 1):
            temp = nww(tasksParams[r-1][1],tasksParams[r][1])
        else:
            temp = nww(tasksParams[r-1][1],temp)
        r = r - 1
    hyperperiod = temp

    print("Hyperperiod: " + str(hyperperiod))

    ll_condition = numOfTasks*(math.pow(2,(1/numOfTasks))-1)        # calculating liu-leyland condition

    bb_condition = 1
    for n in range(numOfTasks):                                     # calculating bini-butazzo condition
        bb_condition = bb_condition * (1+(tasksParams[n][0]/tasksParams[n][1]))    

    print("params: c t d")                                          # printing tasks, utilization and tests
    for l in range(numOfTasks):
        print("task "+str(l+1)+": ", end='')
        for m in range(numOfParams):
            print(str(tasksParams[l][m]) + " ", end='')
        print("\n")
    print("Utilization of the processor: ", end=' ')
    print("".join("%.2f" % u))
    print("Liu-Leyland condition: ", end=' ')
    print("".join("%.2f" % ll_condition))
    print("Bini-Butazzo condition: ", end=' ')
    print("".join("%.2f" % bb_condition))
    
    if(u<=ll_condition and bb_condition<=2 and u<=1):                # checking schedulability
        print("Set of tasks is schedulable, sufficiency conditions are met")
    elif(u>ll_condition and bb_condition<=2 and u<=1):
        print("Liu-Leyland condition is not met.")
    elif(u<=ll_condition and bb_condition>2 and u<=1):
        print("Bini-Butazzo condition is not met.")
    elif(u>ll_condition and bb_condition>2 and u<=1):
        print("Liu-Leyland and Bini-Butazzo not met, but still schedulable.")
    else:
        print("Totally not schedulable.")


if __name__ == "__main__":
    main()



