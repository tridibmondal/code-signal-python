https://app.codesignal.com/arcade/intro/level-2/bq2XnSr5kbHqpHGJC


def makeArrayConsecutive2(statues):
    statues.sort()
    s=statues[0]
    e=statues[len(statues)-1]
    c=0
    for i in range(s,e+1):
        if(i not in statues):
            c=c+1

    return c

