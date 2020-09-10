def principalPrompt():
	principal = int(input("How much are you starting with?\n"))
	userPrompts(principal)

def userPrompts(principal):
	invest_amount = int(input("How much are you investing per year?\n"));
	take_out = float(input("What percent are you taking out per year?\n"))/100;
	interest_rate = float(input("Interest rate? (In percent)\n"))/100;
	years = int(input("Compound for how many years?\n"));
	variableInterest(principal, invest_amount, take_out, interest_rate, years)

def variableInterest(principal, invest_amount, take_out, interest_rate, years):
	taken_out = int(principal * take_out) #Calculate amount to take out
	if take_out != 0:
		principal -= taken_out #Take out calculated amount
		print(f"You take out ${taken_out}")

	#Interest forumla A = P(1+r)^1, where A is value after interest,
	#P is the principal, r is the interest rate.
	#
	#I could use the formula A = P(1+r)^Y, where Y is the years compounded,
	#but I want to see the principal for each year.
	new_principal = int((principal + invest_amount) * (1 + interest_rate))
	print(f"New principal is ${new_principal}")

	#Check if there's more interest to be calculated
	years -= 1
	if years > 0:
		variableInterest(new_principal, invest_amount, take_out, interest_rate, years)
		#This breaks the PEP-8 standard, but it's the only line that does so
		#Therefore it's staying as is for now
		#The standard with line breaks looks ugly in my opinion and this context
	else:
		while True:
			again = input("Keep new principal with different settings? (Y/N)\n")
			again = again.lower() #New line to conform to PEP-8 80 char limit
			if again in ["y", "yes"]: #Only way I know to validate input, haha
				userPrompts(new_principal)
				break
			elif again in ["n", "no"]:
				retry()
				break
			else:
				print("Invalid input!")

def retry():
	retry = input("Press ENTER to restart, type exit to close the program\n");
	if retry.lower() == "exit":
		exit()
	else:
		principalPrompt()

principalPrompt();
