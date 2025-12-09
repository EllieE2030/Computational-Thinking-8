print("Hello! My name is Story! I am about to tell you a story and you get to make it your own!!! ")
name = input("What is your name?")
answer = input(f"Hello {name}! Are you ready to continue? Type 'YES' if you are and 'NO' if you are not. ")
if answer == 'NO':
    print(f"Thats too bad, have a good day {name}!")
elif answer == 'YES':
    print(f"I am so glad you are going to join me, {name}!")
    town = input("Our story starts in a town called...")
    print(f"In {town}, everyone lived in harmony until...")
    drama = input("Did a dinosaur come or was a princess born? Type 'A' for a dinosaur or type 'B' for a princess.")
    if drama == 'A':
        print(f"A dinosaur came and attacked {town}. He was looking for something special.")
        dino = input("The dinosaur was named...")
        print(f"{dino} the dinosaur wasn't a mean dinosaur, in fact he loved dogs and his favorite movie was Freaky Friday.")
        plot = input(f"Does {dino} come to {town} to find a family or to have some food? Type 'A' for family and 'B' for food.")
        if plot == 'A':
            found = input(f"{dino} looked everywhere for his family. He looked at the beach, in space, and even...")
            print(f"{dino} looked in {found} for a long time but found nothing")
            print(f"{dino} decided to go to see someone important and in {town}, the most important person was the wizard! ")
            input(f"{dino} went to see the wizard and realized that the wizard was")
            print("His DAD!!!")
            dad = input(f"{dino}'s dad was named...")
            print(f"{dino} was so happy to meet his dad, {dad}! {dino} and his dad lived happily ever after in the wizard palace!")
            final = input("Did you enjoy the story? Type 'YES' or 'NO'!")
            if final == 'YES':
                print("Thank you for enjoying the story! Play again and try a new route!")
            elif final == 'NO':
                print("Thats too bad, but you can always try again for a new story line!")
        elif plot == 'B':
            food = input(f"{dino} was super hungry and really wanted some...")
            want = input(f"{food} was {dino}'s favorite and it made {dino} so happy that {dino} wanted to...")
            print(f"Once {dino} did {want}, {dino} decided to go to sleep because {dino} ate too much {food}.")
            dream = input(f"When {dino} was dreaming, {dino} met a celebrity, the celebrity was...")
            print(f"{dino} and {dream} became best friends in {dino}'s dream!")
            print(f"When {dino} woke up, {dream} was there too! They went to disneyland in {town} together and ate soo much {food} every single day for the rest of their lives!")
            done = input("Did you enjoy the story? Type 'YES' or 'NO'!")
            if done == 'YES':
                print("Thank you for enjoying the story! Play again and try a new route!")
            elif done == 'NO':
                print("Thats too bad, but you can always try again for a new story line!")
    elif drama == 'B':
        princess = input(f"There was a princess born in {town} to the king and queen! They were overjoyed to have a daughter and named her...")
        power = input(f"{princess} was a beautiful baby and as she grew older she developed special powers that control...")
        print(f"{princess}'s {power} power's made her even more special!")
        evil = input(f"People wanted {princess}'s power so much. Who wanted her {power} powers? Type 'A' for a witch or type 'B' for a evil prince.")
        if evil == 'A':
            witch = input(f"There was an evil witch across {town} who yearned for {princess} powers. Her name was...")
            transport = input(f"One day, {witch} flew to the castle using her...")
            print(f"The witch used her {transport} every time she needed to get somewhere. She especially needed it for her new plan!")
            plan = input(f"What was her plan? Did she plan to hurt the princess or turn into a frog and suck the powers out of her? Type 'A' to hurt her or type 'B' to turn into a frog.")
            if plan == 'A':
                print("The witch stormed the castle that day and got into a sword fight with the princess.")
                print(f"{princess} used her {power} powers and beat the witch!")
                print("The princess was then recognized for her heroic actions and became queen later that year!")
                finish = input("Did you enjoy the story? Type 'YES' or 'NO'!")
                if finish == 'YES':
                    print("Thank you for enjoying the story! Play again and try a new route!")
                elif finish == 'NO':
                    print("Thats too bad, but you can always try again for a new story line!")
            elif plan == 'B':
                print("The witch used a magic potion to transform herself into a frog.")
                print(f"Little did {witch} know, but the princess was afraid of frogs.")
                print(f"{princess} used her {power} power's to banish the witch for good!")
                print(f"The princess was then recognized for her heroic actions and became queen later that year!")
                done = input("Did you enjoy the story? Type 'YES' or 'NO'!")
                if done == 'YES':
                    print("Thank you for enjoying the story! Play again and try a new route!")
                elif done == 'NO':
                    print("Thats too bad, but you can always try again for a new story line!")
        elif evil == 'B':
            prince = input(f"There was an evil prince in the land who schemed to become king of the land of {town}. His name was...")
            weak = input(f"{prince} was handsome and smart but had only one weakness which was...")
            print(f"{prince} was about to go into the palace and use his charm to win over the princess until he realized that his plan could fail if his weakness was exposed.")
            weapon = input(f"The princess ran out of the palace because she heard something. Just in case, she brought...")
            print(f"{princess} saw the prince and immediately went into a battle with him using her {weapon}! To no surprise, the princess won and banished the prince from {town}!")
            print("The princess was then recognized for her heroic actions and became queen later that year!")
            complete = input("Did you enjoy the story? Type 'YES' or 'NO'!")
            if complete == 'YES':
                    print("Thank you for enjoying the story! Play again and try a new route!")
            elif complete == 'NO':
                    print("Thats too bad, but you can always try again for a new story line!")



         
                

        


