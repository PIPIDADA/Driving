country = input('請問您是哪國人？')
age = input('請輸入您的年齡：')
age = int(age)
if country == '台灣':
    if age >= 18:
        print('您可以考駕照了！')
    else:
        print('您目前無法考取駕照！')
elif country == 'American':
    if age >= 16:
        print("You can try to get a driver's license!!")
    else:
        print("Sorry, you can't drive.") 
        print("To ride a bike is good for you!")

