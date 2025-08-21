import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

# Try BOTH options to see which works:

# OPTION 1: Direct Connection
direct_url = "postgresql://postgres:TungtungtungtungSahur2025@db.egvdtkayqkgaycryqirc.supabase.co:5432/postgres"

# OPTION 2: Pooler Connection  
pooler_url = "postgresql://postgres.egvdtkayqkgaycryqirc:TungtungtungtungSahur2025@aws-0-us-east-2.pooler.supabase.com:6543/postgres"

print("Testing DIRECT connection...")
try:
    conn = psycopg2.connect(direct_url)
    print("✅ DIRECT CONNECTION WORKS!")
    conn.close()
except Exception as e:
    print(f"❌ Direct failed: {e}")

print("\nTesting POOLER connection...")
try:
    conn = psycopg2.connect(pooler_url)
    print("✅ POOLER CONNECTION WORKS!")
    conn.close()  
except Exception as e:
    print(f"❌ Pooler failed: {e}")