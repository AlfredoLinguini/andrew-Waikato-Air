#document PLANPLANPLAN
name_list = []
price = (0)
auck_seats = (164)
ham_seats = (300)
wainui_seats = (127)
more_people = False
flight_place = False
firstc_loop = False
available_loop = False
name_loop = False
yes = {"yes", "y", "yes please daddy"}
no = {"no", "n", "oh hell nuh"}
from time import sleep
while more_people == False:
    print("Hello, and welcome to Waikato Airport.")
    while name_loop == False:
      f = input("What is your name? Minimum of 3 Characters\n").title()
      if len(f) < 3:
        print("Please Enter 3 or more character name")
        name_loop = False
      elif len(f) >= 3:
        name_list.append(f)
        print("Nice to meet you {}".format(f))
        name_loop = True
    while flight_place == False:
        place = input(
            "Where will you be flying too? Auckland, Hamilton or Wainuiomata?\n"
        ).title()
        if place == "Auckland":
            print("The next available flight for Auckland is 2:30pm tommorow")
            price = price + (125)
            auck_seats = auck_seats - (1)
            flight_place = True
        elif place == "Hamilton":
            print("The next available flight for Hamilton is 4pm tommorow")
            price = price + (90)
            ham_seats = ham_seats - (1)
            flight_place = True
        elif place == "Wainuiomata":
            print("The next available flight for Wainuiomata is 9am tommorow")
            price = price + (420)
            wainui_seats = wainui_seats - (1)
            flight_place = True
        else:
            print("Your opinion is not an option!")
            sleep(1)
            flight_place = False
    while available_loop == False:
        available = input("Are you able to make the next flight?\n").lower()
        if available in no:
            available_loop = False
        if available in yes:
            if place == "Auckland":
                print("{} seats are left".format(auck_seats))
                print("Great, that brings your total too ${}".format(price))
                available_loop = True
            if place == "Hamilton":
                print("{} seats are left".format(ham_seats))
                print("Great, that brings your total too ${}".format(price))
                available_loop = True
            if place == "Wainuiomata":
                print("{} seats are left".format(wainui_seats))
                print("Great, that brings your total too ${}".format(price))
                available_loop = True
    #add and show discounts here

    while firstc_loop == False:
        firstc = input("Do you want to fly first class?\n").lower()
        if firstc in yes:
            print("That will be $50")
            firstprice = price + (50)
            firstc_loop = True
        elif firstc in no:
            print("Just a normal ticket")
            firstc_loop = True
        else:
            firstc_loop = False
    others = input("Will there be other people coming with you?\n").lower()
    if others in yes:
        print(f"Thank you {name_list}")
        sleep(1)
        more_people = False
        flight_place = False
        firstc_loop = False
        available_loop = False
        name_loop = False
    if others in no:
        print("Thats all then *typing on keyboard noises*")
        sleep(1.5)
        print(f"Thank you {name_list}")
        sleep(1)
        more_people = True

#add places, names and costs for each person
sleep(2)
print("Have a good flight")
