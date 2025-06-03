# Constants for gravity on different planets
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14
EARTH_GRAVITY = 1.0

def main():
    # Prompt the user for their weight on Earth
    earth_weight = float(input("Enter a weight on Earth: "))

    # Prompt the user for the name of a planet
    planet = input("Enter a planet (Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune): ")

    # Determine the gravity multiplier for the selected planet
    if planet == "Mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity_constant = VENUS_GRAVITY
    elif planet == "Mars":
        gravity_constant = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity_constant = URANUS_GRAVITY
    elif planet == "Neptune":
        gravity_constant = NEPTUNE_GRAVITY
    else:
        print("Invalid planet name. Please use capital first letter, e.g., 'Mars'.")
        return

    # Calculate and round the weight
    planetary_weight = earth_weight * gravity_constant
    rounded_weight = round(planetary_weight, 2)

    # Output the result
    print("The equivalent weight on " + planet + ": " + str(rounded_weight) + " kg")

# Correct check to run main
if __name__ == "__main__":
    main()
