import csv
import glob
import os

files = glob.glob(r"e:\CODEX\Cytotax\Transactions\*.csv")
print("Found files:", len(files))

rows = []
for f in files:
    with open(f, 'r', encoding='utf-8') as f_in:
        lines = f_in.readlines()
        # line 1 is title, line 2 is blank, line 3 is header
        if len(lines) > 2:
            reader = csv.DictReader(lines[2:])
            for r in reader:
                rows.append(r)

print("Total rows:", len(rows))

# Let's do a naive sum for 2020
proceeds_2020 = 0.0
for r in rows:
    if r['Date'].startswith('2020'):
        # Just summing Net Value CAD for Sent Crypto
        if r['Sent Currency'] and r['Sent Currency'] not in ('CAD', 'USD'): # assuming CAD/fiat are not crypto
            if r['Net Value (CAD)']:
                proceeds_2020 += float(r['Net Value (CAD)'])

print("Naive Proceeds 2020:", proceeds_2020)
