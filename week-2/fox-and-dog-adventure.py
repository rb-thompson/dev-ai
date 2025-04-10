# A tale of a fox and a dog
# This code demonstrates the use of various Python concepts including variables, arithmetic operations,
# conditional statements, loops, and data structures like lists and dictionaries.

def fox_and_dog_adventure():
    # Basic variable types
    fox_speed = 15  # int: Fox's running speed (meters per second)
    dog_rest_time = 3.5  # float: Dog's napping time (hours)
    fox_name = "Quick Brown Fox"  # str: Fox's name
    dog_is_lazy = True  # bool: Is the dog lazy?
    jump_distances = [2, 4, 6, 8]  # list: Distances fox jumps (meters)
    animal_traits = {"fox": "cunning", "dog": "lazy"}  # dict: Traits of each animal

    # Arithmetic operators: Calculate total distance fox jumps
    total_jump_distance = jump_distances[0] + jump_distances[1] * 2 - jump_distances[2] / 3
    print(f"{fox_name} jumps a total of {total_jump_distance:.2f} meters!")

    # Conditional statement 1: Check if fox jumps far enough
    if total_jump_distance > 10:
        print(f"{fox_name} leaps impressively far!")
    elif total_jump_distance > 5:
        print(f"{fox_name} makes a decent jump.")
    else:
        print(f"{fox_name} barely clears the ground.")

    # Conditional statement 2: Compare fox speed to dog speed
    dog_speed = 10  # Dog's speed when awake
    if fox_speed > dog_speed and dog_is_lazy:
        print("The fox outruns the lazy dog!")
    elif fox_speed == dog_speed or not dog_is_lazy:
        print("The dog might catch up if it wakes up!")
    else:
        print("The dog naps while the fox leaps ahead.")

    # For loop with conditional: Fox jumps over obstacles
    obstacles = ["log", "fence", "lazy dog"]
    for obstacle in obstacles:
        if obstacle == "lazy dog" and dog_is_lazy:
            print(f"{fox_name} easily jumps over the {obstacle} while it sleeps.")
        else:
            print(f"{fox_name} jumps over the {obstacle} with effort.")

    # While loop with conditional: Dog naps and wakes up
    nap_time_left = dog_rest_time
    while nap_time_left > 0:
        if nap_time_left > 2:
            print(f"Dog naps deeply for {nap_time_left:.1f} hours...")
        elif nap_time_left > 1:
            print(f"Dog stirs slightly, napping for {nap_time_left:.1f} hours...")
        else:
            print(f"Dog is almost awake, napping for {nap_time_left:.1f} hours...")
        nap_time_left -= 1  # Decrease nap time by 1 hour each iteration
    print("The lazy dog finally wakes up!")

    # Conditional statement 3: Check animal traits
    fox_trait = animal_traits["fox"]
    if fox_trait == "cunning" and dog_is_lazy:
        print(f"The {fox_trait} fox outsmarts the lazy dog every time!")
    else:
        print("The animals' traits lead to an unexpected twist.")

    # Bonus: The famous pangram
    pangram = "The quick brown fox jumps over the lazy dog"
    print(f"\nFamous saying: '{pangram}'")

# Run the adventure
if __name__ == "__main__":
    fox_and_dog_adventure()