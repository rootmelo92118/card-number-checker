def cardNumberChecker(cardNumber):
    sum = 0
    cardNumber = list(cardNumber)
    index = (lambda x : 0 if len(x)%2 == 0 else 1) (cardNumber)
    for i in range(index,len(cardNumber),2):
        cardNumber[i] = str((lambda x : x*2 if x*2 < 10 else x*2-9) (int(cardNumber[i])))
    for i in cardNumber:
        sum += int(i)
    return (lambda SUM,CardNumber : {"Status": True,"Information":"This card numbers is valid."} if SUM%10 == 0 else {"Status": False,"Information":"This card numbers is invalid.\nThe check digit should be {} not {}.".format((lambda x,y : 10-x%10+int(y[-1]) if 10-x%10+int(y[-1]) < 10 else 10-x%10+int(y[-1])-10) (SUM,CardNumber),CardNumber[-1])}) (sum,cardNumber)

print(cardNumberChecker(input("card Numbers : "))["Information"])