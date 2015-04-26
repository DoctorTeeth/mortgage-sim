import numpy as np
import random

class Loan:
    state = "normal" 
    balance = 100000

def chooseState(p,d):
    r1 = random.random() 
    r2 = random.random() 
    maybePrepay  = r1 < p
    maybeDefault = r2 < d
     
    if maybePrepay and maybeDefault:
        #randomly choose which bucket applies
        if random.random() < 0.5:
            return "prepay"
        else:
            return "default"
    elif maybePrepay:
        return "prepay"
    elif maybeDefault:
        return "default"
    else:
        return "normal"

def runSimulation(N,p,d):

    xs = [] 
    ys = []

    # create a pool of LOAN_COUNT loans with 100k principal each
    LOAN_COUNT = 100
    loans = []
    for i in range(LOAN_COUNT):
        loans.append(Loan())
    
    # the servicing account starts off empty 
    cash = 0 
    
    # we assume a 10 year mortgage with 4% rate
    # total cost of mortgage should be ~ 121,494
    interestRate = 0.04
    payAmount    = 1012 

    # we assume that defaults are recovered at 80%
    recoveryRate = 0.8

    # for each day in the simulation period 
    for i in range(1,N + 1):

        for loan in loans:

            # if the loan is still in the pool         
            if loan.state == "normal":

                # allow for state change
                loan.state = chooseState(p,d)  

                if loan.state == "default":
                    recovery = recoveryRate * loan.balance
                    cash = cash + recovery
                elif loan.state == "prepay":
                    cash = cash + loan.balance
                else:
                    # credit the payment to the cash account
                    thisPayment = min(payAmount,loan.balance)
                    cash = cash + thisPayment 
                     
                    # compute how much principal has been paid
                    interestDue = (loan.balance * interestRate) / 12
                    principalPaid = thisPayment - interestDue 
                    loan.balance = loan.balance - principalPaid

                    # get rid of loans that are basically done
                    if loan.balance < 0.01:
                        loan.state = "finished"

        # write the graph data
        xs.append(i)
        ys.append(cash)

    y = np.array(ys)
    x = np.array(xs)

    #scale down y for display
    y = y / 1000 
    
    return dict(x=x,y=y)

