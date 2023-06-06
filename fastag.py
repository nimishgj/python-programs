import sqlite3

# Connect to the database
conn = sqlite3.connect("fastag.db")
cursor = conn.cursor()

# Create the table for storing Fastag account information
cursor.execute("""
CREATE TABLE IF NOT EXISTS fastag (
    vehicle_number TEXT PRIMARY KEY,
    balance REAL NOT NULL
)
""")
conn.commit()

# Recharge a Fastag account
def recharge(vehicle_number, amount):
    cursor.execute("""
    UPDATE fastag
    SET balance = balance + ?
    WHERE vehicle_number = ?
    """, (amount, vehicle_number))
    conn.commit()

# Deduct a toll charge from a Fastag account
def deduct_toll_charge(vehicle_number, toll_charge):
    cursor.execute("""
    UPDATE fastag
    SET balance = balance - ?
    WHERE vehicle_number = ? AND balance >= ?
    """, (toll_charge, vehicle_number, toll_charge))
    if cursor.rowcount == 0:
        print("Insufficient balance in Fastag account for vehicle number {}".format(vehicle_number))
    conn.commit()

# Get the balance for a Fastag account
def get_balance(vehicle_number):
    cursor.execute("""
    SELECT balance
    FROM fastag
    WHERE vehicle_number = ?
    """, (vehicle_number,))
    result = cursor.fetchone()
    if result is None:
        print("No Fastag account found for vehicle number {}".format(vehicle_number))
        return None
    return result[0]