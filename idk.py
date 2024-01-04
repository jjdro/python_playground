import subprocess

# Define the file path of the Python script
file_path = "counting_text.py"

# Run the Python script and capture its output
output = subprocess.check_output(["python", file_path], universal_newlines=True)

# Print the output
print(output)
