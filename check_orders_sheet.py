import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'freelance_dashboard.settings')
django.setup()

from dashboard.sheets_service import GoogleSheetsService

def check_orders_sheet():
    service = GoogleSheetsService()
    
    if service.authenticate():
        print("Connected to Orders sheet successfully!")
        
        raw_data = service.get_all_data()
        print(f"\nFound {len(raw_data)} rows in Orders sheet")
        
        if raw_data:
            print("\nColumn headers found:")
            for key in raw_data[0].keys():
                print(f"  - {key}")
            
            print(f"\nFirst 3 rows of data:")
            for i, row in enumerate(raw_data[:3]):
                print(f"\nRow {i+1}:")
                for key, value in row.items():
                    print(f"  {key}: {value}")
        else:
            print("No data found in Orders sheet")
    else:
        print("Failed to connect to Orders sheet")

if __name__ == "__main__":
    check_orders_sheet()