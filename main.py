#document PLANPLANPLAN
name_list = []
place_list = []
price = (0)
auck_seats = (164)
ham_seats = (300)
wainui_seats = (127)
more_people = False
flight_place = False
firstc_loop = False
available_loop = False
name_loop = False
others_loop = False
yes = {"yes", "y", "yes please daddy"}
no = {"no", "n", "oh hell nuh"}
from time import sleep
while more_people == False:
    others_loop = False
    print("Hello, and welcome to Waikato Airport.")
    while name_loop == False:
      name = input("What is your name? Minimum of 3 Characters\n").title()
      if len(name) < 3:
        print("Please Enter 3 or more character name")
        name_loop = False
      elif len(name) >= 3:
        name_list.append(name)
        print("Nice to meet you {}".format(name))
        name_loop = True
    while flight_place == False:
        place = input(
            "Where will you be flying too? Auckland, Hamilton or Wainuiomata?\n"
        ).title()
        if place == "Auckland":
            place_list.append(place)
            print("The next available flight for Auckland is 2:30pm Monday")
            price = price + (125)
            auck_seats = auck_seats - (1)
            print("Your current total cost is ${}".format(price))
            sleep(2)
            price = price - (12.5)
            print("But there is a 10% discount for this ticket. That brings your total price to ${}".format(price))
            sleep(2)
            flight_place = True
        elif place == "Hamilton":
            place_list.append(place)
            print("The next available flight for Hamilton is 4pm Wednesday")
            price = price + (90)
            ham_seats = ham_seats - (1)
            print("The total cost is ${}".format(price))
            sleep(2)
            print("I can not seem to find a discount for this flight, sorry")
            sleep(2)
            flight_place = True
        elif place == "Wainuiomata":
            place_list.append(place)
            print("The next available flight for Wainuiomata is 9am Saturday")
            price = price + (420)
            wainui_seats = wainui_seats - (1)
            print("Total price is going to be ${}".format(price))
            sleep(2)
            price = price - (289.8)
            print("There is a discount for this flight for 69%. This brings it down to ${}".format(price))
            flight_place = True
        else:
            print("Your opinion is not an option!")
            sleep(1)
            flight_place = False
    while available_loop == False:
        available = input("Are you able to make the next flight?\n").lower()
        if available in no:
            available_loop = False
        elif available in yes:
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
        else:
          print("Please state a REAL place buddy boy")
          available_loop = False
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
    while others_loop == False:
      others = input("Will there be other people coming with you?\n").lower()
      if others in yes:
          print("Thank you {}".format(name_list))
          sleep(1)
          more_people = False
          flight_place = False
          firstc_loop = False
          available_loop = False
          name_loop = False
          others_loop = True
      elif others in no:
          print("Thats all then *typing on keyboard noises*")
          sleep(1.5)
          print("Thank you {}".format(name_list))
          sleep(1)
          more_people = True
          others_loop = True
      else:
        print("Can you please answer with a yes or a no")
        others_loop = False
print("That'll cost ${}".format(price))
sleep(1)
print("And here are your flights. {}".format(name_list + place_list))
sleep(2)
print("Have a good flight")