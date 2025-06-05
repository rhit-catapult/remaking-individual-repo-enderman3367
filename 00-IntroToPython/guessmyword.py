import random as rand
import nltk
from nltk.corpus import words

def get_word_list():
    """Get a list of words from NLTK, with fallback to manual list"""
    try:
        # Try to access the words corpus
        word_list = words.words()
        # Filter for words between 4-12 letters to make the game reasonable
        filtered_words = [word for word in word_list if 4 <= len(word) <= 12 and word.isalpha()]
        return filtered_words
    except LookupError:
        # If words corpus is not downloaded, try to download it
        print("Downloading word database... this may take a moment.")
        try:
            nltk.download('words', quiet=True)
            word_list = words.words()
            filtered_words = [word for word in word_list if 4 <= len(word) <= 12 and word.isalpha()]
            return filtered_words
        except Exception as e:
            print(f"Could not download NLTK words database: {e}")
            print("Using fallback word list...")
            # Fallback to original animal words if NLTK fails
            return [
                "jellyfish", "tiger", "snake", "horse",
                "fish", "lion", "emu", "cat", "dog", "penguin", "turtle",
                "elephant", "giraffe", "zebra", "monkey", "panda", "koala",
                "kangaroo", "whale", "dolphin", "octopus", "shark", "eagle",
                "falcon", "parrot", "owl", "rabbit", "fox", "wolf", "bear"
            ]
    except ImportError:
        print("NLTK not installed. Using fallback word list...")
        print("To install NLTK, run: pip install nltk")
        # Fallback if NLTK is not installed
        return [
            "jellyfish", "tiger", "snake", "horse",
            "fish", "lion", "emu", "cat", "dog", "penguin", "turtle",
            "elephant", "giraffe", "zebra", "monkey", "panda", "koala",
            "kangaroo", "whale", "dolphin", "octopus", "shark", "eagle",
            "falcon", "parrot", "owl", "rabbit", "fox", "wolf", "bear"
        ]

def main():
    
    # Get words from NLTK
    words_list = get_word_list()
    print(f"Loaded {len(words_list)} words from database")

    secret_word = rand.choice(words_list).upper()
    word_length = len(secret_word)
    
    # Initialize game state
    display_word = ["*"] * word_length  # Display word with asterisks
    guessed_letters = []  # Track all guessed letters
    wrong_guesses = []    # Track wrong guesses
    max_wrong_guesses = 14  # Traditional hangman limit
    
    print("hangman time")
    print("=" * 40)
    print(f"this word has {word_length} letters.")
    print(f"You have {max_wrong_guesses} wrong guesses allowed.")
    print()
    
    # Game loop
    while True:
        # Display current state
        print("Word: " + " ".join(display_word))
        print(f"Wrong guesses left: {max_wrong_guesses - len(wrong_guesses)}")
        
        if wrong_guesses:
            print(f"Wrong letters: {', '.join(wrong_guesses)}")
        
        if guessed_letters:
            print(f"All guessed letters: {', '.join(sorted(guessed_letters))}")
        
        print()
        
        # Check win condition
        if "*" not in display_word:
            print("you win")
            print(f"word was: {secret_word}")
            break
        
        # Check lose condition
        if len(wrong_guesses) >= max_wrong_guesses:
            print("loser")
            print(f"The word was: {secret_word}")
            break
        
        # Get user input
        try:
            guess = input("Guess a letter: ").upper().strip()
            
            # Validate input
            if len(guess) != 1:
                print("please enter exactly one letter")
                continue
            
            if not guess.isalpha():
                print("please enter a valid letter")
                continue
            
            if guess in guessed_letters:
                print("you already guessed that letter")
                continue
            
            # Process the guess
            guessed_letters.append(guess)
            
            if guess in secret_word:
                # Correct guess - reveal all instances of the letter
                for i, letter in enumerate(secret_word):
                    if letter == guess:
                        display_word[i] = letter
                
                print(f"'{guess}' is in the word.")
            else:
                # Wrong guess
                wrong_guesses.append(guess)
                print(f"'{guess}' is not in the word.")
            
            print("-" * 40)
            
        except KeyboardInterrupt:
            print("\n\nthanks for playing")
            break
        except EOFError:
            print("\n\nthanks for playing")
            break

main()
