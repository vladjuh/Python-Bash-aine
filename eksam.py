import os.path

def calculate():
	file_exists1 = os.path.exists('firstnumber.txt')
	file_exists2 = os.path.exists('secondnumber.txt')
	miljon = 100000

	if file_exists1 == True:
		with open('firstnumber.txt') as f:
			number1 = f.readline()
	
	else:
		print('there is no file firstnumber.txt')

	if file_exists2 == True:
		with open('secondnumber.txt') as f:
			number2 = f.readline()
	
	else:
		print('there is no file secondnumber.txt')

	summa = int(number1) + int(number2)
	summastr = str(summa)

	if summa > miljon:
		with open('miljon2r.txt', 'w') as f:
			f.write(summastr)
	else:
		with open('summary.txt', 'w') as f:
			f.write(summastr)			

	i = summa
	while i < 20:
  		print('Tere!')
  		i += 1

calculate()
