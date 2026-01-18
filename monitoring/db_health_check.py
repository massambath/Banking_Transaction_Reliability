import mysql.connector

def check_db():
    try:
        db = mysql.connector.connect(host="localhost", user="root", password="password", database="djamo_db")
        print("✅ Database is UP")
        # On pourrait ajouter un check sur le nombre de connexions actives ici
    except Exception as e:
        print(f"🚨 DATABASE DOWN: {e}")

if __name__ == "__main__":
    check_db()