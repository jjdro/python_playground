import subprocess

def interact_with_subprocess():
    # Start the subprocess
    subprocess.Popen(['python', 'counting_text2.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    while True:
        # Get user input from the console
        user_input = input("Enter a command: ")

        # Send the user input to the subprocess
        subprocess.stdin.write(user_input.encode())
        subprocess.stdin.write(b'\n')
        subprocess.stdin.flush()

        # Read the output from the subprocess
        output = subprocess.stdout.readline().decode().strip()

        # Print the output
        print(output)

        # Check if the subprocess has finished
        if subprocess.poll() is not None:
            break

    # Close the subprocess
    subprocess.stdin.close()
    subprocess.stdout.close()
    subprocess.terminate()

# Call the function to start the interaction
interact_with_subprocess()
