#creating a empty set
a= set()
print(type(a))

#adding value to empty set
a.add(5)
a.add(6)
a.add(5)
a.add(6)  #adding a value repeatedly does not change a set

#we can add tuple in sets
a.add((5,6,7))
print(a)
#adding list and dictionary  in sets (not  possible)
a.add([1,2,3])  #cannot add list in sets
a.add({5:2})    #cannot add dictionary  in sets
print(a)

#len()  (To find length of the set)
print(len(a))

#remove()  
a.remove(6)  #remove 6 from set by using remove function 
print(a)

#pop()
print(a.pop())  #remove tuple  from set
print(a)      
