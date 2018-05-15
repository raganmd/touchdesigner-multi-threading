import threading
import os

path_to_file        = "temp-files/"
file_name           = "attempt1"

def workFucnt1(path_to_file, file_name):
    ouptput_file        = path_to_file + file_name + '.txt'
    working_file        = open(ouptput_file, 'w')

    working_file.write("Start Working Function")

    for number in range(100000):
        working_file.write("\nFor loop {} entry".format(number))

    working_file.write('\nEnding working Function')
 
    working_file.close()

    return

# un-comment this line below to see the process block touch
# workFucnt1(path_to_file, file_name)

# un-comment the bottom two lines to see the process
# execute without blocking Touch
myThread            = threading.Thread(target=workFucnt1, args=(path_to_file, file_name,))
myThread.start()