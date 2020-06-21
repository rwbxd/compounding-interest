def variableInterest(principle, invest, take_out, interest_rate, years):
	taken_out = int(principle * take_out) # This code could go in the new_principle, but I want to find a way to print the amount taken out
	print("You take out $" + str(taken_out))
	new_principle = int((principle - (taken_out) + invest) * (1 + interest_rate))
	print("New principle is $" + str(new_principle))
	years -= 1
	if years > 0:
		variableInterest(new_principle, invest, take_out, interest_rate, years)
	else:
		again = input("Again?\n")
		if again == "y" or again == "Y":
			userPrompts(new_principle)
		else:
			return

def principlePrompt():
	principle = int(input("How much are you starting with?\n"))
	userPrompts(principle)

def userPrompts(principle):
	invest = int(input("How much are you investing per year?\n"));
	take_out = int(input("What percent are you taking out per year?\n"))/100;
	interest_rate = int(input("Interest rate?\n"))/100;
	years = int(input("How many years?\n"));
	variableInterest(principle, invest, take_out, interest_rate, years)

principlePrompt();

# variableInterest(0,10000,0,.05,2) Test Code

input("Press ENTER to exit");
