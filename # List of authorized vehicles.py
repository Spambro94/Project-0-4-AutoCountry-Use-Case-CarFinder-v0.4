# List of authorized vehicles
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan', 'Rivian R1T', 'Ram 1500']

def print_menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.4")
    print("********************************")
    print("Please Enter the following number below from the following menu:\n")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")
    print("********************************")

def print_vehicles():
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
    for vehicle in AllowedVehiclesList:
        print(vehicle)

def search_vehicle():
    vehicle_name = input("\nPlease Enter the full Vehicle name: ").strip()
    # Checking if the vehicle is in the list
    if vehicle_name in AllowedVehiclesList:
        print(f"\n{vehicle_name} is an authorized vehicle")
    else:
        print(f"\n{vehicle_name} is not an authorized vehicle, if you received this in error please check the spelling and try again")

def add_vehicle():
    new_vehicle = input("\nPlease Enter the full Vehicle name you would like to add: ").strip()
    AllowedVehiclesList.append(new_vehicle)
    print(f"\nYou have added \"{new_vehicle}\" as an authorized vehicle")

def delete_vehicle():
    vehicle_name = input("\nPlease Enter the full Vehicle name you would like to REMOVE: ").strip()

    if vehicle_name in AllowedVehiclesList:
        confirmation = input(f"\nAre you sure you want to remove \"{vehicle_name}\" from the Authorized Vehicles List? (yes/no): ").strip().lower()

        if confirmation == "yes":
            AllowedVehiclesList.remove(vehicle_name)
            print(f"\nYou have REMOVED \"{vehicle_name}\" as an authorized vehicle")
        else:
            print("\nRemoval cancelled.")
    else:
        print(f"\n{vehicle_name} is not in the Authorized Vehicles List, please check the name and try again.")

def main():
    while True:
        print_menu()
        user_input = input("Enter your choice: ")

        if user_input == "1":
            print_vehicles()
        elif user_input == "2":
            search_vehicle()
        elif user_input == "3":
            add_vehicle()
        elif user_input == "4":
            delete_vehicle()
        elif user_input == "5":
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("Invalid input, please try again.")

# Running the program
if __name__ == "__main__":
    main()