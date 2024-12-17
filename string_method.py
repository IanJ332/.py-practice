from DistUpgrade.utils import capitalize_first_word
from orca.messages import charactersTooLong

sentence = "the quick brown fox jumps over the lazy dog"

# Count how many characters in the sentence - .len()
# print(f'you have {len(sentence) } characters in the sentence.')

# Find first space in the sentence - .find()
# print(f'The first space in the sentence is at character {sentence.find(" ") }')

# help capitalize and upper and lower - .capitalize(), .upper(), .lower()
# .capitalize() help capitalize first characters
# print(f'The capitalized sentence is : "{capitalize_first_word(sentence)}".')

# .upper() help upper every characters
# print(f'The upper sentence is : "{sentence.upper()}".')

# .lower() help lower every characters
# print(f'The lower sentence is : "{sentence.lower()}".')

# Count
# print(f'There are {sentence.lower().count("a")} a in your sentence.')