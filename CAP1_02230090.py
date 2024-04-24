# Function to read input from a file
def load_input(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read lines from the file and strip spaces
            lines = file.readlines()
            input_data = [line.strip().replace(' ', '') for line in lines]
            return input_data
    except FileNotFoundError:
        # Handle the case when the file is not found
        print(f"File '{file_path}' not found.")
        return []

# Function to calculate the score based on given conditions
def calculate_total_score(input_data):
    # Assign scores for different conditions
    A = 1
    B = 2
    C = 3
    X = 0
    Y = 3
    Z = 6
    
    # Initializing the total score
    total_score = 0
    
    # Iterate through input conditions
    for conditions in input_data:
        if conditions == 'AX':
            # If opponent chooses Rock and the event should end by loss
            # I should choose scissor and accordingly score is updated
            total_score += C + X
        elif conditions == 'AY':
            # If opponent chooses Rock and the event should end by draw
            # I should choose ROCK and accordingly score is updated
            total_score += A + Y
        elif conditions == 'AZ':
            # If opponent chooses Rock and the event should end by win
            # I should choose paper and accordingly score is updated
            total_score += B + Z
        elif conditions == 'BX':
            total_score += A + X
        elif conditions == 'BY':
            total_score += B + Y
        elif conditions == 'BZ':
            total_score += C + Z
        elif conditions == 'CX':
            total_score += B + X
        elif conditions == 'CY':
            total_score += C + Y
        elif conditions == 'CZ':
            total_score += A + Z

    # Returning the total score 
    return total_score

# File path containing input data
file_path = 'input_0_cap1.txt'

# Read input from file
input_data = load_input(file_path)

# Check if input data is available
if input_data:
    # Calculate total score based on input data
    total_score = calculate_total_score(input_data)
    print(f"Total score: {total_score}")
