# def write_employees_to_file(employee_list, path):
#     # Open the file in "w" mode (write mode)
#     file = open(path, "w")

#     # Iterate through the list of employee lists
#     for department in employee_list:
#         # Iterate through each employee in the department
#         for employee in department:
#             # Write each employee on a new line
#             file.write(employee + "\n")

#     # Close the file
#     file.close()

# # Example usage:
# employee_list = [['60b90c1c13067a15887e1ae1,Tayson,3', '60b90c2413067a15887e1ae2,Vika,1'], ['60b90c2e13067a15887e1ae3,Barsik,2']]
# path_to_file = "employees.txt"

# write_employees_to_file(employee_list, path_to_file)

# def read_employees_from_file(path):
#     # Open the file in "r" mode (read mode)
#     file = open(path, "r")

#     # Read lines from the file and remove the newline character
#     employees = [line.strip() for line in file.readlines()]

#     # Close the file
#     file.close()

#     return employees

# # Example usage:
# path_to_file = "employees.txt"

# employees_list = read_employees_from_file(path_to_file)
# print(employees_list)

# def add_employee_to_file(record, path):
#     # Open the file in "a" mode (append mode)
#     file = open(path, "a")

#     # Add the employee record to the file on a new line
#     file.write(record + "\n")

#     # Close the file
#     file.close()

# # Example usage:
# path_to_file = "employees.txt"
# employee_record = "60b90c1c13067a15887e1ae1,Tayson,3"

# add_employee_to_file(employee_record, path_to_file)

# def get_cats_info(path):
#     cats_list = []

#     # Open the file in "r" mode using a with statement
#     with open(path, "r") as file:
#         # Iterate through each line in the file
#         for line in file:
#             # Split the line into parts using comma as a separator
#             parts = line.strip().split(',')

#             # Extract cat information from parts
#             cat_info = {
#                 "id": parts[0],
#                 "name": parts[1],
#                 "age": parts[2]
#             }

#             # Append cat information to the list
#             cats_list.append(cat_info)

#     return cats_list



# # Example usage:
# path_to_file = "employees.txt"

# cats_info = get_cats_info(path_to_file)
# print(cats_info)


# # def sanitize_file(source, output):
# #     # Open the source file in "r" mode using a with statement
# #     with open(source, "r") as source_file:
# #         # Read the contents of the source file
# #         source_content = source_file.read()

# #     # Remove digits from the content
# #     sanitized_content = ''.join(char for char in source_content if not char.isdigit())

# #     # Open the output file in "w" mode using a with statement
# #     with open(output, "w") as output_file:
# #         # Write the new contents to the output file
# #         output_file.write(sanitized_content)

# def sanitize_file(source, output):
#      with open(source, "r") as file:
#          source_content = file.read()

#      prepared_content = ''.join(char for char in source_content if not char.isdigit())
   
#      with open(output, "w") as output:
#         output.write(prepared_content)  

# # Example usage:
# source_file_path = "employees.txt"
# output_file_path = "output.txt"

# sanitize_file(source_file_path, output_file_path)


def save_applicant_data(source, output):
    with open(output, "w") as output:
        for application in source:
            prepared_content = f"{application['name']},{application['specialty']},{application['math']},{application['lang']},{application['eng']}\n"
            output.write(prepared_content)  


def save_applicant_data(source, output):
    # Open the output file in "w" mode using a with statement
    with open(output, "w") as output_file:
        # Iterate through each applicant in the source list
        for applicant in source:
            # Create a formatted string with applicant's data
            applicant_data = f"{applicant['name']},{applicant['specialty']},{applicant['math']},{applicant['lang']},{applicant['eng']}\n"

            # Write the formatted string to the output file
            output_file.write(applicant_data)

source = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]
save_applicant_data(source,"output.txt")
