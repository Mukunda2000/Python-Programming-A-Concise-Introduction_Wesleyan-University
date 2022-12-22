def problem2_6():
    import random
    """ Simulates rolling 2 dice 100 times """
    # Setting the seed makes the random numbers always the same
    # This is to make the auto-grader's job easier.
    random.seed(431)  # don't remove when you submit for grading
    for i in range(0,100):
        l1=(random.randint(1,6))
        l2=(random.randint(1,6))
        print(l1+l2)

#problem2_6()