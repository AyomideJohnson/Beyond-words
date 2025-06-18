def separate_data(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    with open('12andLower.txt', 'w') as file_12_lower, \
            open('13and14.txt', 'w') as file_13_14, \
            open('15.txt', 'w') as file_15:

        for line in lines:
            parts = line.strip().split(' ')

            if not parts[0].isdigit():
                # Skip the line if the first element is not a valid integer
                continue

            first_integer = int(parts[0])

            if first_integer < 6:
                # Do nothing and move to the next line
                pass
            elif first_integer < 13:
                file_12_lower.write(line)
            elif first_integer in (13, 14):
                file_13_14.write(line)
            else:
                file_15.write(line)


if __name__ == "__main__":
    input_file = "decider.txt"
    separate_data(input_file)




