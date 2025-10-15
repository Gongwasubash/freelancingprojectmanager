import gspread
from google.oauth2.service_account import Credentials
from django.conf import settings
import os
from datetime import datetime

class GoogleSheetsService:
    def __init__(self):
        self.sheet_id = os.getenv('GOOGLE_SHEET_ID')
        self.credentials_file = os.getenv('GOOGLE_CREDENTIALS_FILE', 'credentials.json')
        self.client = None
        self.workbook = None
        self.sheet = None
        
        # Handle relative paths by making them absolute
        if not os.path.isabs(self.credentials_file):
            self.credentials_file = os.path.join(os.getcwd(), self.credentials_file)
        
    def authenticate(self):
        """Authenticate with Google Sheets API"""
        try:
            scope = ['https://spreadsheets.google.com/feeds',
                    'https://www.googleapis.com/auth/drive']
            
            # Check for environment variable first (for production)
            credentials_json = os.getenv('GOOGLE_CREDENTIALS_JSON')
            if credentials_json:
                import json
                try:
                    creds_dict = json.loads(credentials_json)
                    creds = Credentials.from_service_account_info(creds_dict, scopes=scope)
                    self.client = gspread.authorize(creds)
                    self.workbook = self.client.open_by_key(self.sheet_id)
                    self.sheet = self.workbook.worksheet('Orders')
                    print("✅ Successfully connected using environment credentials")
                    return True
                except json.JSONDecodeError as e:
                    print(f"❌ Invalid JSON in GOOGLE_CREDENTIALS_JSON: {e}")
                    return False
            elif os.path.exists(self.credentials_file):
                creds = Credentials.from_service_account_file(self.credentials_file, scopes=scope)
                self.client = gspread.authorize(creds)
                self.workbook = self.client.open_by_key(self.sheet_id)
                self.sheet = self.workbook.worksheet('Orders')
                print(f"✅ Successfully connected using file: {self.credentials_file}")
                return True
            else:
                print("❌ No credentials found, using sample data")
                return False
        except Exception as e:
            print(f"❌ Authentication error: {str(e)}")
            return False
    
    def get_all_data(self):
        """Fetch all data from the Google Sheet"""
        if not self.client and not self.authenticate():
            return []
        
        try:
            records = self.sheet.get_all_records()
            return records
        except Exception as e:
            print(f"Error fetching data: {e}")
            return []
    
    def get_dashboard_data(self):
        """Process data for dashboard display"""
        raw_data = self.get_all_data()
        if not raw_data:
            print("No data from Google Sheets, using sample data")
            return self._get_sample_data()
        
        processed_data = []
        for row in raw_data:
            try:
                # Map all possible Orders sheet columns to dashboard format
                client_name = (row.get('Customer Name', '') or row.get('Client Name', '') or 
                              row.get('Client', '') or row.get('Name', '') or 'Customer')
                
                order_id = (row.get('Order ID', '') or row.get('Order Number', '') or 
                           row.get('Project', '') or row.get('ID', '') or 'Order')
                
                total_amount = (row.get('Total Amount', 0) or row.get('Amount', 0) or 
                               row.get('Price', 0) or row.get('Cost', 0) or 0)
                
                order_status = (row.get('Order Status', '') or row.get('Status', '') or 
                               row.get('State', '') or 'Pending')
                
                order_date = (row.get('Order Date', '') or row.get('Date', '') or 
                             row.get('Start Date', '') or row.get('Created', '') or '2024-01-01')
                
                delivery_date = (row.get('Delivery Date', '') or row.get('Due Date', '') or 
                                row.get('Deadline', '') or row.get('Expected Date', '') or '')
                
                service_type = (row.get('Service Type', '') or row.get('Service', '') or 
                               row.get('Product', '') or row.get('Description', '') or 'Service')
                
                email = (row.get('Email', '') or row.get('Customer Email', '') or 
                        row.get('Contact Email', '') or row.get('E-mail', '') or '')
                
                # Get contact and handle all possible variations
                contact_raw = (row.get('Contact', '') or row.get('contact', '') or 
                              row.get('Phone', '') or row.get('phone', '') or 
                              row.get('Mobile', '') or row.get('mobile', '') or 
                              row.get('Contact Number', '') or row.get('Phone Number', '') or 
                              row.get('Cell', '') or row.get('Number', '') or '')
                
                # Convert to string and handle numeric values
                contact = str(int(contact_raw)) if isinstance(contact_raw, (int, float)) and contact_raw != 0 else str(contact_raw) if contact_raw else ''
                
                # Keep original NPR values
                amount_npr = float(total_amount) if total_amount else 0
                
                # Map your data to dashboard format
                processed_data.append({
                    'client': client_name or 'Customer',
                    'project': order_id or service_type,
                    'amount': amount_npr,
                    'status': self._map_order_status(order_status),
                    'deadline': delivery_date or self._calculate_deadline('7 days'),
                    'start_date': order_date or '2024-01-01',
                    'description': service_type or 'Order',
                    'email': email,
                    'contact': contact,
                })
            except (ValueError, TypeError) as e:
                print(f"Error processing row: {e}")
                continue
        
        # If no processed data, return sample data
        if not processed_data:
            print("No processed data, using sample data")
            return self._get_sample_data()
            
        return processed_data
    
    def _map_order_status(self, original_status):
        """Map order status to dashboard status"""
        status_mapping = {
            'Pending': 'Pending',
            'Processing': 'Ongoing',
            'In Progress': 'Ongoing',
            'Completed': 'Completed',
            'Delivered': 'Completed',
            'Cancelled': 'Pending',
            'Shipped': 'Ongoing'
        }
        return status_mapping.get(original_status, 'Pending')
    
    def _calculate_deadline(self, delivery_time):
        """Calculate deadline based on delivery time"""
        from datetime import datetime, timedelta
        
        try:
            if 'day' in delivery_time.lower():
                days = int(''.join(filter(str.isdigit, delivery_time)))
                deadline = datetime.now() + timedelta(days=days)
                return deadline.strftime('%Y-%m-%d')
            elif 'same day' in delivery_time.lower():
                return datetime.now().strftime('%Y-%m-%d')
            else:
                return (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
        except:
            return (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
    
    def _get_sample_data(self):
        """Return sample data when Google Sheets is not available"""
        return [
            {'client': 'ABC Corp', 'project': 'Website Redesign', 'amount': 5000, 'status': 'Completed', 'deadline': '2024-01-15', 'start_date': '2023-12-01', 'description': 'Complete website overhaul', 'email': 'abc@corp.com', 'contact': '9841234567'},
            {'client': 'XYZ Ltd', 'project': 'Mobile App', 'amount': 8000, 'status': 'Ongoing', 'deadline': '2024-02-28', 'start_date': '2024-01-01', 'description': 'iOS and Android app development', 'email': 'xyz@ltd.com', 'contact': '9851234567'},
            {'client': 'Tech Startup', 'project': 'API Development', 'amount': 3000, 'status': 'Pending', 'deadline': '2024-01-30', 'start_date': '2024-01-15', 'description': 'REST API for mobile app', 'email': 'tech@startup.com', 'contact': '9861234567'},
            {'client': 'E-commerce Co', 'project': 'Database Optimization', 'amount': 2500, 'status': 'Completed', 'deadline': '2023-12-20', 'start_date': '2023-12-01', 'description': 'Performance improvements', 'email': 'ecom@co.com', 'contact': '9871234567'},
            {'client': 'Marketing Agency', 'project': 'Analytics Dashboard', 'amount': 4500, 'status': 'Ongoing', 'deadline': '2024-02-15', 'start_date': '2024-01-10', 'description': 'Custom analytics solution', 'email': 'marketing@agency.com', 'contact': '9881234567'},
        ]