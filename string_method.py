from DistUpgrade.utils import capitalize_first_word

sentence = "The quick brown fox jumps over the lazy dog"

# Count how many characters in the sentence - .len()
print(f'you have {len(sentence) } characters in the sentence.')

# Find first space in the sentence - .find()
print(f'The first space in the sentence is at character {sentence.find(" ") }')

# help capitalize and upper and lower - .capitalize(), .upper(), .lower()
print(f'The capitalized sentence is {capitalize_first_word(sentence)}')

# still need upper and lower