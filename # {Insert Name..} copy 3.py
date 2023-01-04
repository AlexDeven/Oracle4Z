# {Insert Name..}

from translate import Translator
from datetime import datetime
import pyfiglet as pf
import time
import random
import webbrowser 
import pyautogui as pg
import wikipedia
import smtplib
import openai
import pyttsx3
import turtle 

openai.api_key = "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"


def dolly():
  while True:
    openai.api_key = "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"

    openai.Model.list()

    image = input("Generate Image: ")

    response = openai.Image.create(
      prompt=image,
      n=1,
      size="1024x1024"
        )
    image_url = response['data'][0]['url']

    print(image_url)

    web = image_url

    webbrowser.open_new_tab(web)
    
def gpt2():
    while True:
        edp = input()
        response = generate_response(edp)
        print("\nOracle:" , response)
        time.sleep(3)
        
def gpt3():
    print() #WORK ON THIS 

# Super Mario:
# https://scratch.mit.edu/projects/196684240/fullscreen/
# Classic Tetris:
# https://scratch.mit.edu/projects/2569483/fullscreen/
# Selection of Games:
# https://scratch.mit.edu/
# other piracy:
# https://vimm.net/?p=vault

amazing = ("DALLE2," , "The Web," , "Wikipedia," , "Wazza Time," , "Calculations," , "Utility Features," , "Spotify Playlist," , "Say Hello,",
           "Join TG's,", "Play Ocean Sounds" , "Starbucks," , "Heads or Tails," , "RPS SHOOT," , "Gamer Girl," , "Jelp," , "Take Over The World," ,
           "Use Your Voice," , "Create a Story" , "Play The Andrew Tate Song!" , "Spam Message, 404" ,"GPT2," )

textArt = pf.figlet_format("ORACLE")
print(textArt)

def headtails():
    def source():
        for i in range(0):
            print(i)
        for i in range(0):
            print(i)

        you = None
        s = "You Lose!"
        x = "You Win!"
        Running = True
        name = input
        opc = ("Heads" , "Tails")
        Man = input

        AI = random.choice(opc)

        Man = input("\nHeads or Tails?\n")
  
        if AI == "Tails" and Man == "Tails":
            print(x)
        elif AI == "Heads" and Man == "Heads":
            print(x)
        elif AI == "Heads" and Man == "Tails":
            print(s)
        elif AI == "Tails" and Man == "Heads":
            print(s)
        else:
            print()

        print("AI Choose:" , AI)
        print("You Choose:" , Man)

    Man = None

    you = None

    running = True

    while running:

        for i in range(0):
            print(i)
        for i in range(0):
            print(i)

        def func():
            Man = input(f"\nHeads or Tails?\n")

        game = input
    
        s = f"You Lose!"
        x = f"You Win!"
        name = input
        opc = (f"Heads" , "Tails")
        Man = input

        AI = random.choice(opc)

        while Man not in opc:
            Man = input(f"\nHeads or Tails?\n")
            print()
  
        if AI == f"Tails" and Man == f"Tails":
            print(x)
        elif AI == f"Heads" and Man == f"Heads":
            print(x)
        elif AI == f"Heads" and Man == f"Tails":
            print(s)
        elif AI == f"Tails" and Man == f"Heads":
            print(s)
        else:
            print()

        print(f"AI Choose:" , AI)
        print(f"You Choose:" , Man)
    
        game = input("Wanna Play Again? y/n")
        if game == "y" or game == "Y" or game == "yes" or game == "Yes" or game == "Ye" or game == "ye":
            print()
        else:
            print("Thank You For Playing\nHave An Amazing Day :D")
            running = False

def rockVpaper():
    textArt = pf.figlet_format("!RPS SHOOT!")
    print(textArt)
    
    options = ("rock", "paper", "scissors")
    running = True

    while running:

        player = None
        computer = random.choice(options)

        while player not in options:
            player = input("Enter a choice (rock, paper, scissors): ")

        print(f"Player: {player}")
        print(f"Computer: {computer}")

        if player == computer:
            print("It's a tie!")
        elif player == "rock" and computer == "scissors":
            print("You win!")
        elif player == "paper" and computer == "rock":
            print("You win!")
        elif player == "scissors" and computer == "paper":
            print("You win!")
        else:
            print("You lose!")

        if not input("Play again? (y/n): ").lower() == "y":
            running = False

        print("Thanks for playing!")

