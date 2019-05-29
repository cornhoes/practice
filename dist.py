print("How many kilometers did you run today?")
kms = input()
print("Okay! You said " + kms + " kilometers!")

#Y/N section i guess
while True:
	query = input(f"Is {kms} kilometers correct?")
	F1 = query[0].lower()
	if query == "" or not F1 in["y","n"]:
		print("Please confirm with \"yes\" or \"no\"!")
	else:
		break
if F1 == "y":
				miles = float(kms)/1.60934
				miles = round(miles,2)
				print(f"You ran {miles} miles today. Nice job!")
if F1 == "n":
				print("Oh dang :(")

#Y/N section!!!!!!!!! it worked!!!!!!!!!!!!!!!!!!!!!!! wow!!!!!!!!!
#really wasnt expecting that


