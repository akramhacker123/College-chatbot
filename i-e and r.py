import json
import random
import json

# Load entity file
with open('entities.json', 'r', encoding='utf-8') as file:
    entities_data = json.load(file)

# Load response JSON file
with open('responses.json', 'r', encoding='utf-8') as file:
    responses_data = json.load(file)

# Rest of the code...

# Load entity file
import nltk

with open('entities.json') as file:
    entities_data = json.load(file)

# Load response JSON file
with open('responses.json') as file:
    responses_data = json.load(file)

# User's question
question = "Q and A.csv"

# Tokenize the question
tokens = nltk.word_tokenize(question)

# Initialize variables
matched_category = None
response_key = None
response_message = None

# Search for the matched category in the entity file
for entity in entities_data['entities.json']:
    if any(word.lower() in tokens for word in entity['words']):
        match_count = sum(word.lower() in tokens for word in entity['words'])

        if not matched_category or match_count > matched_category['match_count']:
            matched_category = {
                'category': entity['responseKeyword'],
                'match_count': match_count
            }

# Retrieve response message from response JSON
if matched_category:
    response_key = matched_category['category']

    if response_key in responses_data['responses']:
        response_messages = responses_data['responses'][response_key]
        response_message = random.choice(response_messages)

print("Matched Category:", matched_category)
print("Response Key:", response_key)
print("Response Message:", response_message)
