import os
import time
import random
from mnemonic import Mnemonic
from colorama import init, Fore, Style

# Initialize colorama
init()

def generate_seed_phrase(num_words):
    mnemo = Mnemonic("english")
    return mnemo.generate(strength=128 if num_words == 12 else 256)

def main():
    # Simulated startup messages with different colors
    print(Fore.RED + "Establishing the Environment...")
    time.sleep(1)
    print(Fore.YELLOW + "Software Name: Mnemonic Generator")
    print(Fore.GREEN + "Software Developed by - Pikai")
    print(Fore.GREEN + "Mnemonic Standard: BIP-39")
    input(Style.RESET_ALL + "Press Enter to Start")

    # User input for number of phrases to generate
    num_phrases = int(input("How many phrases do you want to generate? "))
    
    # User input for phrase length
    while True:
        phrase_length = int(input("Mnemonic Phrase Length (12 or 24): "))
        if phrase_length in [12, 24]:
            break
        else:
            print("Invalid input. Please enter either 12 or 24.")

    # Generating seed phrases
    print("\nGenerating Seed Phrases...")
    seed_phrases = []
    for _ in range(num_phrases):
        seed_phrase = generate_seed_phrase(phrase_length)
        seed_phrases.append(seed_phrase)

    # Displaying seed phrases
    print("\nGenerated Seed Phrases:")
    for phrase in seed_phrases:
        print(Style.RESET_ALL + phrase)

    # Saving seed phrases to a text file
    save_to_file = input("\nDo you want to save these phrases to a text file? (yes/no): ")
    if save_to_file.lower().strip() == 'yes':
        filename = input("Enter the file name to save (e.g., seed_phrases.txt): ")
        if not filename.endswith(".txt"):
            filename += ".txt"
        with open(filename, 'w', encoding='utf-8') as f:
            for phrase in seed_phrases:
                f.write(phrase + '\n')
        print(Fore.MAGENTA + f"Seed phrases saved to {filename}")

if __name__ == "__main__":
    main()
