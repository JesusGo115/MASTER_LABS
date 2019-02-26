#Created by: Jonathan J. Quintero Ramos and Jesus "Chuy" Gomez
#finished on 2/09/2019
#Created for Cst205 professor Wes at CSUMB
#The following code uses pickle to de-serialize a pickled code (a serilzlized data)
#By looping through the file's data which is strored on a different variable
#This variable is then used by a function to see what intensities there are of the rgb colors of the image.
#it is then sent to another function in which an svg image of the data's histogram is created

import pickle 
# Part of python3 to deserialize data is imported, part of python3
import hw1_hist_plotter as hp
# The following was imported to use the data conversion of the function and generate the histogram.




def task2(m):
    red = []
    green = []
    blue = []

    data = open(m, 'rb')
    newData = pickle.load(data)
    data.close()
    
    for i in range(len(newData)):
        for j in range(len(newData[i])):
            red.append(int(newData[i][j][0]))
            green.append(newData[i][j][1])
            blue.append(newData[i][j][2])

    red.sort()
    green.sort()
    blue.sort()

    master = [red, green, blue]

    return master

hp.hist_plotter(task2('image_matrix'))
#task2(first,second,newData)
##hp.hist_plotter(task2(first,second,newData))
#The function to make the histograms is then used with the function as part of its parametes