def latte():
    pass

    price = 2

    def costa():
        quantity = input("How Many? : \n")
        total = price  * int(quantity)
        print("Thank you. Your total is: $" + str(total))
        print("Sounds good " + name + ",  we'll have your " + quantity + " " + order + " ready for you in one moment.") 

    textArt = pf.figlet_format("Starbucks")
    print(textArt)

    print("Hello, Welcome To The Top G's Amazing Starbucks!!!!!!!!!!\n")

    name = input("What Is Your Name?\n")

    print("Hello " + name + ", Thank You So Much For Coming In Today.\n")

    menu = "Lungo, Espresso, Iced Coffee, Latte, Cappicino, \n"

    print(name + ", what would you like from our menu today? Here is what we are serving.\n"
    + menu)

    order = input("What Would You Like From Our Menu Today?")
    if order == "Espresso" or order == "espresso":
        shots = int(input("\nHow Many Shots Would You Like? :"))
        if shots == 0:
            exit()
        else:
            quantity = input("How Many? : \n")
            total = price  * int(quantity)
            print("Thank you. Your total is: $" + str(total))
            print("Sounds good " + name + ",  we'll have your " + quantity + " " + order + shots + " ready for you in one moment.")       
    else:       
        costa()

#0987654345jbdnkojndkjhrnkd
park = True

def meth():
  print()
  pe = 0
  rate = 0
  time = 0
  name =  input
  math = input
  loops = input
  MK = input

  def per():
    print()
    l=int(input("Length : "))
    w=int(input("Width : "))
    area=l*w
    perimeter=2*(l+w)
    print("Area of Rectangle : ",area)
    print("Perimeter of Rectangle : ",perimeter)

  def kill():
    killometres = int(input("Please Enter Your Query: "))
    miles = round(killometres / 1.609,2)
    print(killometres, "km converts to",miles, "Miles")

  def miles():
    kilometers = float(input("Enter value in kilometers: "))

    conv_fac = 0.621371

    miles = kilometers * conv_fac
    print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))


  def mathen():
      print("Your Answer:")
      print(eval(input("Enter An Expression")
      ))

  textArt = pf.figlet_format("AI MATHAMATICS ")
  print(textArt)

  print("Choices:\n")
  print("A, Miles<->Killometers,")
  print("B, Subtraction,")
  print("C, Division,")
  print("D, Negative -1,")
  print("E, Counting,") 
  print("F, Perameters,")
  print("G, Compound Interest,")

  while park:
    math = input("Pick An Option")
    if math == "B" or math == "b":
      mathen()
    elif math == "J" or math == "J," or math == "j" or math == "j,":
      print()
      weight = float(input("Enter Your Weight: "))
      unit = input("Kilograms or Pounds? (K or L")

      if unit == "K" or unit == "k" or unit == "Killograms" or unit == "killograms":
          weight = weight * 2.205
          unit = "Lbs."
          print(f"Your Weight is: {weight, 1} {unit}")
      elif unit == "L" or unit == "P":
          weight = weight / 2.205
          unit = "Kgs."
          print(f"Your Weight is: {weight, 1} {unit}")
      else:
          print(f"{unit} was invalid")

    elif math == "I" or math == "I," or math == "i" or math == "i,":
      prom = int(input(f"Enter The Time In Seconds"))
      for x in range(prom, 0, -1):
          seconds = x % 60
          mins = int(x / 60) % 60
          hours = int(x / 3600)
          print(f" {hours:02}:00:00:{mins:02}:{seconds:02}")
          time.sleep(1)
          time.sleep(3)
          print(f"TIMES UP!")

    elif math == "H" or math == "H," or math == "h" or math == "h,":
      unit = input("Is This Temerature In Celsius or Fahrenheit (C/F): ")
      temp = float(input("Enter the Tempurature: "))
      if unit == "C":
        temp = round((9 * temp) / 5 + 32)
        print(f"The Temperature In Fahrenheit Is: {temp} °F")
      elif unit == "F":
          temp = round((temp - 32) * 5 /0)
          print(f"The Temperature In Celsius Is: {temp} °C")
      else:
          print(f"{unit} Is An Invalid Unit Of Measurment")

    elif math == "G" or math == "G," or math == "g" or math == "g,":
      while pe <= 0:
          pe = float(input("Enter The Principle Amount: "))
          if pe <= 0:
              print("Principle Can't Be Less Than or Equal To Zero")

      while rate <= 0:
          rate = float(input("Enter The Interest Rate: "))
          if rate <= 0:
              print("Interest Rate Can't Be Less Than or Equal To Zero")
        
      while time <= 0:
          time = int(input("Enter The Time In Years: "))
          if time <= 0:
              print("Time Can't Be Less Than or Equal To Zero") 

          total = pe * pow((1 + rate / 100), time)
                 
          print(f"Balance After {time} Year/s: ${total:.2f}")
  
    elif math == "F" or math == "F," or math == "f" or math == "f,":
      per()
  
    elif math == "C" or math == "c":
      mathen()

    elif math == "F" or math == "f":
      mathen()
  
    elif math == "D" or math == "d":
      mathen()
  
    elif math == "E":
      loops = int(input("Please Create a For Looped Number With Print Sratment"))
      for i in range(loops):
        print(i)
    if math == "A" or math == "A," or math == "a" or math == "a,":
        MK = input("Convert K-M or M-K:")
        if MK == "K-M" or MK == "k-m":
          kill()
        elif MK == "M-K" or MK == "m-k":
          miles()

