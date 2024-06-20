light_speed = 300000000

def main():
    mass = int(input("m: "))
    print("E:", energy(mass))

def energy(m):
    return m * pow(light_speed, 2)

main()
