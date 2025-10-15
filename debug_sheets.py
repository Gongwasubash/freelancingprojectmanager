#!/usr/bin/env python3
"""
Debug Google Sheets Data
Check what data we're actually getting from the sheet
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'freelance_dashboard.settings')
django.setup()

from dashboard.sheets_service import GoogleSheetsService

def debug_sheets():
    """Debug what data we're getting from Google Sheets"""
    print("Debugging Google Sheets Data")
    print("=" * 40)
    
    service = GoogleSheetsService()
    
    if service.authenticate():
        print("Connected to Google Sheets successfully!")
        
        # Get raw data
        raw_data = service.get_all_data()
        print(f"\nRaw data from sheet ({len(raw_data)} rows):")
        
        for i, row in enumerate(raw_data[:10]):  # Show first 10 rows
            print(f"Row {i+1}: {row}")
        
        # Get processed data
        processed_data = service.get_dashboard_data()
        print(f"\nProcessed data ({len(processed_data)} records):")
        
        for i, record in enumerate(processed_data[:5]):  # Show first 5 records
            print(f"Record {i+1}:")
            for key, value in record.items():
                print(f"  {key}: {value}")
            print()
    else:
        print("Failed to connect to Google Sheets")

if __name__ == "__main__":
    debug_sheets()