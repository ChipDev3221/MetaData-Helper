import time

def melink():
  print("https://github.com/Maralexbar/MetaDataStringEditor-EM")
  selection()

def methods():
  print("==========")
  print("select a method:")
  print("1. Custom OS")
  print("2. No Hand Taps")
  print("3. Cosmetic in wardrobe")
  print("4. anti die in ghost reactor")
  print("5. custom creator code")
  print("6. all creator codes valid")
  print("7. colored text")
  print("8. Exit")
  print("==========")
  mchoice = input("Enter your choice: ")
  if mchoice == "1":
      print("For a custom OS, search for Gorilla OS in the metadata editor and change it to whatever you would like. and press enter to format it correctly")
      methods()
  elif mchoice == "2":
      print("For no hand taps, search for OnHandTapRPC in the metadata editor and delete the string.")
      methods()
  elif mchoice == "3":
      print("For cosmetic in wardrobe, search for NOTHING and change it to any item ID.")
      methods()
  elif mchoice == "4":
      print("For anti die in ghost reactor, search for EnemyHitPlayerRPC and delete the string.")
      methods()
  elif mchoice == "5":
      print("to add a custom creator code, search for CREATOR CODE and change the 3 values to the words you want.")
      methods()
  elif mchoice == "6":
      print("to make all creator codes valid, search for CREATOR CODE INVALID and delete the IN.")
      methods()
  elif mchoice == "7":
      print("for custom colored text, search for a text value and add <color=[red, blue, green, yellow]> and </color> around the text.")
      methods()
  elif mchoice == "8":
      selection()

def github():
    print("==========")
    print("My github page:")
    print("https://github.com/ChipDev3221/")
    print("==========")
    selection()

def discord():
    print("==========")
    print("https://discord.gg/bbZNqnZkZt")
    selection()
    print("==========")

def exit():
    print("goodbye!")
    time.sleep(3)

def selection():
  print("==========")
  print("welcome to metadata helper!")
  print("select an option:")
  print("1. Link to metadata editor")
  print("2. Methods")
  print("3. My github page")
  print("4. metahacks discord")
  print("5. Exit")
  print("==========")
  choice = input("Enter your choice: ")
  if choice == "1":
    melink()
  elif choice == "2":
    methods()
  elif choice == "3":
    github()
  elif choice == "4":
    discord()
  elif choice == "5":
    exit()

selection()