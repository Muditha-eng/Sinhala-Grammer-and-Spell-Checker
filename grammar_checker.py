import json

# Embedded corrections data (from corrections.json)
corrections_data = {
    "මම": {
        "ගියෙමු": "ගියෙමි",
        "ගියහ": "ගියෙමි",
        "ගියෝය": "ගියෙමි",
        "කලේය": "කලෙමි",
        "කලෙමු": "කලෙමි",
        "කීවෝය": "කීවෙමි",
        "කීවේය": "කීවෙමි",
        "යමු": "යමි"
    },
    "අපි": {
        "ගියෙමි": "ගියෙමු",
        "ගියහ": "ගියෙමු",
        "කලේය": "කලෙමු",
        "කලෝය": "කලෙමු",
        "කීවෝය": "කීවෙමු",
        "යමි": "යමු"
    },
    "අක්කා,අම්මා": {
        "ගියෙමි": "ගියාය",
        "ගියහ": "ගියාය",
        "කලේය": "කලාය",
        "කීවෝය": "කීවාය"
    },
    "මල්ලී": {
        "ගියෙමි": "ගියේය",
        "ගියහ": "ගියේය",
        "කලේය": "කලේය",
        "කීවෝය": "කීවේය"
    }
}

# Embedded Sinhala dictionary (from sinhala_dictionary.txt)
sinhala_words = {
    "මම", "අපි", "අක්කා", "අම්මා", "අයියා", "මල්ලී", "ගියෙමි", "ගියෙමු", "ගියාය",
    "කලෙමි", "කලාය", "කලා", "කීවෙමි", "කීවාය", "යමු", "යමි"
}

def correct_sentence_with_rules(sentence, corrections_data):
    """
    Corrects Sinhala grammar errors in a given sentence based on subject-specific rules.
    """
    words = sentence.split()
    if not words:
        return sentence

    subject = words[0]
    corrections = {}
    for key, rules in corrections_data.items():
        if subject in key.split(","):
            corrections = rules
            break

    corrected_sentence = sentence
    for incorrect, correct in corrections.items():
        if incorrect in sentence:
            corrected_sentence = sentence.replace(incorrect, correct)
            break

    return corrected_sentence

def validate_words(sentence, sinhala_words):
    """
    Validate words in the sentence against the Sinhala dictionary.
    """
    words = sentence.split()
    unknown_words = [word for word in words if word not in sinhala_words]
    return unknown_words

# Input and processing loop
while True:
    sentence = input("Enter a Sinhala sentence to check (or type 'exit' to quit): ")
    if sentence.lower() == "exit":
        break

    # Correct the sentence
    corrected_sentence = correct_sentence_with_rules(sentence, corrections_data)
    print(f"Original: {sentence}")
    print(f"Corrected: {corrected_sentence}")

    # Validate words
    unknown_words = validate_words(sentence, sinhala_words)
