import csv
import os
import sqlite3
from acb import process_transactions

def generate_schedule3_csv(year_filter='2024 P1', output_path='schedule3_report.csv'):
    yearly = process_transactions()
    data = yearly.get(year_filter, {'Proceeds': 0.0, 'ACB': 0.0, 'Gain': 0.0, 'Income': 0.0})
    
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Period / Year', 'Line Description', 'Proceeds of Disposition (CAD)', 'Adjusted Cost Base (CAD)', 'Outlays/Expenses (CAD)', 'Realized Capital Gain / Loss (CAD)'])
        
        proceeds = data['Proceeds']
        acb = data['ACB']
        gain = data['Gain']
        
        writer.writerow([
            year_filter,
            'Crypto-assets & Cryptocurrencies (Schedule 3 Line 15200 / 15301)',
            f"{proceeds:.2f}",
            f"{acb:.2f}",
            "0.00",
            f"{gain:.2f}"
        ])
        
    print(f"Schedule 3 report exported to {output_path}")
    return data

if __name__ == '__main__':
    generate_schedule3_csv('2024 P1', 'schedule3_2024_P1.csv')
    generate_schedule3_csv('2024 P2', 'schedule3_2024_P2.csv')
    generate_schedule3_csv('2025', 'schedule3_2025.csv')
