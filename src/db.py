import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'cytotax.db')

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    try:
        # Sentinel: Pre-create the file with strict permissions to prevent unauthorized access
        fd = os.open(DB_PATH, os.O_CREAT | os.O_EXCL | os.O_RDWR, 0o600)
        os.close(fd)
    except FileExistsError:
        # Sentinel: Fail securely to thwart TOCTOU race condition attacks
        raise RuntimeError("TOCTOU race condition detected: Database file was created between check and creation")
    
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        type TEXT,
        tag TEXT,
        sending_wallet TEXT,
        sent_amount REAL,
        sent_currency TEXT,
        sent_cost_basis REAL,
        receiving_wallet TEXT,
        received_amount REAL,
        received_currency TEXT,
        received_cost_basis REAL,
        fee_amount REAL,
        fee_currency TEXT,
        gain_cad REAL,
        net_value_cad REAL,
        fee_value_cad REAL,
        tx_src TEXT,
        tx_dest TEXT,
        tx_hash TEXT,
        description TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE acb_pools (
        currency TEXT PRIMARY KEY,
        quantity REAL,
        total_acb_cad REAL,
        unit_cost_cad REAL
    )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("Database initialized.")
