class CarFinder:
   def __init__(self):
       self.allowed_vehicles = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']
   def print_allowed_vehicles(self):
       print("Allowed Vehicles:")
       for vehicle in self.allowed_vehicles:
           print(vehicle)
   def display_menu(self):
       print("*********************************")
       print("AutoCountry Vehicle Finder v0.2")
       print("*********************************")
       print("Please Enter the following number below from the following menu:")
       print("1. Print all allowed Vehicles")
       print("2. SEARCH for Authorized Vehicle")
       print("3. Exit")
   def run(self):
       while True:
           self.display_menu()
           choice = input("Enter your choice: ")
           if choice == '1':
               self.print_allowed_vehicles()
           elif choice == '2':
             vehicle_name = input("Enter the name of the authorized vehicle:")
             if vehicle_name in self.allowed_vehicles:
               print("Authorized Vehicle:", vehicle_name)
             if vehicle_name not in self.allowed_vehicles:
               print("Is not an authorized vehicle:", vehicle_name)
             
           if choice == '3':
             print("Thank you for using the AutoCountry Vehicle Finder, good-bye!!")
             break
                  
           
if __name__ == "__main__":
   car_finder = CarFinder()
   car_finder.run()