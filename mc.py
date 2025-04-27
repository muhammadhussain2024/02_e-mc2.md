# Constant for the speed of light
C = 299792458  # meters per second

def main():
    # Read mass from the user
    mass = float(input("Enter kilos of mass: "))

    # Print steps
    print("\ne = m * C^2...\n")
    print("m =", mass, "kg")
    print("C =", C, "m/s")

    # Calculate energy
    energy = mass * C**2

    # Print the result
    print("\n" + str(energy) + " joules of energy!")

# Required to call main function
if __name__ == '__main__':
    main()