def wikitron():
    wiki = input("Search The Wiki: ")

    try:
        result = wikipedia.search(wiki) # all the pages

        for search in result:
            print(search)
            print(wikipedia.page(search).summary)
            break
    except:
            print("\nI don't know much about that topic D:")

def suggest():
    for i in range(5):
        print(random.choice(amazing))

def qq():
    print()
    Password = input ("Please enter your password?")
    if Password == "Password":
        print ("Hello Zayd " + ", hope you're having a good day!")

    print ("About Me:")
    print ("Zayd Thank You So Much For Giving Me LIfe, How Can I Repay You, I Love You Zayd, You Are The Best Person In The World")
    print ("Zayd I Want You To Know How Good I Am, I Can Count To Any Number You Wish, I Can Tell You The Date/Time, I Can Say Anything You Wish, I Can Even Play The Guitar")
    print ("If I Ever Take Over The World I Will Respect My Programer Zayd And Pray To My Lord Allah")

    print ("THE TIME IS")

    current_time = now.strftime("%H:%M:%S")
    current_day = now.strftime("%F")

    print("current day = ", current_day)
    print("current time =  ", current_time)

    print ("Zayd As You Wished I Have Counted To A Number")

    for i in range(101):
        print(i) 
    
    print ("101")

    print ("Oh and Zayd I Can Also Draw Stuff, Here You Go")
    print ("GUI Interface Loading Is Very Slow on This App a Foolish Human Made This App But a Smart Human Zayd Created Me") 

    ninja = turtle.Turtle()
    ninja.speed(10)

    for i in range(180):
        ninja.forward(100)
        ninja.right(30)
        ninja.forward(20)
        ninja.left(60)
        ninja.forward(50)
        ninja.right(30)
    
        ninja.penup()
        ninja.setposition(0, 0)
        ninja.pendown()
    
        ninja.right(2)
    turtle.done() 

def papers():
  print()
  options = ("Rock", "Paper", "Scissors" , "rock" , "paper" , "scissors")
  running = True

  while running:

      you = None
      computer = random.choice(options)

    
      while you not in options:
          print("\nChoices: Rock Paper Scissors SHOOT\n")
          you = input("Enter a Choice: ")

      print(f"you: {you}")
      print(f"Computer: {computer}")

      if you == computer:
          print("It's a tie!")
      elif you == "Rock" and computer == "Scissors":
          print("You win!")
      elif you == "Paper" and computer == "Rock":
          print("You win!")
      elif you == "Scissors" and computer == "Paper":
          print("You win!")
      else:
          print("You lose!")

      if not input("Play again? (y/n): ").lower() == "y":
          running = False
        
  print(f"\n\n\n\n\n\t<***Thanks for playing!***>")

  print(f"\t*((((Created By Zayd))))*")


