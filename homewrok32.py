
deflist=[123,12,61,71,[23,51]]
def flattern(gl=None,*args):
    if gl>0:
        newlist=[]
        for i in range(gl):
            if type(args[i])==list:
                for a in range(len(args[i])):
                    newlist.append(args[i][a])
            else:
                newlist.append(args[i])
        print(newlist)
    else:
        print(list(args))
flattern(5,*deflist)


