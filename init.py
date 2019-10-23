from linkBot import LinkBot
from selenium import webdriver

# You must indicate the full path where the driver is! And be careful, there are one driver for a browser.
driver = webdriver.Chrome(
    executable_path="C:\\Users\\Monkey (D) Luffy\\Documents\\Software Développement\\webDriver\\chromedriver.exe")
bot = LinkBot(driver)


while True:
    print("LinkedinBot By Léo Delpon !")
    print("[+] Press a number between 1 and 4 //")
    print("[+] Before using this script, the followed package has to be installed : Selenium")
    print("[1] add Contact")
    print("[2] add Specified Contact")
    print("[3] Liking the Linkedin feed")
    print("[4] Finding a job")
    choice = int(input("Make a choice: "))

    if choice == 1:
        print("// To make it work, you must have a complete profile //")
        bot.addContact()
    elif choice == 2:
        print("// To make it work, you must have a complete profile //")
        bot.specifiedContact()
    elif choice == 3:
        print("// To make it work, you must have a complete profile //")
        bot.feedLiking()
    elif choice == 4:
        print("// To make it work, you must have a complete profile //")
        print("// You have to put your document inside the PYLINKEDIN folder //")
        bot.jobLooking()
    else:
        choice = int(input("Make a choice between 1 and 4 dude: "))
