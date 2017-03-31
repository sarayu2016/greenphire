from collections import Counter
import random

#number of contestants in the program
names = []
numbers_entered = []
power_ball = []
notime = input('Number of users entering the contest:')
for j in range(0, int(notime)):
	number_int = []
	firstname = input('Enter your first name:')
	lastname = input('Enter your last name:')
	names.append([firstname, lastname])

	
	number = input("select 1st # (1 thru 69):")
	number_int.append(number)
	number = input("select 2nd # (1 thru 69 excluding"+ " " + number_int[0]+ "):")
	number_int.append(number)
	number = input("select 3rd # (1 thru 69 excluding"+ " " + number_int[0]+ ","+ number_int[1] + "):")
	number_int.append(number)
	number = input("select 4th # (1 thru 69 excluding"+ " " + number_int[0]+ ","+ number_int[1] +","+ number_int[2] +  "):")
	number_int.append(number)
	number = input("select 5th # (1 thru 69 excluding"+ " " + number_int[0]+ ","+ number_int[1] +","+ number_int[2] +","+ number_int[3]+ "):")
	number_int.append(number)
	number = input("select Power Ball # (1 thru 26):")
	number_int.append(number)
	power_ball.append(int(number))
	numbers_entered.append(number_int)
	
cnt_ball = Counter(power_ball)
for i in range(0, len(names)):
  print(names[i][0]+ " " + names[i][1]+  " "+ str(numbers_entered[i][0]) + " "+ str(numbers_entered[i][1]) +  " "+ str(numbers_entered[i][2]) +  " "+ str(numbers_entered[i][3]) +  " "+ str(numbers_entered[i][4]) +  " "+ 'Powerball:' +  " "+ str(numbers_entered[i][5]))
print("Powerball winning number:")
print(str(random.randint(1,70)) + " " + str(random.randint(1,70)) + " " + str(random.randint(1,70)) + " " + str(random.randint(1,70)) + " " + str(random.randint(1,70)) + " " + "Powerball:" +  " " + str(cnt_ball.most_common(1)[0][0]))

	    
