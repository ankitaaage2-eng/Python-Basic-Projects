# Q9: Unique words + math module
import math

def unique_words_program():
    try:
        sentence = input("Enter a sentence: ")
        
        if not sentence.strip():
            print("Empty sentence entered!")
            return
        
        # Sentence la words madhe split kar ani set madhe tak
        words = sentence.lower().split()
        unique_words = set(words)
        
        # Sorted order madhe print kar
        sorted_unique = sorted(unique_words)
        print(f"\nUnique Words (Sorted): {sorted_unique}")
        
        # Count cha square
        count = len(unique_words)
        power_result = math.pow(count, 2)
        print(f"Total Unique Words: {count}")
        print(f"Count raised to power 2: {int(power_result)}")
        
    except Exception as e:
        print(f"Error: {e}")

unique_words_program()