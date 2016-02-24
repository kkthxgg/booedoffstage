i = 0 
numbers = []

def myloop(starter):
    print "hey, i got a starter %r "% starter
    i = starter    
    print "hey, i got an i  %r "% starter
    while i < 6: 
        print "empty print"
        print "At the top i is %d " % i
        #numbers.append(i)

        i = i + 1 
        print "numbers now :", numbers
        print "At the bottom i is %d " %i
    print "whew, that while loop was a lot of work, right?!!?"

    for j in range(0,starter):
        print "I'm the better loop because i work! here's iteration %r " % j

    
myloop(6)

print "The numbers: " 

for num in numbers:
    print num
