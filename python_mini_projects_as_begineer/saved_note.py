
# question 3: Write a function that takes a note as input and saves it to a file called "notes.txt". Each note should be saved on a new line. The function should also read the file and print all the notes with their corresponding line numbers.
def savednote(note):
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    with open("notes.txt", "r") as file:
        for i, line in enumerate(file, start=1):
            print(f"{i}: {line.strip()}")

note=input("enter your note:")
savednote(note)