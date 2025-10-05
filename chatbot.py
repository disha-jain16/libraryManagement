def chatbot():  
    print("Hello! I'm ChatBot. Type 'quit' to exit.")  
  
    while True:  
        user_input = input("You: ").lower()  
  
        if user_input == "quit":  
            print("ChatBot: Goodbye! Have a nice day.")  
            break  
          
        elif "hello" in user_input or "hi" in user_input:  
            print("ChatBot: Hi there! How can I help you?")  
          
        elif "how are you" in user_input:  
            print("ChatBot: I'm just a bot, but I'm doing great! How about you?")  
          
        elif "your name" in user_input:  
            print("ChatBot: My name is PyBot, your Python assistant.")  
          
        elif "time" in user_input:  
            import datetime  
            now = datetime.datetime.now()  
            print("ChatBot: The current time is", now.strftime("%H:%M:%S"))  
          
        elif "date" in user_input:  
            import datetime  
            today = datetime.date.today()  
            print("ChatBot: Today's date is", today.strftime("%B %d, %Y"))  
          
        else:  
            print("ChatBot: Sorry, I don't understand. Can you rephrase?")  
              
  
# Run the chatbot  
chatbot()  
