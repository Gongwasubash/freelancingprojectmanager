# Freelancing Dashboard

A professional Django web dashboard that reads data from Google Sheets to display freelancing project analytics, KPIs, and financial summaries.

## Features

- 📊 **Overview Dashboard**: KPIs, charts, and recent projects
- 📁 **Projects Management**: Searchable and filterable project list
- 💰 **Finance Summary**: Income tracking and pending payments
- ⚙️ **Settings**: Google Sheets API configuration
- 🔐 **Authentication**: Django user authentication
- 📱 **Responsive Design**: Works on desktop and mobile

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Google Sheets API Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable Google Sheets API
4. Create Service Account credentials
5. Download the JSON credentials file
6. Rename it to `credentials.json` and place in project root
7. Share your Google Sheet with the service account email (found in credentials.json)

### 3. Configure Environment Variables

Update the `.env` file with your Google Sheet ID:

```env
GOOGLE_SHEET_ID=1F2PLmOQC3J8G3K9j2Q6EH37hP7toKphSuCZN4jfVD7Q
GOOGLE_CREDENTIALS_FILE=credentials.json
```

### 4. Database Setup

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5. Run the Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` and login with your superuser credentials.

## Google Sheet Format

Your Google Sheet should have these columns:

- **Client**: Client name
- **Project**: Project name
- **Amount**: Project amount (numeric)
- **Status**: Project status (Completed, Ongoing, Pending)
- **Deadline**: Project deadline
- **Start Date**: Project start date
- **Description**: Project description

## Project Structure

```
freelancing-dashboard/
├── dashboard/                 # Main Django app
│   ├── views.py              # Dashboard views
│   ├── sheets_service.py     # Google Sheets integration
│   └── urls.py               # URL patterns
├── templates/                # HTML templates
│   ├── auth/                 # Authentication templates
│   └── dashboard/            # Dashboard templates
├── static/                   # Static files
│   ├── css/                  # Stylesheets
│   └── js/                   # JavaScript files
├── .env                      # Environment variables
├── credentials.json          # Google API credentials
└── requirements.txt          # Python dependencies
```

## Usage

1. **Login**: Use Django superuser credentials
2. **Overview**: View KPIs and charts on the main dashboard
3. **Projects**: Browse, search, and filter projects
4. **Finance**: Track income and pending payments
5. **Settings**: Configure Google Sheets API
6. **Refresh**: Click refresh button to sync latest data

## Features in Detail

### Dashboard Overview
- Total earnings from completed projects
- Active project count
- Pending payment amounts
- Completed project count
- Monthly income trend chart
- Project status distribution pie chart

### Projects List
- Search by client or project name
- Filter by status (All, Ongoing, Completed, Pending)
- Sortable table with all project details
- Status badges with color coding

### Finance Summary
- Total income calculation
- Pending dues tracking
- Monthly income breakdown chart
- Separate tables for paid and pending projects

### Settings
- Google Sheets API configuration
- Connection testing
- System status display
- Data export functionality

## Troubleshooting

### Google Sheets API Issues
- Ensure credentials.json is properly configured
- Verify the service account email has access to your sheet
- Check that the Google Sheets API is enabled in your project

### Sample Data
If Google Sheets is not configured, the dashboard will display sample data for demonstration purposes.

## Security Notes

- Keep `credentials.json` secure and never commit it to version control
- Use environment variables for sensitive configuration
- Ensure proper authentication is enabled in production

## License

This project is for educational and personal use.