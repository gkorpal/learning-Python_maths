''' It prompts students for how many credits they have. Print whether of not
they have enough credits for graduation. (At Loyola University Chicago 120
credits are needed for graduation.) '''


credits = int(input('How many credits have you completed? '))
if credits >= 120:
    print("You are ready for graduation.")
else:
    d = 120 - credits
    print("Need to complete", d, "more credits to be able to graduate.")
