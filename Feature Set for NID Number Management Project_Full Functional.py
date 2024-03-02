class NIDManagement:
    def __init__(self):
        self.nid_numbers = []

    def add_nid(self):
        nid = input("Enter the NID number to add: ")
        self.nid_numbers.append(nid)
        print("NID number added successfully.")

    def display_nids(self):
        if self.nid_numbers:
            print("List of NID numbers:")
            for nid in self.nid_numbers:
                print(nid)
        else:
            print("No NID numbers found.")

    def delete_nid(self):
        nid = input("Enter the NID number to delete: ")
        if nid in self.nid_numbers:
            self.nid_numbers.remove(nid)
            print("NID number deleted successfully.")
        else:
            print("NID number not found.")

    def update_nid(self):
        old_nid = input("Enter the NID number to update: ")
        if old_nid in self.nid_numbers:
            new_nid = input("Enter the new NID number: ")
            index = self.nid_numbers.index(old_nid)
            self.nid_numbers[index] = new_nid
            print("NID number updated successfully.")
        else:
            print("NID number not found.")

# Sample usage:
nid_manager = NIDManagement()

while True:
    print("\n1. Add NID number")
    print("2. Display NID numbers")
    print("3. Delete NID number")
    print("4. Update NID number")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        nid_manager.add_nid()
    elif choice == "2":
        nid_manager.display_nids()
    elif choice == "3":
        nid_manager.delete_nid()
    elif choice == "4":
        nid_manager.update_nid()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please enter a valid option.")


