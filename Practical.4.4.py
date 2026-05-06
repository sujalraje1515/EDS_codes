import pandas as pd
from itertools import combinations
from collections import Counter

# Prompt user to input the file name
file_name = input()

# Read data from the specified CSV file
df = pd.read_csv(file_name)

# write the code
df.columns = df.columns.str.strip()
df['Product'] = df['Product'].str.strip()
transaction = df.groupby('Date')["Product"].apply(list)
pair_counter = Counter()
for products in transaction:
	products.sort()
	pairs = list(combinations(products,2))
	pair_counter.update(pairs)

if pair_counter:
	max_freq = max(pair_counter.values())

	for pair, count in sorted(pair_counter.items()):
		if count == max_freq:
			print(f"{pair[0]} and {pair[1]}: {count} times")

# Output the most frequent product pairs