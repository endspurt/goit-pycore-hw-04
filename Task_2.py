
import os

def get_cats_info(path):
  
    cats_info = []  # Initialize an empty list to store cat information
    try:
        with open(path, 'r', encoding='utf-8') as file:  # Open the file safely with UTF-8 encoding
            for line in file:  # Read each line in the file
                id, name, age = line.strip().split(',')  # Split the line into components
                cat_dict = {'id': id, 'name': name, 'age': age}  # Create a dictionary for the cat
                cats_info.append(cat_dict)  # Append the dictionary to the list
    except Exception as e:  # Handle possible exceptions like file not found or read errors
        print(f"An error occurred: {e}")
    return cats_info  # Return the list of dictionaries


print(os.path.exists("GoIT\goit-pycore-hw-04\Task_2_file.txt"))
# Example usage:
cats_info = get_cats_info("GoIT\goit-pycore-hw-04\Task_2_file.txt")
print(cats_info)

