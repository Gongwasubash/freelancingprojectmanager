#!/usr/bin/env python3
"""
Test Google Sheets Connection
Quick script to verify Google Sheets API connectivity
"""

import os
import sys
import django
from pathlib import Path

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'freelance_dashboard.settings')
django.setup()

from dashboard.sheets_service import GoogleSheetsService

def test_connection():
    """Test Google Sheets connection"""
    print("Testing Google Sheets Connection")
    print("=" * 40)
    
    # Initialize service
    service = GoogleSheetsService()
    
    print(f"Sheet ID: {service.sheet_id}")
    print(f"Credentials File: {service.credentials_file}")
    print(f"File Exists: {os.path.exists(service.credentials_file)}")
    
    # Test authentication
    print("\nTesting authentication...")
    if service.authenticate():
        print("SUCCESS: Authentication successful!")
        
        # Test data retrieval
        print("\nTesting data retrieval...")
        data = service.get_dashboard_data()
        print(f"SUCCESS: Retrieved {len(data)} records")
        
        if data:
            print("\nSample data:")
            for i, record in enumerate(data[:3]):  # Show first 3 records
                print(f"  {i+1}. {record.get('client', 'N/A')} - {record.get('project', 'N/A')} - ${record.get('amount', 0)}")
        
        return True
    else:
        print("ERROR: Authentication failed!")
        print("The dashboard will use sample data.")
        return False

if __name__ == "__main__":
    test_connection()