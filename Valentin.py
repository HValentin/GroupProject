def checkInput(size):
    choiceArray = ["A", "B", "C", "D", "E"]
    while True:
        inp = input("What choice?")
        inp = inp.upper()
        for x in range(size):
            if inp == choiceArray[x]:
                return inp

        print("Not a valid input")


print("He opened the latch covering the USB slots on his computer, which he built himself, plugging the camera into one end and placing it on the desk.\n\
         He took the other end and pushed the USB into its socket.\n\
        A - Put in quick!\n\
        B - Put in slowly")

choice = checkInput(2)
if choice == "A":
    print("“AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH” Mac screamed in agony.")
    input()
    print("A shock of electricity ran through his body as thunder pounded in the background.\n\
        His hands were shaking as he absorbed the power from his machine. \n\
        'It was so much that power he felt invincible, immortal and unshakable.'\n\
        He looked around the room trying to gain a sense of reality.\n\
        His eyes were blurring, focus disappearing but he noticed something.\n\
        The inkjet printer was gone.\n\
        Moments passed as his vision returned but still unbalanced, still absorbing something within his body, but what?\n\
         A - What was it?")
    choice = checkInput(1)
elif choice == "B":
        print ("A shock of electricity ran through his body as thunder pounded in the background.\n\
        His hands were shaking as he absorbed the power from his machine. \n\
        'It was so much that power he felt invincible, immortal and unshakable.'\n\
        He looked around the room trying to gain a sense of reality.\n\
        His eyes were blurring, focus disappearing but he noticed something.\n\
        The inkjet printer was gone.\n\
        Moments passed as his vision returned but still unbalanced, still absorbing something within his body, but what?\n\
         A - What was it?")
        choice = checkInput(1)

else:
    pass
if choice == "A":
    print('As Mac fell back from the sheer force of the current, he discovered his veins becoming tri-coloured upon waking up from a sleepy hase.\n\
          There was no pulse yet he could feel his body pulsating with a new type of blood flow.\n\
           A - Look at red vein. \n\
           B - Look at blue vein. \n\
           C - Look at yellow vein.')
choice = checkInput(3)

if choice == "A":
   print ("it's blood")
   choice = checkInput(3)

elif choice == "B":
    print ("blue, so blue it could only be compared to that blue powerade drink, this was the data buses. \n\
           The data was being carried through his new veins to his brain and around his body as the control unit took over his senses")
    choice = checkInput(3)

elif choice == "C":
    print ("Yellow like monster energy; an address bus carrying the addresses for functions. \n\
           He tried to pick up his hand and his wrist illuminated with a series of binary digits")
    choice = checkInput(3)

if choice == "A" or "B" or "C":
    print("The data was being carried through his new veins to his brain and around his body as the control unit took over his senses, Mac was confused and found himself overheating at the prospect. \n\
               He prayed for a windows operating system because he heard it was the most compatible with other devices and although he knew something wasn’t quite right, he was desperate to see the pictures of his phishing trip and the only way to do that was through the printer to his left. \n\
               “Wait that wasn’t there before” he muttered as he saw the printer transform before his eyes, the ink cartridges exploded into a multitude of colors and as they cleared he noticed something unusual, the printer had grown legs. \n\
               A - What is that?")
