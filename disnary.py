from logging.handlers import MemoryHandler
from turtle import update

## dictionary method [program]

mydis={
    "sumii":"is a coder",
    "robot": "is a machiine",
    "marks": [2,3,5],
     "secoundis": {'sourav':'surname is joshi'}       #create new dictionary 
}
print(mydis["sumii"])
print(mydis["robot"])
print(mydis["marks"])
print(mydis['secoundis']['sourav'])


# some dictionary mrthod
print(mydis.keys())                  #print keys of the dictionary
print(mydis.values())                #print "keys": "values" of the dictionary
print(mydis.items())       #print the (keys & values) for all content of dictionary

#update method
updatemydis={
    "you are  bad": "sometimes"
}
mydis.update(updatemydis) #updates the dictionary by adding key-value pairs updatemydis
print(mydis)

#get method
print(mydis.get("sumii23")) #if the key is not presend in dictionary (.get) prints none in output 