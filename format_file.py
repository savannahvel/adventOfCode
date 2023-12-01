import sys
import os

def format_file(input_file_path, output_file_path=None):
    # If output_file_path is not provided, save it in the same directory as the input file
    if output_file_path is None:
        output_file_path = os.path.splitext(input_file_path)[0] + '_output.js'

    # Read the input file
    with open(input_file_path, 'r') as file:
        file_content = file.read()

    # Split the content into lines
    lines = file_content.split('\n')

    # Remove empty lines
    lines = [line.strip() for line in lines if line.strip()]

    # Convert the lines to a JavaScript array
    js_array = f'export default {str(lines)};'

    # Write the JavaScript array to the output file
    with open(output_file_path, 'w') as output_file:
        output_file.write(js_array)

    print(f'Formatted data written to {output_file_path}')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python format_file.py <input_file_path> [output_file_path]")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None

    format_file(input_path, output_path)

# python3 format_file.py 2023/Day1/puzzle_input_1.txt