FILE_PATH = r"C:\Users\HP\OneDrive\Desktop\python file\file.txt"

def write_file():
    print("Enter your text (type 'END' to finish):")
    
    lines = []
    
    while True:
        data = input()
        if data == "END":
            break
        lines.append(data)

    print("\nPress 1 to Save")
    print("Press 2 to Not Save")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            with open(FILE_PATH, "w") as file:
                for line in lines:
                    file.write(line + "\n")
            print("Data saved successfully!")
        except Exception as e:
            print("Error:", e)
    
    elif choice == "2":
        print("Data not saved.")
    
    else:
        print("Invalid choice!")

# Run function
if __name__ == "__main__":
    write_file()