import json

# Load the JSON file
with open("synm.json", "r") as f:
    file = json.load(f)

# Extract keys from the JSON object and store them in a list
syn_key = [list(file[i].keys())[0] for i in range(len(file))]
t = []
for i in syn_key:
    if i.endswith('?'):
        t.append(i[:-1])
    else:
        t.append(i)

# Convert the keys to lowercase and store them in a new list
syn_key_lower = [i.lower() for i in syn_key]

# Loop through the lowercase keys and print them
for i in syn_key_lower:
    if i.endswith('?'):
        print(i[:-1])
    else:
        print(i)

# Perform further processing as needed
lt = []
for j in range(len(syn_key)):
    print(file[j][syn_key[j]])
    # if i in syns[j][t[j]]:
    #     lt.append(i)


