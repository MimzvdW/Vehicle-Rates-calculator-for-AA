def menu():
    welcome_list = [" ",
                    "Welcome to the AA Calculator",
                    " ",
                    "Please select one of the following options:",
                    "1. Have a look at the previous entry.",
                    "2. Make a new entry.",
                    "3. Close the program"]
    for options in welcome_list:
        print(options)
menu()
options = int(input("Enter your choice:"))

while True:

    if options == 2:
        meters = int(input("How many meters have you traveled:"))
        km = meters/1000
        message_list = ["Here is the list of vehicles",
                    "1. Hatchback",
                    "2. SUV",
                    "3. Sports Car"]
        for options in message_list:
            print(options)

        vehicles = int(input("Please select one:"))

        import requests
        AA_Calc = 'https://raw.githubusercontent.com/tyrone0501/AA-Petrol-Price/main/Cars.json'
        response = requests.get(AA_Calc)
        response_json = response.json()

        siteresponse_H = response_json["Hatchback"]
        siteresponse_S = response_json["SUV"]
        siteresponse_SC = response_json["SportsCar"]

        if vehicles == 1:
            #cost = km * (response_json["Hatchback"]) #One way to do it
            cost = km * siteresponse_H
            description = input("Please type in your description of where you traveled and why?:")

        elif vehicles == 2:
            cost = km * siteresponse_S
            description = input("Please type in your description of where you traveled and why?:")

        elif vehicles == 3:
            cost = km * siteresponse_SC
            description = input("Please type in your description of where you traveled and why?:")

        else:
            print("Please enter a number between 1 to 3")

        import json

        entry = {
            "Cost": cost,
            "KM": km,
            "Description": description
            }
        json_object = json.dumps(entry, indent=4)
        with open("PreviousEntry.json", "w+") as outfile:
            outfile.write(json_object)

        outfile.close()

        menu()
        options = int(input("Enter your choice:"))

    if options == 1:
        import json

        with open("PreviousEntry.json", "r") as infile:
            data = json.load(infile)
        print("")
        print("Here is the previous entry")
        print("")
        print("Your amount of kilometers is", (data["KM"]), "KM")
        print("Your total cost is R", (data["Cost"]))
        print("Your Description:", (data["Description"]))

        infile.close()

        menu()

    if options == 3:
        print("Thank you for using our AA Calculator")
        exit()

    else:
        print("Please enter a number between 1 to 3")
        print("")
        menu()
        options = int(input("Enter your choice:"))

