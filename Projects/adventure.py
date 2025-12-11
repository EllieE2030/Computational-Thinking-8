print("Hello!")
answer1 = input("Do you want to use the SAAS sports finder?")
if answer1 == 'no':
    print("Have a nice day!")
elif answer1 == 'yes':
    gender = input("Mixed or single gender?")
    if gender == 'mixed':
        answer2 = input("Team or solo?")
        if answer2 == 'team':
            print("The sport for you is club ultimate!")
        elif answer2 == 'solo':
            print("You should try cross country, wrestling, or track and field!")
    elif gender == 'single':
        season = input("Winter or spring?")
        if season == 'winter':
            print("You should try basketball or flag football!")
        elif season == 'spring':
            print("You should try tennis, lacrosse, golf, boys soccer, or girls ultimate!")
    