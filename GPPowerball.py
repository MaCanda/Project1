#-------------------------------------------------------------------------------
# Name:        Greenphire Powerball program
# Purpose:
#                This program allows the Greenphire employees to enter their
#                favorite numbers and program computes the winning powerball
#                number based on which number has been most selected as favorite
#
# Author:      Maria Canda
#
# Created:     01/11/2017
# Copyright:   (c) majitc 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
##import random
##import numpy as np

def main():
        Emp = []


        #enter Emp name and favorite numbers
        intnumEmp = 0
        Empfave = []
        y=0

        for i in range(7):
            Empfave.append(range(i,7))

        while True:
            name = input('Enter Employee name')
            Empfave[0] = name
            myNum = input('select 1st # -1 thru 69:' )
            Empfave[1] = int(myNum)
            inputstatement = 'select 2nd # -1 thru 69 excluding ' + str(Empfave[1])
            myNum = input(inputstatement)
            Empfave[2] = int(myNum)
            inputstatement = 'select 3rd # -1 thru 69 excluding ' + str(Empfave[1]) + ' and ' + str(Empfave[2])
            myNum = input(inputstatement)
            Empfave[3] = int(myNum)
            inputstatement = 'select 4th # -1 thru 69 excluding ' + str(Empfave[1]) + ' , ' + str(Empfave[2]) + ' and ' + str(Empfave[3])
            myNum = input(inputstatement)
            Empfave[4] = int(myNum)
            inputstatement = 'select 5th # -1 thru 69 excluding ' + str(Empfave[1]) + ' , ' + str(Empfave[2]) + ' , ' + str(Empfave[3]) + ' and ' + str(Empfave[4])
            myNum = input(inputstatement)
            Empfave[5]= int(myNum)
            inputstatement = 'select Power Ball # (1 thru 26):'
            myNum = input(inputstatement)
            Empfave[6] = int(myNum)
            Emp.append(Empfave[0:7])
            y += 1
            Answer = input('Enter another Employee? (Y or N)')
            if Answer == 'N' or Answer == 'n':
                break
            elif Answer == 'Y' or Answer == 'y':
                iter
            else:
                raise Exception('Answer must be Y or N')
        intnumEmp = y


##    print(Emp)
    # count the number of duplicates

        counts = {}
        countp = {}
        for i in range(intnumEmp):
            for j in range(1,7):
                if j == 6:
                    #create dictionary of 6th number and their counts
                    countp.setdefault(Emp[i][j], 0)
                    countp[Emp[i][j]] = countp[Emp[i][j]] + 1
                else:
                    # create a dictionary of favorite numbers and their counts only first 5 numbers
                    counts.setdefault(Emp[i][j], 0)
                    counts[Emp[i][j]] = counts[Emp[i][j]] + 1



    ##print(counts)
    ##print(countp)

    #work on the winning first five numbers

        kys=list(counts.keys())
        val=list(counts.values())



        #get unique counts
        win5= [0,0,0,0,0]
        highs=[0,0,0,0,0]
        descval =sorted(val,reverse=True)
        ##print(descval)

        #get the unique counts maximum of 5
        i=0
        for j in descval[0:5]:
            if j not in highs:
                if i < 5:
                    highs[i] = j
                    i += 1
    ##print(highs)

        #get the keys for the top 5 values
        i = 0
        for j in highs:
            for k,v in counts.items():
                if v==j:
                    if i < 5:
                        win5[i] = k
                        i += 1
    ##print(win5)

    #work on the winning powerball (6th) number

        kysp=list(countp.keys())
        valp=list(countp.values())

    ##print(val.sort(reverse=True))
        #for i in descval:
            #get unique counts
        winp= 0
        highp=0
        descvalp =sorted(valp,reverse=True)
    ##print(descvalp)

        #get the unique counts , since descvalp is already sorted, just get 1

        highp = descvalp[0]
    ##print(highs)

    #get the key for the winning powerbal number
        for k,v in countp.items():
            if v==highp:
                winp = k
    ##print(highp)
    ##print(winp)

        #display the employees and the corresponding number entries
        for i in range(intnumEmp):
            for j in range(7):
                if j < 6:
                    print(Emp[i][j], end = ' ')
                else:
                    print('Powerball: ' + str(Emp[i][j]) , end = '\n')

        print('Powerball winning number:' , end = '\n')
        #display the final powerball number
        for i in range(5):
            print(win5[i], end = ' ')

        print('Powerball: ' + str(winp))




if __name__ == '__main__':
    try:
        main()

    except Exception as err:
        print('An exception occurred.' + str(err))






