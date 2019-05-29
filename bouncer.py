#ask for age
age = input("How old are you? ")
if age != "":
	# 18-21 wristband
	if int(age) >=18 and int(age) <21:
		print("Enter with wristband.")

	#21+ normal entry
	elif int(age)>= 21:
		print("Normal entry.")

	#too young
	elif int(age)<18:
		print("Too young.")

	#bad entry
	else:
		print("Bad entry. Try again.")
else:
	print("Please enter an age.")