import os

def total_salary(path):
    try:
        total_sum = 0
        count = 0
        # Open the file using the context manager
        with open(path, 'r', encoding='utf-8') as file:
            # Iterate through each line in the file
            for line in file:
                # Split the line into name and salary
                parts = line.strip().split(',')
                salary = int(parts[1])  # Convert the salary part to integer
                total_sum += salary  # Add the salary to the total sum
                count += 1  # Increment the count of developers

        if count > 0:
            average_salary = total_sum / count  # Calculate the average salary
        else:
            average_salary = 0

        # Return total sum and average salary
        return total_sum, average_salary
    except FileNotFoundError:
        # Handle the case where the file is not found
        print("Error: The file was not found.")
        return None
    except Exception as e:
        # Handle other possible exceptions
        print(f"An error occurred: {e}")
        return None


print(os.path.exists("GoIT\goit-pycore-hw-04\Task_1_file.txt"))

#Example of function usage
total, average = total_salary("GoIT\goit-pycore-hw-04\Task_1_file.txt")
print(f"Total salary sum: {total}, Average salary: {average}")

