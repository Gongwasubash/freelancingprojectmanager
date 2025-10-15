#!/usr/bin/env python3
"""
Check Google Credentials
Extract service account email from credentials file
"""

import json
import os

def check_credentials():
    """Check credentials file and extract service account email"""
    credentials_file = r"C:\Users\acer\Downloads\sigma-kayak-474813-f6-bea8569b294f.json"
    
    print("Google Sheets Setup Information")
    print("=" * 40)
    
    if os.path.exists(credentials_file):
        try:
            with open(credentials_file, 'r') as f:
                creds = json.load(f)
            
            print(f"Credentials file found")
            print(f"Project ID: {creds.get('project_id', 'N/A')}")
            print(f"Service Account Email: {creds.get('client_email', 'N/A')}")
            print()
            print("NEXT STEPS:")
            print("1. Copy the service account email above")
            print("2. Open your Google Sheet:")
            print("   https://docs.google.com/spreadsheets/d/1F2PLmOQC3J8G3K9j2Q6EH37hP7toKphSuCZN4jfVD7Q/edit")
            print("3. Click 'Share' button")
            print("4. Paste the service account email")
            print("5. Give it 'Editor' permissions")
            print("6. Click 'Send'")
            print()
            print("After sharing, the dashboard will automatically connect to live data!")
            
        except Exception as e:
            print(f"Error reading credentials: {e}")
    else:
        print(f"Credentials file not found at: {credentials_file}")

if __name__ == "__main__":
    check_credentials()