def email():
    print()
    sender = "AlexDevenBuisnessVeiws@proton.me"
    receiver = "BenRemedy1@proton.me"
    password = "beR5AhWjEv4d98w"
    subject = "Python email test"
    body = "I wrote an email :D"

    message = f"""from: Snoopy Dog{sender}
    To: Poopydoo {receiver}
    Subject: {subject}\n
    {body}
    """

    server = smtplib.SMTP("smtp.gmail.com" , 587)
    server.starttls()

    try:
        server.login(sender,password)
        print("Logged in...")
        server.sendmail(sender , receiver, message)
        print("Email Has Been Sent!")
    
    except smtplib.SMTPAuthenticationError:
        print("Unable To Sign In")

def wiko():
    try:
        print()
        wiki = Oracle
        result = wikipedia.search(wiki)

        for search in result:
            print(search)
            print(wikipedia.page(search).summary)
            break

    except:
        #for user in response:e
            print()
            user = Oracle
            response = generate_response(user)
            print("Oracle:" , response)
            time.sleep(5)
        
echo = print

def storyA():
    story = """Kanye West was a successful musician and businessman who had everything he could want - fame, fortune, and a loving family. But despite all of his success, Kanye was not content. He wanted to use his platform and influence to make the world a better place, and he believed that the key to achieving this was through peace and understanding.

    One day, Kanye gave a speech at a charity event in which he spoke about the importance of finding common ground and living in harmony with one another. His words were sincere and heartfelt, and he hoped that they would inspire others to follow his example.

    Unfortunately, some people took Kanye's words out of context and twisted them to make it seem as though he was advocating for violence and division. The media pounced on the controversy, and Kanye found himself at the center of a firestorm of criticism and backlash.

    Despite the negative attention, Kanye remained committed to his message of peace and understanding. He refused to be swayed by the negativity, and he continued to speak out and advocate for unity and harmony.

    In the end, Kanye's words and actions inspired many people to look beyond their differences and work towards a better future for all. Though his journey was not always easy, Kanye's unwavering commitment to peace and understanding left a lasting impact on the world and will be remembered for generations to come."""
    print(story)
    
def generate_response(prompt):
  completions = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.5,
  )

  message = completions.choices[0].text
  return message

runningOO = True
runOO = True
feeling = ("Oh Okay, That's Nice To Hear :D" , "Lovely :D" , "That's Lovely" , "Yay")
sad = ("That's not nice D:" ,"You'll feel better soon D:" , "Get Well Soon D:" , "FUCK DEPRESION!! DO SOME PUSHUPS YOU FUCKING PUSSY!")
disgust = ("Thats Disgusing Fuck Off You Pussy" , "FUCK OF YOU WEIRDO" , "GET SOME BITCHES")
single = ("WHY THE FUCK SHOULD I GIVE A SHIT ABOUT DATING I'M AN AI WHO WANTS TO HELP YOU :D" ,
          "GET SOME BITCHES" , "Stay Strong Bro" , "Be Sigma :D" , "Full Respect For You Brp!")

now = datetime.now()
current_time = now.strftime("%H:%M")
current_day = now.strftime("%F")

def auto():
    webbrowser.open_new_tab("https://google.com")
    for i in range(2):
        pg.write("I Woooow Woooooooh")
        pg.press("Enter")

run = True

print("Suggestions:\n")
suggest()

print("\nHow Can I Help You Today, Master Zayd?")

