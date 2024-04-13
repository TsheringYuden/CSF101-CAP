class GameScoreCalculator:
    def __init__(self, playing_a_game):
        # Initialize the object with the path to the input file and the scoring system
        self.playing_a_game = playing_a_game  # Path to the input file
        self.scores = {
            ('A', 'X'): (3, 0),  # Rock vs. Scissors (Win): (Player, Opponent)
            ('A', 'Y'): (1, 3),  # Rock vs. Rock (Draw): (Player, Opponent)
            ('A', 'Z'): (2, 6),  # Rock vs. Paper (Loss): (Player, Opponent)
            ('B', 'X'): (1, 0),  # Paper vs. Rock (Win): (Player, Opponent)
            ('B', 'Y'): (2, 3),  # Paper vs. Paper (Draw): (Player, Opponent)
            ('B', 'Z'): (3, 6),  # Paper vs. Scissors (Loss): (Player, Opponent)
            ('C', 'X'): (2, 0),  # Scissors vs. Rock (Win): (Player, Opponent)
            ('C', 'Y'): (3, 3),  # Scissors vs. Scissors (Draw): (Player, Opponent)
            ('C', 'Z'): (1, 6)   # Scissors vs. Paper (Loss): (Player, Opponent)
        }

    def read_input(self):
        # Read input data from the specified file
        try:
            with open(self.playing_a_game, 'r') as file:
                lines = file.readlines()
                # Extract and format conditions pairs
                input_data = [line.strip().replace(' ', '') for line in lines]
                return input_data
        except FileNotFoundError:
            # Handle the case when the file is not found
            print(f"File '{self.playing_a_game}' not found.")
            return []
        except Exception as e:
            # Handle any other errors that may occur while reading the file
            print(f"An error occurred while reading the file: {e}")
            return []

    def calculate_score(self):
        # Calculate the total score based on the input data and the scoring system
        input_data = self.read_input()
        if not input_data:
            return 0  # Return 0 if input data is empty
        
        total_score = 0
        # Iterate over each conditions pair in the input data
        for conditions in input_data:
            # Extract opponent move and outcome from the conditions pair
            opponent_move, outcome = conditions[0], conditions[1]
            # Look up the corresponding score pair from the scores dictionary
            score_pair = self.scores.get((opponent_move, outcome), (0, 0))  # Default to (0, 0) if not found
            # Update the total score with the player and opponent scores
            total_score += sum(score_pair)
        
        return total_score

# Specify the input file path
playing_a_game = 'CSF101-CAP/input_0_cap1.txt'

# Create an instance of GameScoreCalculator
calculator = GameScoreCalculator(playing_a_game)

# Calculate the total score
total_score = calculator.calculate_score()

# Print the total score
print(f"Total score: {total_score}")