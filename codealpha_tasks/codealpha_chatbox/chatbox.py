def chatbox():
    print("SIMPLE CHATBOX")
    print("You can say 'Hi ,Hello ,Hola ,How are you ,What is your name ,Bye ")
    print("TYPE 'Bye'to exit\n")
    while True:
        user_input=input("You: ").lower().strip()
        if user_input=="hello"or user_input=="hi" or user_input=="hola":
            print("BOT: Hi there!")
        elif user_input=="how are you":
            print("BOT: I'm fine ,thanks:)!")
        elif user_input=="what is your name":
            print("BOT: I'm a simple python chatbox:)")
        elif user_input=="bye":
            print("BOT: Goodbye!")
            break
        else:
            print("BOT: Sorry I don't understand that.")

chatbox()    