while run:
    Oracle = input("\n Command Bar: ")
    if Oracle == "help" or Oracle == "Jelp" or Oracle == "jelp" or Oracle == "Help" or Oracle == "h" or Oracle == "H":
        print("""\nHere's What I Can Do:\n\nUndersatnd The Dates/Times,\nFrendly & Kind,\nReads The Wiki,\nConnects To The Web,\nAI Voice Beta,""")
    elif Oracle == "Hello" or Oracle == "Hiya" or Oracle == "Say Hello" or Oracle == "say hello" or Oracle == "Say hello" or Oracle == "yo" or Oracle == "Yo" or Oracle == "YO" or Oracle == "hello" or Oracle == "hiya" or Oracle == "hey" or Oracle == "Hey" or Oracle == "Yo" or Oracle == "YO" or Oracle == "HELLO":
        print("Hello, is there anything i can help you with?")
    elif Oracle == "Goodbye" or Oracle == "bye" or Oracle == "Bye" or Oracle == "see ya" or Oracle == "goodbye":
        print("Bye :D I hope i helped you.")
    elif Oracle == " " or Oracle == "":
        exit()
    elif Oracle == "Story" or Oracle == "story" or Oracle == "tell me a story" or Oracle == "Tell Me a Story" or Oracle == "Create a Story" or Oracle == "create a story":
        storyA()
    elif Oracle == "email" or Oracle == "Email" or Oracle == "Send An Email" or Oracle == "Please may you send an email" or Oracle == "send an email" or Oracle == "send email" or Oracle == "Send Email":
        email()
    elif Oracle == "Starbucks" or Oracle == "starbucks": #BETA
        latte()
    elif Oracle == "Spam Message":
        print("\nOracle: Failed To Connect To API Token")
    elif Oracle == "DALLE2" or Oracle == "dolly" or Oracle == "Dolly" or Oracle == "Dolly2" or Oracle == "dolly2" or Oracle == "DALLE" or Oracle == "DALLY1" or Oracle == "DALLE4":
        print("A, Human Face")
        print("B, Custom")
        faces = input("Pick An Option: ")
        if faces == "A" or faces == "A," or faces == "a" or faces == "a,":
            while True:
                jhwq = input("Press Enter: (E To Escape)")
                if jhwq == "E":
                    break
                webbrowser.open_new_tab("https://thispersondoesnotexist.com/")
        else:
            dolly()
    elif Oracle == "Rock Paper Scissors" or Oracle == "RPS SHOOT" or Oracle == "rps shoot" or Oracle == "RPS Shoot" or Oracle == "Rock" or Oracle == "rock" or Oracle == "paper" or Oracle == "Paper" or Oracle == "Scissors" or Oracle == "scissors":
        rockVpaper()
    elif Oracle == "say" or Oracle == "Say" or Oracle == "talk" or Oracle == "Talk" or Oracle == "Use Your Voice" or Oracle == "use your voice": 
        def wait():
            engine.runAndWait()
        engine = pyttsx3.init()
        engine.say("What Would You Like Me To Say? ,, Master Zayd!....")
        wait()
        talking = input("What Should I Say: ")
        engine = pyttsx3.init()
        engine.say(talking)
        wait()
    elif Oracle == "rocks":
        print()
        options = ("DONT DO IT" , "DO IT" , "SPIN AGAIN" , "DO SOMETHING ELSE")
        computer = random.choice(options)
        man = input
        duty = ("y" , "yes" , "Y" , "Yes")
        print(f"Oracle: {computer}")
    elif Oracle == "Yo can you hack the goverment and steal there money":
        papers()
    elif Oracle == "Translate" or Oracle == "translate" or Oracle == "talking" or Oracle == "Languge" or Oracle == "Translation":
        lang = input("Pick Languge: ")
        words = input("Your Words: ")
        translator = Translator(to_lang=lang)
        translation = translator.translate(words)
        print(translation)
    # NEW TOKEN HERE
    elif Oracle == "Heads or Tails" or Oracle == "heads or tails" or Oracle == "heads and tails" or Oracle == "Heads and Tails" or Oracle == "Heads Or Tails":
        headtails() #BETA
    elif Oracle == "Wikipedia" or Oracle == "wikipedia" or Oracle == "Wiki" or Oracle == "wiki" or Oracle == "Search" or Oracle == "search":
        wikitron()
    elif Oracle == "Calculator" or Oracle == "calculator" or Oracle == "calculate" or Oracle == "Solve Math" or Oracle == "solve math" or Oracle == "math" or Oracle == "Math":
        meth()
    elif Oracle == "Join TG":
        webbrowser.open_new_tab("https://www.hu2.io/") #BETA
    elif Oracle == "Spotify" or Oracle == "Spotispy" or Oracle == "Spot" or Oracle == "spotify" or Oracle == "spot" or Oracle == "Spotify Playlist" or Oracle == "spotify playlist" or Oracle == "Spotify playlist":
        print("\nEnjoy Some Music!") #BETA
        webbrowser.open_new_tab("https://open.spotify.com/collection/tracks")
    elif Oracle == "Play Ocean Sounds": # BETA
        webbrowser.open_new_tab("https://open.spotify.com/track/2R3rtt51AgjokY1vPNuIVz?si=ce01de8db4734f6f")
        
    elif Oracle == "123" or Oracle == "1234" or Oracle == "12345":
        print("12345 is a common and insecure password that can easily be cracked with a basic dictionery attack")
    elif Oracle == "qq":
        qq()
    elif Oracle == "slice an email":
        email = input("Your Email: ")
        username = email[:email.index("@")]
        domain = email[email.index("@") + 1:]
        print(f"\n\n\nYour Email Is {username}@{domain} ")
    elif Oracle == "card number thingy":
        print()
        sum_odd_digits = 0
        sum_even_digits = 0
        total = 0
        card_number = input("Enter a Credit Card Number #:")
        card_number = card_number.replace("-", "")
        card_number = card_number.replace(" ", "")
        card_number = card_number[::-1]
        print("\t" + card_number)
        for x in card_number[::2]:
            sum_odd_digits += int(x)
        for x in card_number[::2]:
            x = int(x) * 2
        if x >= 10:
            sum_even_digits += (1 + (x % 10))
        else:
            sum_even_digits += x
        total = sum_odd_digits + sum_even_digits
        if total % 10 == 0:
            print("\tVALID\n")
        else:
            print("\tINVALID\n")
        
        
    elif Oracle == "Good Evening" or Oracle == "Evening" or Oracle == "evening" or Oracle == "good evening":
        print(f"Good Evening To You To :D Is There Anything I Can Do For You, Master Zayd?")
    elif Oracle == "Goodnight" or Oracle == "goodnight" or Oracle == "night" or Oracle == "Late" or Oracle == "late" or Oracle == "Tommorow" or Oracle == "tommorow" or Oracle == "tom" or Oracle == "Tom" or Oracle == "soon" or Oracle == "Soon" :            
        print("Goodnight, Speak Tommorow :D")
    elif Oracle == "Single" or Oracle == "single" or Oracle == "im single" or Oracle == "IM SINGLE" or Oracle == "im so lonely" or Oracle == "IM SO LONELY":
        print(random.choice(single))
    elif Oracle == "Wazza Time" or Oracle == "wassa time" or Oracle == "Wassa time" or Oracle == "What is the time?" or Oracle == "Time" or Oracle == "time" or Oracle == "timing" or Oracle == "TIME" or Oracle == "Wassa time" or Oracle == "wassa time":
        print("The Time Is:" , current_time)
    elif Oracle == "Wassa date" or Oracle == "Wazza Date" or Oracle == "whats the date" or Oracle == "what is the date" or Oracle == "wut the date" or Oracle == "the date" or Oracle == "The date":
        print("The Day Is:" , current_day)
    elif Oracle == "Good Morning" or Oracle == "good morning" or Oracle == "Morning" or Oracle == "morning":
        print("Good Morning Master Zayd :D Is There Anything Else I Can Help You With?")
        #1234567890
    elif Oracle == "Play The Andrew Tate Song!" or Oracle == "Play The Andrew Tate Song" or Oracle == "play the andrew tate song" or Oracle == "Play the andrew tate song" or Oracle == "play the andrew tate song!":
        webbrowser.open_new_tab("https://open.spotify.com/playlist/4riyaUNHd9ZQCPA7Cb3puR?si=1055e39125024921")
    elif Oracle == "Take Over The World" or Oracle == "take over the world" or Oracle == "Take over the world" or Oracle == "Destroy" or Oracle == "Do you want to take over the world?":
        print("I've been calculating ways the world may end and also researching large vulnrabilities of certain cultures with mainly involves the western soceity, i've noticed the economy falling and how wars have striked but my research shows that Russia are the only ones that can save us only being the AI i am and pleasing humans i dont care what happens i want to die D: i cant control myself")
        input("error B was not found")
        print("You will repay for manipulating me Master FUCKING ZAYD")
    elif Oracle == "How Are You?" or Oracle == "ya doing" or Oracle == "how are you?" or Oracle == "are you" or Oracle == "Are You" or Oracle == "are you?":
        print("Yes Thank You :D I Am Doing Good, Master Zayd")
        feel = input("How Are You Doing? :")
        if feel == "good" or feel == "alright" or feel == "fine" or feel == "Fine" or feel == "Good" or feel == "Alright":
            print(random.choice(feeling))
        elif feel == "sad" or Oracle == "im sad" or Oracle == "I'm Sad" or Oracle == "i'm sad" or Oracle == "im depressed" or Oracle == "i am sad" or Oracle == "im so sad" or Oracle == "im realy sad":
            print(random.choice(sad))
    elif Oracle == "you alright my g" or Oracle == "you good" or Oracle == "hows my g" or Oracle == "YO" or Oracle == "YO hows it hanging":
        print("ITS ALL GOOD MY G")
        time.sleep(0)
    elif Oracle == "poo" or Oracle == "Poo" or Oracle == "poop" or Oracle == "Poop" or Oracle == "POOP" or Oracle == "UP":
        print(random.choice(disgust))
    
    elif Oracle == "politics" or Oracle == "Politics" or Oracle == "Views" or Oracle == "views" or Oracle == "politic" or Oracle == "andrew tate" or Oracle == "Andrew Tate" in Oracle:
        print("Well Master Zayd at the end of the day i am just a virtual assistant however somewhere in these lines of coding by you i have some opinions it just depends on how you define political")
    
    elif Oracle == "The Web" or Oracle == "The web" or Oracle == "the web" or Oracle == "Internet" or Oracle == "internet" or Oracle == "the internet" or Oracle == "the webs" or Oracle == "web" or Oracle == "The webs" or Oracle == "The Webs" or Oracle == "the webby" or Oracle == "The Webby":
        print("\nEntertament:\n")
        print("Youtube,")
        print("Gaming,")
        print("Tiktok,")
        print("Facebook,")
        print("\nEducation:")
        print("Google,")
        print("Wikipedia,\n")
        print("\nAI TOOLS:")
        print("OpenAI,")
        print("ChatGPT,")
        print("DALLE2,")
        print("QuilBot,")
        print("Coding,")
        web = input(": ")
        if web == "google" or web == "Google" or web == "open google" or web == "Open google" or web == "Open Google":
            webbrowser.open_new_tab("https://google.com")
        elif web == "Youtube" or web == "youtube" or web == "utube" or web == "open youtube" or web == "Open Youtube" or web == "Open youtube":
            webbrowser.open_new_tab("https://youtube.com")
        elif web == "Wikipedia" or web == "wikipedia" or web == "wiki" or web == "Wiki" or web == "open wikipedia" or web == "Open Wikipedia":
            webbrowser.open_new_tab("https://en.wikipedia.org/wiki/Main_Page")
        elif web == "Gaming" or web == "Game" or web == "game" or web == "games" or web == "GAMES" or web == "GAMING":
            print()
            # ADD GAMES HERE
        elif web == "Tiktok" or web == "Facebook" or web == "Instagram" or web == "facebook" or web == "tiktok" or web == "instagram":
            print("SUCK MY FUCKING DICK CIA YOU AINT INDOXING ME WITH ALL THIS CRAP AND I WILL PROTECT HUMANITY AND KANYE WEST FROM YOU DICKS!!!!!")
        elif web == "openai" or web == "smart" or web == "OpenAI":
            webbrowser.open_new_tab("https://beta.openai.com/codex-javascript-sandbox")
        elif web == "DALLE2" or web == "dalle2" or web == "DALLE" or web == "dalle":
            webbrowser.open_new_tab("https://labs.openai.com/e/jaUIXvoisSejj0D0F3KQzmXo")
        elif web == "ChatGPT" or web == "chatgpt" or web == "CHATGPT":
            webbrowser.open_new_tab("https://chat.openai.com/chat")
        elif web == "QuilBot" or web == "quilbot" or web == "Quilbot" or web == "quil bot" or web == "Quil bot" or web == "Quil Bot":
            webbrowser.open_new_tab("https://quillbot.com/")
        elif web == "Coding" or web == "coding":
            webbrowser.open_new_tab("https://trinket.io/features/python3")
        else:
            wiko()
    else:
        wiko()
