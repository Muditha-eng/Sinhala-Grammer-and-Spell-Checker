import re
from typing import List, Tuple
from Levenshtein import distance as edit_distance

class SinhalaSpellChecker:
    def __init__(self, dictionary_path: str):
        self.dictionary = self._load_dictionary(dictionary_path)
    
    def _load_dictionary(self, path: str) -> set:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return set(word.strip() for word in f if word.strip())
        except FileNotFoundError:
            print(f"Error: Dictionary file '{path}' not found.")
            return set()
    
    def suggest_corrections(self, word: str, max_suggestions: int = 5) -> List[Tuple[str, float]]:
        if not self.dictionary:
            print("Error: Dictionary is empty. Please load a valid dictionary.")
            return []

        if word in self.dictionary:
            return [(word, 1.0)]
        
        suggestions = []
        for dict_word in self.dictionary:
            dist = edit_distance(word, dict_word)
            similarity = 1 - (dist / max(len(word), len(dict_word)))
            if similarity > 0.6:
                suggestions.append((dict_word, similarity))
        
        return sorted(suggestions, key=lambda x: x[1], reverse=True)[:max_suggestions]


if __name__ == "__main__":
    dictionary_path = "./data/sinhala_dictionary.txt"
    checker = SinhalaSpellChecker(dictionary_path)

    while True:
        user_input = input("\nEnter a single Sinhala word (or type 'exit' to quit): ").strip()
        
        if user_input.lower() == "exit":
            print("Exiting the Sinhala Spell Checker. Goodbye!")
            break

        if not re.match(r"^[\u0D80-\u0DFF]+$", user_input):
            print("Please enter a valid Sinhala word.")
            continue

        if user_input in checker.dictionary:
            print(f"'{user_input}' is correctly spelled.")
        else:
            suggestions = checker.suggest_corrections(user_input)
            if suggestions:
                print(f"Suggestions for '{user_input}':")
                for suggestion, score in suggestions:
                    print(f"  - {suggestion} (Similarity: {score:.2f})")
            else:
                print(f"No suggestions available for '{user_input}'.")
