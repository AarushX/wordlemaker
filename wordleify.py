import re

def process_file(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            words = infile.read().split()
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found. Please try again.")
        return False
    except IOError:
        print(f"Error: Unable to read the file '{input_file}'.")
        return False

    pattern = re.compile(r'^[a-zA-Z]{5}$')
    filtered_words = [word for word in words if pattern.match(word)]

    try:
        with open(output_file, 'w') as outfile:
            outfile.write('\n'.join(filtered_words))
    except IOError:
        print(f"Error: Unable to write to the file '{output_file}'.")
        return False

    print(f"Processing complete. Filtered words are saved to '{output_file}'.")
    return True

def main():
    output_file = 'output.txt'
    while True:
        input_file = input("What is the path of the file to input: ")
        output_file = "OUT_" + input_file
        if process_file(input_file, output_file):
            break

main()
