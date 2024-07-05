def copy_file_line_by_line(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            with open(destination_file, 'w') as dst:
                for line in src:
                    dst.write(line)
        print(f"Contents of {source_file} have been copied to {destination_file}.")
    except FileNotFoundError:
        print(f"Error: {source_file} not found.")
    except IOError as e:
        print(f"Error: {e}")

# Example usage
source_file = 'source.txt'
destination_file = 'destination.txt'
copy_file_line_by_line(source_file, destination_file)
