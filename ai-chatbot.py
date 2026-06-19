def chatbot():
    print("Hello. I am Python based AI chatbot")
    while True:
        user=input('You:').lower()
        if user == "hello":
            print("Hello . Nice to meet you")
        elif user == "how are you":
            print("I am good . Thanks for asking")
        elif user == "who are you":
            print("I am Python AI chatbot")
        elif user == "bye":
            print("Goodbye,Thanks for conversation")
        else:
            break
    print("Sorry,I don't understand")
chatbot() 