# Quick Start Guide

## Login Credentials
- **Username:** `admin`
- **Password:** `admin123`
- **URL:** `http://127.0.0.1:8000/login/`

## Start Server
1. Double-click `run_server.bat` OR
2. Open command prompt in this folder and run:
   ```
   python manage.py runserver 127.0.0.1:8000
   ```

## If Login Still Fails
Run this in command prompt:
```
python create_user.py
python manage.py runserver 127.0.0.1:8000
```

## Your Google Sheets Data
The dashboard is now connected to your Google Sheet and will show:
- Your design services as "projects"
- NPR prices converted to USD
- All services marked as "Pending" status
- Professional dashboard with charts and KPIs

## Service Account Email (for sharing)
`subash@sigma-kayak-474813-f6.iam.gserviceaccount.com`

Make sure this email has access to your Google Sheet for live data updates.