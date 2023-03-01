import sys

data = input('input marks: ').lower()

#first remove all spaces
data = data.replace(' ', '')

#then check for having equals symbol (for counting credits with marks)
isCredits = '=' in data

#then split by comma
marks = data.split(',')

LETTERS = {'a': 90, 'b': 80, 'c': 70, 'd': 60, 'e': 50, 'f': 0}

marksList = []
creditsList = []
maximumCredit = 0
#loop through it
for mark in marks:
    #check if credits were counted and this mark does not contain it
    if isCredits and '=' not in mark:
        print('Error in input: please write the marks correctly!')
        sys.exit(0)

    if isCredits:
        #split the mark and credit
        m, c = mark.split('=')

        #find the lowest possible mark
        finalMarkMin = LETTERS[m[0]] + (('+' in m) * 5)
        finalMarkMax = (100,finalMarkMin+4)[finalMarkMin<95]

        #find the credit by using middle mark
        constant = int(c) / 100 #this is came out from the rule of (x/100)*c
        finalCreditMin = round(finalMarkMin * constant, 2)
        finalCreditMax = round(finalMarkMax * constant, 2)
        
        maximumCredit += int(c)

        marksList += [finalMarkMin]
        creditsList += [(finalCreditMin, finalCreditMax)]

        #print it
        print(f'{finalMarkMin} - {finalMarkMax}', end='    ')
        print(f'{finalCreditMin} - {finalCreditMax}/{c}')
        continue

    #find the lowest possible mark
    finalMarkMin = LETTERS[mark[0]] + (('+' in mark) * 5)
    finalMarkMax = (100,finalMarkMin+4)[finalMarkMin<95]

    marksList += [finalMarkMin]

    #print it
    print(f'{finalMarkMin} - {finalMarkMax}')

#print final averages
marksAvg = round(sum(marksList) / len(marksList), 2)
print('\nAverage: ', f'{marksAvg} - {marksAvg + 4}')

if isCredits:
    totalCreditsMin = round(sum(x[0]for x in creditsList), 2)
    totalCreditsMax = round(sum(x[1]for x in creditsList), 2)
    print(f'Credits: {totalCreditsMin} - {totalCreditsMax}/{maximumCredit}')
