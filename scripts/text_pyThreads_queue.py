# import libraries
import threading
import os
import queue

path_to_file        = "temp-files/"
file_name           = "attempt2"
target              = op('table1')
frameStart          = op('execute1')

myQ                 = queue.Queue()

target.store('myQ', myQ)

def workFucnt1(path_to_file, file_name, myQ):

    myQ.put("Processing")

    ouptput_file        = path_to_file + file_name + '.txt'
    working_file        = open(ouptput_file, 'w')

    working_file.write("Start Working Function")

    for number in range(100000):
        working_file.write("\nFor loop {} entry".format(number))

    working_file.write('\nEnding working Function')
 
    working_file.close()

    myQ.put("Ready")

    return

frameStart.par.framestart = 1

# workFucnt1(path_to_file, file_name, myQ)

myThread            = threading.Thread(target=workFucnt1, args=(path_to_file, file_name, myQ,))
myThread.start()
