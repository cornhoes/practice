print("Hello! What is your name? ")
name = input()
if name == "abigail":
	print("Oh, hello. I see you're in charge here.")
elif name == "alex":
	print("What a shame. Fined $10,000. Go directly to jail. Do not pass go. Do not collect $200.")
elif name == "marius":
	answer = input(f"Hello, {name}. Who wrote les mis? ")
	if answer == "victor hugo":
		print("Nice. :)")
	else:
		print ("Nope. Try again.")
		print(f"Hello, {name}. Who wrote les mis?")
		answer = input()
		if answer == "victor hugo":
			print("Nice. :)")
		else:
			print ("Nope. Try again. Last chance before self destruct sequence initiated.")
			print(f"Hello, {name}. Who wrote les mis?")
			answer = input()
			if answer == "victor hugo":
				print("Nice. :)")
			else:
				print ("nahhh u lost. Goodnight.")
elif name == "gabi":
	answer = input(f"Hello, {name}. Best place to travel? (please exclude articles)")
	if answer == "netherlands":
		print("dope. identity confirmed. proceed.")
	else:
		print ("INCORRECT. Try again.")
		print("Best place to travel? (exclude articles)")
		answer = input()
		if answer == "netherlands":
			print("u got it!! nice job :^)")
		else: 
			print: ("Fake Gabi. Goodnight.")
elif name == "adi":
	answer = input(f"Hello, {name}. security question: what is running? (please answer \"a _____\")")
	if answer == "lifestyle":
		print("u got it! access granted. you rock!!! :^)")
	else:
		print("nope. nice try. access denied. goodnight.")
else:
	print(f"Hello, {name}. Access denied. Goodnight.")