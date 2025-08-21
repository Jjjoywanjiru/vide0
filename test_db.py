import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

print("Testing connection with:", DATABASE_URL)

try:
    connection = psycopg2.connect(DATABASE_URL)
    print("✅ Database connection successful!")
    
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    print("PostgreSQL version:", version[0])
    
    cursor.close()
    connection.close()
    
except Exception as e:
    print("❌ Connection failed:", e)
    print("\nTroubleshooting tips:")
    print("1. Check if your Supabase project is active")
    print("2. Verify your password is correct")
    print("3. Try the direct connection format")