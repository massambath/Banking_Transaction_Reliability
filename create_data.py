import mysql.connector
import random

db =  mysql.connector.connect(
    host='localhost',
    user='root',
    password='passer',
    database='djamo_db'
)

cur = db.cursor()

# 1 Création de 10000 users
print("Génération des utilisateurs.......")
for i in range(10000):
    cur.execute("INSERT INTO users (full_name) VALUES (%s)", (f"User_{i}",))
    u_id = cur.lastrowid
    cur.execute("INSERT INTO accounts (user_id, balance) VALUES (%s, %s)", (u_id, random.uniform(1000, 500000)))
db.commit()

#2 Génération de 1 000 000 de transactions
print("Génération d'un millions de transactions")
for batch in range(100):
    transactions = []
    for _ in range(10000):
        s , r = random.randint(1,10000), random.randint(1,10000)
        transactions.append((s,r,random.uniform(10,5000),'success','transfer'))

        cur.executemany(
            "INSERT INTO transactions (sender_account_id,receiver_account_id, amount, status,transaction_type) VALUES(%s,%s,%s,%s,%s)",
            transactions
        )
        db.commit()
        print(f"Progression: {batch+1}%")
print("Base de données prete pour les tests SRE !")