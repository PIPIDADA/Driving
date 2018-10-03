country = input('請問您是哪國人？')
age = input('請輸入您的年齡：')
age = int(age)
if country == '台灣':
    if age >= 1 and age < 18:
    	print('您目前無法考取駕照！')
    else:
    	print('您可以考駕照了！')

