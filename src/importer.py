import csv
import glob
import os
import sqlite3
import hashlib
from decimal import Decimal
from db import get_db, init_db

def clean_float(val):
    if val is None or val == '':
        return None
    val = str(val).replace(',', '')
    try:
        return float(val)
    except ValueError:
        return None

def import_csvs():
    init_db()
    conn = get_db()
    cursor = conn.cursor()
    
    csv_dir = r"e:\CODEX\Cytotax\Transactions"
    files = glob.glob(os.path.join(csv_dir, "*.csv"))
    
    total_rows = 0
    seen_file_hashes = set()
    
    for f in sorted(files):
        # Deduplicate identical files
        with open(f, 'rb') as f_bin:
            f_hash = hashlib.sha256(f_bin.read()).hexdigest()
        if f_hash in seen_file_hashes:
            print(f"Skipping duplicate file {f}")
            continue
        seen_file_hashes.add(f_hash)
        
        with open(f, 'r', encoding='utf-8-sig') as f_in:
            lines = f_in.readlines()
            if len(lines) < 3:
                continue
                
            reader = csv.DictReader(lines[2:])
            
            for row in reader:
                date = row.get('Date', '')
                type_ = row.get('Type', '')
                tag = row.get('Tag', '')
                sending_wallet = row.get('Sending Wallet', '')
                sent_amount = clean_float(row.get('Sent Amount', ''))
                sent_currency = row.get('Sent Currency', '')
                sent_cost_basis = clean_float(row.get('Sent Cost Basis', ''))
                receiving_wallet = row.get('Receiving Wallet', '')
                received_amount = clean_float(row.get('Received Amount', ''))
                received_currency = row.get('Received Currency', '')
                received_cost_basis = clean_float(row.get('Received Cost Basis', ''))
                fee_amount = clean_float(row.get('Fee Amount', ''))
                fee_currency = row.get('Fee Currency', '')
                gain_cad = clean_float(row.get('Gain (CAD)', ''))
                net_value_cad = clean_float(row.get('Net Value (CAD)', ''))
                fee_value_cad = clean_float(row.get('Fee Value (CAD)', ''))
                tx_src = row.get('TxSrc', '')
                tx_dest = row.get('TxDest', '')
                tx_hash = row.get('TxHash', '')
                description = row.get('Description', '')
                
                cursor.execute('''
                INSERT INTO transactions (
                    date, type, tag, sending_wallet, sent_amount, sent_currency, sent_cost_basis,
                    receiving_wallet, received_amount, received_currency, received_cost_basis,
                    fee_amount, fee_currency, gain_cad, net_value_cad, fee_value_cad,
                    tx_src, tx_dest, tx_hash, description
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    date, type_, tag, sending_wallet, sent_amount, sent_currency, sent_cost_basis,
                    receiving_wallet, received_amount, received_currency, received_cost_basis,
                    fee_amount, fee_currency, gain_cad, net_value_cad, fee_value_cad,
                    tx_src, tx_dest, tx_hash, description
                ))
                total_rows += 1

    conn.commit()
    conn.close()
    print(f"Imported {total_rows} rows.")

if __name__ == '__main__':
    import_csvs()
