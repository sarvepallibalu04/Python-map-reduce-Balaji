#Balaji Sarvepalli
#This is an example mapper

import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 7) : 
    Country, Ground, Matches, Won, Runs, Wkts, Balls  = datalist  #assign names

    # print intermediate key-value pairs to standard output
    print (Country,"\t", Matches)




    