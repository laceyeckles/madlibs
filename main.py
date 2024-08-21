# Mad Libs Generator - A Princess in Paris Story
# Story created by Lacey Eckles

# Loop back to this point once code finishes
loop = 1

while (loop < 10):

    # All the questions that the program asks the user
    princess_name = input("Choose a name for the princess: ")
    adjective = input("Choose an adjective: ")
    noun = input("Choose a noun: ")
    p_noun = input("Choose a plural noun: ")
    verb = input("Choose a verb: ")
    verb2 = input("Choose another verb: ")
    place = input("Name a place in Paris: ")
    noun2 = input("Choose another noun: ")

    # Displays the story based on the user's input
    print("------------------------------------------")
    print(f"Once upon a time, Princess {princess_name} lived in a {adjective} castle.")
    print(f"She loved to {verb} and {verb2} with her {noun} and her {p_noun}.")
    print(f"One day, she decided to visit {place} in Paris.")
    print(f"While there, she found a magical {noun2} that changed her life forever.")
    print("And they all lived happily ever after.")
    print("------------------------------------------")

    # Loop back to "loop = 1"
    loop = loop + 1
