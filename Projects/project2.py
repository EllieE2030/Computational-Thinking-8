type_a = 0
type_b = 0
type_c = 0
type_d = 0

input("Hello and welcome to the personality quiz! Lets figure out which personality type you are!")
print("")
type = input("Which type do you think you are right now? A, B, C, or D?   ")
print("")
print(f"We'll see if you really are type {type}...")
print("")
print("How do you react when your given a deadline?")
print("")
print("Do you A, break up the task so you make sure you get more work completed?")
print("")
print("Do you B, lowkey forget about it until the last second?")
print("")
print("Do you C, spend a lot of time worrying about it?")
print("")
answer1 = input("Or do you D, start working right away so you can get it done asap?   ")
if answer1 == 'A':
    type_c += 2
elif answer1 == 'B':
    type_b += 2
elif answer1 == 'C':
    type_d += 2
elif answer1 == 'D':
    type_a += 2
print("")
print("")
print("What's your go-to texting style?")
print("")
print("Do you A, tend to go on long tangents and write super-long messages?")
print("")
print("Do you B, quickly respond and super directly?")
print("")
print("Do you C, love using fun reactions and emojis?")
print("")
answer2 = input("Or do you D, tend to get anxious about how your messages come off, so you plan out your responses carefully?   ")
if answer2 == 'A':
    type_a += 2
elif answer2 == 'B':
    type_d += 2
elif answer2 == 'C':
    type_b += 2
elif answer2 == 'D':
    type_c += 2
print("")
print("")
print("Which job is most appealing for you?")
print("")
print("Do you A, choose a therapist?")
print("")
print("Do you B, choose an engineer?")
print("")
print("Do you C, choose a political leader?")
print("")
answer3 = input("Or do you D, choose a CEO?   ")
if answer3 == 'A':
    type_b += 2
elif answer3 == 'B':
    type_c += 2
elif answer3 == 'C':
    type_d += 1
elif answer3 == 'D' or answer3 == 'C':
    type_a += 2
print("")
print("")
print("What motivates you most in school or hobbies?")
print("")
print("A, impressing others, having fun, and making connections?")
print("")
print("B, achieving success through high grades and winning?")
print("")
print("C, maintaining peace and helping others?")
print("")
answer4 = input("Or D, solving complex problems perfectly?   ")
if answer4 == 'A':
    type_b += 2
elif answer4 == 'B':
    type_a += 2
elif answer4 == 'C':
    type_d += 2
elif answer4 == 'D':
    type_c += 2
print("")
print("")
print("At lunch with your friends, you are usually..?")
print("")
print("A, Deciding where to sit and what to do next?")
print("")
print("B, Telling the funniest stories and making people laugh?")
print("")
print("C, Listening quietly and observing everything around you?")
print("")
answer5 = input("Or D, Making sure everyone has someone to sit with and feels happy?   ")
if answer5 == 'A':
    type_a += 2
elif answer5 == 'B':
    type_b += 2
elif answer5 == 'C':
    type_c += 2
elif answer5 == 'D':
    type_d += 2
print("")
print("")
print("Which word do your friends use most to describe you?")
print("")
print("A, A leader or bossy (in a good way!)?")
print("")
print("B, A comedian or social butterfly?")
print("")
print("C, Smart or Organized?")
print("")
answer6 = input("Or D, Kind or supportive?   ")
if answer6 == 'A':
    type_a += 2
elif answer6 == 'B':
    type_b += 2
elif answer6 == 'C':
    type_c += 2
elif answer6 == 'D':
    type_d += 2
print("")
print("")
print("How do you feel about sports or games??")
print("")
print("A, winning is everything! You must play hard to be number one?")
print("")
print("B, you like playing, but you mainly just want to have fun with friends?")
print("")
print("C, you like games with clear rules and strategy?")
print("")
answer7 = input("Or D, you don't really like competitive games because they make you feel stressed?   ")
if answer7 == 'A':
    type_a += 2
elif answer7 == 'B':
    type_b += 2
elif answer7 == 'C':
    type_c += 2
elif answer7 == 'D':
    type_d += 2
print("")

#end of quiz:
if type_a > type_b and type_a > type_c and type_a > type_d:
    print("Congrats! You are type A! You are characterized by your ambition, impatience, and competitiveness! You are a motivated high achiever who thrives under pressure!")
    print("")
    if type == 'A':
        print("Good job! You guessed perfectly!")
    else:
        print("You guessed wrong but that's all good! I hope you like type A more!")
elif type_b > type_a and type_b > type_c and type_b > type_d:
    print("Congrats! You are type B! You are the opposite of type A. You are relaxed easygoing and patient. You enjoy a balanced lifestyle and handle stress well.")
    print("")
    if type == 'B':
        print("Good job! You guessed perfectly!")
    else:
        print("You guessed wrong but that's all good! I hope you like type B more!")
elif type_c > type_a and type_c > type_b and type_c > type_d:
    print("Congrats! You are type C! You are analytical, detail-oriented, and conscientious. You are a perfectionist who may have difficulty expressing your emotions.")
    print("")
    if type == 'C':
        print("Good job! You guessed perfectly!")
    else:
        print("You guessed wrong but that's all good! I hope you like type C more!")
elif type_d > type_a and type_d > type_b and type_d > type_c:
    print("Congrats! You are type D! You are prone to experiencing high levels of negative emotions, such as worry, sadness, and irritability, combined with social inhibition.")
    print("")
    if type == 'D':
        print("Good job! You guessed perfectly!")
    else:
        print("You guessed wrong but that's all good! I hope you like type D more!")
else:
    print(f"I can't decide which personality type you are! You had {type_a} type A points, {type_b} type B points, {type_c} type C points, and {type_d} type D points. I hope this makes sense for you!")
    