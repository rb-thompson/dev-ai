import random

# Game setup
locations = ["Stage", "Prop Room", "Costume Shop", "Green Room"]
props = ["Crown", "Sword", "Goblet", "Mask", "Candle", "Book", "Fan", "Ring"]
max_turns = 10

# Initialize prop locations (randomly assign props to locations)
prop_locations = {prop: random.choice(locations) for prop in props}

# Get number of players
num_players = int(input("How many players? (2-4): "))
while num_players < 2 or num_players > 4:
    print("Please choose 2 to 4 players.")
    num_players = int(input("How many players? (2-4): "))

# Initialize player data
players = {}
for i in range(num_players):
    name = input(f"Enter name for Player {i+1}: ")
    players[name] = {"props": [], "score": 0}

# Game loop
current_turn = 1
while current_turn <= max_turns:
    print(f"\n--- Turn {current_turn} ---")
    for player in players:
        # Display available locations
        print(f"\n{player}'s turn. Locations: {locations}")
        choice = input("Choose a location to search: ").title()
        
        # Validate location
        while choice not in locations:
            print(f"Invalid location. Choose from: {locations}")
            choice = input("Choose a location to search: ").title()
        
        # Check for props in the chosen location
        found = False
        for prop, loc in prop_locations.items():
            if loc == choice and prop not in players[player]["props"]:
                players[player]["props"].append(prop)
                players[player]["score"] += 1
                print(f"{player} found a {prop}!")
                found = True
                # Remove prop so it can't be found again
                del prop_locations[prop]
                break
        if not found:
            print(f"No props found in {choice}.")
    
    current_turn += 1

# End game and show results
print("\n--- Game Over ---")
print("Final Scores:")
winner = None
highest_score = -1

for player, data in players.items():
    score = data["score"]
    props_found = data["props"]
    print(f"{player}: {score} props ({', '.join(props_found)})")
    if score > highest_score:
        highest_score = score
        winner = player

print(f"\nThe winner is {winner} with {highest_score} props!")