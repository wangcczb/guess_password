password = 'a123456'
g = 0
while g < 3:
	guess = input('請輸入密碼: ')
	if guess == password:
		print('登入成功!')
		break
	else :
		print('密碼錯誤! 還有', 2-g, '次機會!')
		g = g + 1