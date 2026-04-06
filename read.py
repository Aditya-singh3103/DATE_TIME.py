FILE_PATH = r"C:\Users\HP\OneDrive\Desktop\python file\file.txt"

# Read file
with open(FILE_PATH, "r") as file:
    lines = file.readlines()

print("Current Content:")
for i in range(len(lines)):
    print(i + 1, ":", lines[i].strip())

# Modify line
line_no = int(input("Enter line number to modify: "))
new_text = input("Enter new text: ")

lines[line_no - 1] = new_text + "\n"

# Save option
choice = input("Save changes? (1 = Yes, 2 = No): ")

if choice == "1":
    with open(FILE_PATH, "w") as file:
        file.writelines(lines)
    print("Saved")
else:
    print("Not Saved")