world = {
    'cave': {
        "description": "You are in a mysterious cave.",
        "exits": {
            "up": "courtyard",
        },
    },
    "tower": {
        "description": "You are at the top of a tall tower.",
        "exits": {
            "down": "gatehouse",
        },
    },
    'courtyard': {
        'description': 'You are in the castle courtyard.',
        'exits': {
            'south': 'gatehouse',
            'down': 'cave',
        },
    },
    'gatehouse': {
        'description': 'You are at the gates of a castle.',
        'exits': {
            'south': 'forest',
            'up': 'tower',
            'north': 'courtyard',
        },
    },
    'forest': {
        'description': 'You are in a forest glade.',
        'exits': {
            'north': 'gatehouse',
        },
    },
}

place = 'cave'
while True:
       location = world[place]
       print(location["description"])
       print("Exits:")
       print(", " .join(location["exits"].keys()))
       direction = input("Where now? ").strip().lower()
       if direction == "quit":
          print("Bye! ")
          break
       elif direction in location["exits"]:
          place = location["exits"][direction]
       else:
          print("I don not understand")
