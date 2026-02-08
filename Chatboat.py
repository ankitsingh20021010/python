print("Chatbot: Hello! type 'bye' to exit" )
while True:
    user =input("you: " ).lower()

    if user=="hello":
        print("Chatboat: Hi!")
    elif user=="how are you":
        print("Chatboat: I am Fine")
    elif user =="bye":
        print("Chatboat: Bye")
    else:
        print("Chatbot: I don't understand")
