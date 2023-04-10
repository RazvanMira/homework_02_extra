minutes = int(input("Introduce the number of minutes of air time.\n"))
texts = int(input("Introduce the number of text messages.\n"))
base_charge = 15
call_center_fee = 0.44
total = 0
if minutes <= 50 and texts <= 50:
    print("The base charge for the cell phone plan is $" + "{:.2f}".format(base_charge))
    print("The 911 call center fee for the cell phone plan is $" + "{:.2f}".format(call_center_fee))
    print("The tax for the cell phone plan is $" + "{:.2f}".format((base_charge + call_center_fee) * 0.05))
    print("The total charge for the cell phone plan is $" + "{:.2f}".format(base_charge + call_center_fee + (base_charge + call_center_fee) * 0.05))
elif minutes > 50 and texts <= 50:
    print("The base charge for the cell phone plan is $" + "{:.2f}".format(base_charge))
    print("The additional minutes charge is $" + "{:.2f}".format((minutes - 50) * 0.25))
    print("The 911 call center fee for the cell phone plan is $" + "{:.2f}".format(call_center_fee))
    print("The tax for the cell phone plan is $" + "{:.2f}".format((base_charge + call_center_fee + ((minutes - 50) * 0.25)) * 0.05))
    print("The total charge for the cell phone plan is $" + "{:.2f}".format(base_charge + call_center_fee + (base_charge + call_center_fee + ((minutes - 50) * 0.25)) * 0.05 + (minutes - 50) * 0.25))
elif minutes <= 50 and texts > 50:
    print("The base charge for the cell phone plan is $" + "{:.2f}".format(base_charge))
    print("The additional texts charge is $" + "{:.2f}".format((texts - 50) * 0.15))
    print("The 911 call center fee for the cell phone plan is $" + "{:.2f}".format(call_center_fee))
    print("The tax for the cell phone plan is $" + "{:.2f}".format((base_charge + call_center_fee + ((texts - 50) * 0.15)) * 0.05))
    print("The total charge for the cell phone plan is $" + "{:.2f}".format(base_charge + call_center_fee + (base_charge + call_center_fee + ((texts - 50) * 0.15)) * 0.05 + (texts - 50) * 0.15))
elif minutes > 50 and texts > 50:
    print("The base charge for the cell phone plan is $" + "{:.2f}".format(base_charge))
    print("The additional minutes charge is $" + "{:.2f}".format((minutes - 50) * 0.25))
    print("The additional texts charge is $" + "{:.2f}".format((texts - 50) * 0.15))
    print("The 911 call center fee for the cell phone plan is $" + "{:.2f}".format(call_center_fee))
    print("The tax for the cell phone plan is $" + "{:.2f}".format((base_charge + call_center_fee + ((minutes - 50) * 0.25) + ((texts - 50) * 0.15)) * 0.05))
    print("The total charge for the cell phone plan is $" + "{:.2f}".format(base_charge + call_center_fee + ((minutes - 50) * 0.25) + ((texts - 50) * 0.15) + (base_charge + call_center_fee + ((minutes - 50) * 0.25) + ((texts - 50) * 0.15)) * 0.05))