import sys,time,random
typing_speed = 50 #wpm
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

print("Ralof: \n")
print_slow(""" Hey, you. You're finally awake. You were trying to cross the border,
right? Walked right into that Imperial ambush, same as us, and that
thief over there.\n
""")
print("Lokir:\n")
print_slow("""Damn you Stormcloaks. Skyrim was fine until you came along. Empire was
nice and lazy. If they hadn't been looking for you, I could've stolen
that horse and been half way to Hammerfell. You there. You and me -- we
should be here. It's these Stormcloaks the Empire wants.\n\n""")

print("Ralof:\n")
print_slow(" We're all brothers and sisters in binds now, thief.\n")

print("Imperial Soldier:\n")
print_slow("Shut up back there! \n \n")

print_slow("[Lokir looks at the gagged man.]\n \n")

print("Lokir:\n")
print_slow("And what's wrong with him?\n")

print("Ralof: \n") 
print_slow("""Watch your tongue! You're speaking to Ulfric Stormcloak, the true High
King. \n""")

print("lokir: \n") 
print_slow("""Ulfric? The Jarl of Windhelm? You're the leader of the rebellion. But if
they captured you... Oh gods, where are they taking us? \n""")

print("ralof: \n")
print_slow("I don't know where we're going, but Sovngarde awaits. \n")

print("Lokir: \n")
print_slow("No, this can't be happening. This isn't happening. \n")

print("ralof: \n") 
print_slow("Hey, what village are you from, horse thief? \n")

print("Lokir: \n") 
print_slow("Why do you care? \n")

print("Ralof: \n")
print_slow("A Nord's last thoughts should be of home. \n")

print("Lokir: \n") 
print_slow("Rorikstead. I'm...I'm from Rorikstead. \n")

print("[They approach the village of Helgen. A soldier calls out to the lead wagon.] \n")

print("Imperial Soldier: \n")
print_slow("General Tullius, sir! The headsman is waiting! \n")

print("General Tullius: \n") 
print_slow("Good. Let's get this over with. \n")

print("lokir:\n")
print_slow(" Shor, Mara, Dibella, Kynareth, Akatosh. Divines, please help me. \n")

print("Ralof: \n")
print_slow("""Look at him, General Tullius the Military Governor. And it looks like
the Thalmor are with him. Damn elves. I bet they had something to do
with this.

This is Helgen. I used to be sweet on a girl from here. Wonder if Vilod
is still making that mead with juniper berries mixed in. Funny...when I
was a boy, Imperial walls and towers used to make me feel so safe. \n \n \n""")

print("[A man and son watch the prisoners pull into town.] \n")

print("Haming: \n")
print_slow(" Who are they, daddy? Where are they going? \n")

print("torolf: \n")
print_slow("You need to go inside, little cub. \n")

print("Haming: \n")
print_slow("Why? I want to watch the soldiers. \n")

print("Torolf: \n")
print_slow("Inside the house. Now. \n")


print("alright out of the cart")
print("what is your name")
name = input()