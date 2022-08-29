class Rental:

    def __init__(self):
        self.income_list = []   
        self.expenses_list = []
        self.roi_list = []


    def income(self):
        while True:
            inc = input("\nLets calculate your monthly income! \n[1] Rent \n[2] Laundry \n[3] Storage  \n[4] Misc. \n[5] Quit) \n . . . ")
            if inc == '5':
                break
            elif inc == "1":
                r = input("How much? $")
                self.income_list.append(int(r))
            elif inc == "2":
                l = input("How much? $")
                self.income_list.append(int(l))
            elif inc == "3":
                s = input("How much? $")
                self.income_list.append(int(s))
            elif inc == "4":
                m = input("How much? $")
                self.income_list.append(int(m))
            else:
                print("Thats not the right input, try again")

    def expenses(self):
        while True:
            exp = input("\nLet's calculate the expenses for each month! \n[1] Tax \n[2] Insurance  \n[3] Utilities \n[4] HOA  \n[5] Repairs  \n[6] Manager  \n[7] Mortgage  \n[8] Etc. \n[9] Quit \n. . . ")
            if exp == '9':
                break  
            elif exp == "1":
                t = input("How much? $")
                self.expenses_list.append(int(t))
            elif exp == "2":
                i = input("How much? $")
                self.expenses_list.append(int(i))
            elif exp == "3":
                u = input("How much? $")
                self.expenses_list.append(int(u))
            elif exp == "4":
                h = input("How much? $")
                self.expenses_list.append(int(h))
            elif exp == "5":
                r = input("How much? $")
                self.expenses_list.append(int(r))
            elif exp == "6":
                m = input("How much? $")
                self.expenses_list.append(int(m))
            elif exp == "7":
                mo = input("How much? $")
                self.expenses_list.append(int(mo))
            elif exp == "8":
                o = input("How much? $")
                self.expenses_list.append(int(o))
            else:
                print("Thats not the right input, try again")


    def roi(self):
        while True:
            r = input("\nLet's calculate cash on cash ROI! \n[1] Down Payment \n[2] Closing Cost \n[3] Etc. \n[4] Quit \n . . . ")
            if r == '4':
                break
            elif r == "1":
                dp = input("How much? $")
                self.roi_list.append(int(dp))
            elif r == "2":
                cc = input("How much? $")
                self.roi_list.append(int(cc))
            elif r == "3":
                c = input("How much? $")
                self.roi_list.append(int(c))
            else:
                print("Thats not the right input, try again!")



James = Rental()


def run():
    while True:
        start = input("\nWelcome to Your ROI Rental Calculator! 🧮 \n\nWhat would you like to do? \n[1] Income  \n[2] Expenses \n[3] ROI \n[4] Calculate \n[5] Summary \n[6] Quit\n . . . ")
        if start == '6':
            break
        
        elif start == '1':
            James.income()

        elif start == '2':
            James.expenses()

        elif start == '3':
            James.roi()

        #Added a percent margins to show how well you are doing!
        elif start == '4':
            x = (((sum(James.income_list) - sum(James.expenses_list))*12) / sum(James.roi_list))*100
            if x <= 6:
                print("\n-------------------------------")
                print(f"Your ROI is {(((sum(James.income_list) - sum(James.expenses_list))*12) / sum(James.roi_list))*100} percent! 🫤 \nLet's try to get that percent up, maybe increase rent?")
                print("-------------------------------\n")            
            elif x <= 12:
                print("\n-------------------------------")
                print(f"Your ROI is {(((sum(James.income_list) - sum(James.expenses_list))*12) / sum(James.roi_list))*100} percent! 🥳🥳🥳 \nThat's pretty good! Keep it up!")
                print("-------------------------------\n")
            else:
                print("\n-------------------------------")
                print(f"Your ROI is {(((sum(James.income_list) - sum(James.expenses_list))*12) / sum(James.roi_list))*100} percent! 🥳🥳🥳 \nWoohoo making bank! Let's invest more!  🤑")
                print("-------------------------------\n")
        

        #Created a summary to see how you can adjust the numbers!
        elif start == '5':
            print("\n-------------------------------")
            print("Your summary is as follows...")
            print(f"Total Income: ${sum(James.income_list)}")
            print(f"Total Expenses: ${sum(James.expenses_list)}")
            print(f"Total Cash on Cash ROI: ${sum(James.roi_list)}")
            print("-------------------------------\n")

        else:
            print("Thats not the right input, try again!")

run()