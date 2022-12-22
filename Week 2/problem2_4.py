def problem2_4():
    """ Make a list of 10 random reals between 30 and 35 """
    import random
    random.seed(70)
    lis=[]
    i=1
    while(i<=10):
        lis.append((random.uniform(0,5))+30)
        i+=1
    print(lis)

#problem2_4()