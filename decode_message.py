def decode(message_file):
    # Read the file contents
    with open(message_file, 'r') as file:
        lines = file.readlines()
    
    # Parse the lines to extract numbers and words
    number_word_pairs = {}
    for line in lines:
        # Skip empty lines and ensure proper formatting
        parts = line.strip().split()
        if len(parts) != 2:
            continue
        number, word = parts
        number_word_pairs[int(number)] = word
    
    # Arrange the numbers into a pyramid structure
    pyramid_lines = []
    current_number = 1
    current_length = 1
    while current_number in number_word_pairs:
        current_line = []
        for _ in range(current_length):
            if current_number in number_word_pairs:
                current_line.append(current_number)
            current_number += 1
        pyramid_lines.append(current_line)
        current_length += 1
    
    # Decode the message
    message = []
    for line in pyramid_lines:
        if line:
            message.append(number_word_pairs[line[-1]])
    
    return ' '.join(message)

if __name__ == "__main__":
    decoded_message = decode('message.txt')
    print(decoded_message)
