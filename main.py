def Symmetric(R):
    temp = []
    for a1, a2 in R:
        sym = False
        for b1, b2 in R:
            if(b1 == a2 and b2 == a1):
                sym = True
        if(sym == True):
            tempval = True
            temp.append(tempval)
        else:
            tempval = False
            temp.append(tempval)
    IsSym = True
    for a in temp:
        if(a == False):
            IsSym = False
    if(IsSym == True):
        print("Relation is symmetric.")
    else:
        print("Relation is not symmetric.")
print("Example: Symmetric([(1,2),(2,1),(4,1),(1,4)])")
Symmetric([(1,2),(2,1),(4,1),(1,4)])
print("Example 2: Symmetric([('a','b'),('b','c'),('b','a')])")
Symmetric([('a','b'),('b','c'),('b','a')])
