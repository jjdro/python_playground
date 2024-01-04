import subprocess

# Define the command to run the subprocess
command = ['python', 'counting_text.py']
command2 = ['python', 'echo_test.py']

while True:
    # Create a subprocess and redirect the input and output streams22
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process2 = subprocess.Popen(command2, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Write data to the subprocess
    input_data = input("what send?")
    process.stdin.write(input_data)
    #process.stdin.close()
    process2.stdin.write(input_data)
    process2.stdin.close()

    # Read the output from the subprocess
    output = process.stdout.read()
    output2 = process2.stdout.read()
    process.stdin.write(input_data)
    print(output)
    output = process.stdout.read()
    # Wait for the subprocess to finish
    process.wait()

    # Print the output
    print(output)
    print(output2)

    if input_data == "exit":
        break

print("done!")