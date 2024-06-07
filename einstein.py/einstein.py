def calculate_energy(masskg):
    sol=300000000
    joul_energy=(masskg)*(sol**2)
    return int(joul_energy)
def main():
    mass_input=input("m :")
    masskg=int(mass_input)
    joul_energy=calculate_energy(masskg)
    print(joul_energy)
main()

