import requests

def get_joke(category):
    try:
        url = f"https://v2.jokeapi.dev/joke/{category}"
        response = requests.get(url)
        data = response.json()

        print(f"Category: {data['category']}")
        if data['type'] == 'twoparts':
            print(f"Setup: {data['setup']}")
            print(f"Delivery: {data['delivery']}")
        else:
            print(f"Joke: {data['joke']}")
    except Exception as e:
        print(f"Something went wrong: {e}")            
        return

    while True:
        print("... Joke-Generator...")
        print("1. Get a random joke")
        print("2. Get a programming joke")
        print("3. Get a pun joke")
        print("4. Get a spooky joke")
        print("5. Quit")

        try:
            choice = int(input("Pick an option from the options above:  "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 - 5")
            continue

        if choice == 1:
            get_joke("any")
        elif choice == 2:
            get_joke("programming")    
        elif choice == 3:
            get_joke("pun")
        elif choice == 4:
            get_joke("spooky")            
        elif choice == 5:
            print(" Goodbyee!! Thanks for using the Joke-Generator!")
            break
        else:
            print("Invalid input. Please enter a number between 1 - 5")