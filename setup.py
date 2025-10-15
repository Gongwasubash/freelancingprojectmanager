#!/usr/bin/env python3
"""
FreelancePro Dashboard Setup Script
Automates the initial setup process for the Django dashboard
"""

import os
import sys
import subprocess
import django
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"Running: {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"{description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"ERROR during {description}: {e}")
        print(f"Output: {e.output}")
        return False

def setup_django():
    """Setup Django environment"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'freelance_dashboard.settings')
    django.setup()

def create_superuser():
    """Create a superuser for the dashboard"""
    try:
        from django.contrib.auth.models import User
        
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@freelancepro.com', 'admin123')
            print("Superuser created successfully")
            print("   Username: admin")
            print("   Password: admin123")
            print("   Email: admin@freelancepro.com")
        else:
            print("INFO: Superuser already exists")
        return True
    except Exception as e:
        print(f"ERROR: Error creating superuser: {e}")
        return False

def check_credentials():
    """Check if Google Sheets credentials exist"""
    if os.path.exists('credentials.json'):
        print("Google Sheets credentials found")
        return True
    else:
        print("WARNING: Google Sheets credentials not found")
        print("   Please follow the setup instructions in README.md")
        print("   The dashboard will use sample data until configured")
        return False

def main():
    """Main setup function"""
    print("FreelancePro Dashboard Setup")
    print("=" * 50)
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("ERROR: Python 3.8 or higher is required")
        sys.exit(1)
    
    print(f"Python {sys.version.split()[0]} detected")
    
    # Install dependencies
    if not run_command("pip install -r requirements.txt", "Installing dependencies"):
        print("ERROR: Failed to install dependencies")
        sys.exit(1)
    
    # Run migrations
    if not run_command("python manage.py migrate", "Setting up database"):
        print("ERROR: Failed to setup database")
        sys.exit(1)
    
    # Setup Django and create superuser
    setup_django()
    if not create_superuser():
        print("ERROR: Failed to create superuser")
        sys.exit(1)
    
    # Check for Google Sheets credentials
    check_credentials()
    
    # Collect static files (if needed)
    run_command("python manage.py collectstatic --noinput", "Collecting static files")
    
    print("\n" + "=" * 50)
    print("Setup completed successfully!")
    print("\nNext steps:")
    print("1. Run: python manage.py runserver")
    print("2. Open: http://127.0.0.1:8000")
    print("3. Login with: admin / admin123")
    print("\nFor Google Sheets integration:")
    print("1. Follow the setup guide in README.md")
    print("2. Place credentials.json in the project root")
    print("3. Share your Google Sheet with the service account")
    print("\nYour Google Sheet URL:")
    print("https://docs.google.com/spreadsheets/d/1F2PLmOQC3J8G3K9j2Q6EH37hP7toKphSuCZN4jfVD7Q/edit")

if __name__ == "__main__":
    main()