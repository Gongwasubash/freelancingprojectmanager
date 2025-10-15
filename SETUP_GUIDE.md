# 🚀 FreelancePro Dashboard - Complete Setup Guide

A professional Django web dashboard that reads data from Google Sheets to display freelancing project analytics, KPIs, and financial summaries with a modern, responsive design.

## ✨ Features

- 📊 **Professional Overview Dashboard**: KPIs with gradient cards, interactive charts
- 📁 **Advanced Projects Management**: Search, filter, and sort functionality
- 💰 **Financial Analytics**: Income tracking, pending payments, monthly breakdowns
- ⚙️ **Google Sheets Integration**: Live data sync from your spreadsheet
- 🔐 **Secure Authentication**: Django user authentication system
- 📱 **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- 🎨 **Modern UI**: Professional gradients, animations, and micro-interactions

## 🛠️ Quick Setup (Automated)

### Option 1: Run Setup Script
```bash
python setup.py
```

### Option 2: Manual Setup

#### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 2. Database Setup
```bash
python manage.py migrate
python manage.py createsuperuser
```

#### 3. Start the Server
```bash
python manage.py runserver
```

#### 4. Access Dashboard
Open your browser and go to: `http://127.0.0.1:8000`

**Default Login:**
- Username: `admin`
- Password: `admin123`

## 📊 Google Sheets Integration

### Step 1: Google Cloud Console Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Google Sheets API:
   - Go to "APIs & Services" > "Library"
   - Search for "Google Sheets API"
   - Click "Enable"

### Step 2: Create Service Account

1. Go to "APIs & Services" > "Credentials"
2. Click "Create Credentials" > "Service Account"
3. Fill in the service account details:
   - Name: `freelance-dashboard`
   - Description: `Service account for freelance dashboard`
4. Click "Create and Continue"
5. Skip role assignment (click "Continue")
6. Click "Done"

### Step 3: Generate Credentials

1. Click on the created service account
2. Go to the "Keys" tab
3. Click "Add Key" > "Create New Key"
4. Select "JSON" format
5. Click "Create" - this downloads your credentials file

### Step 4: Setup Credentials

1. Rename the downloaded file to `credentials.json`
2. Place it in your project root directory (same level as `manage.py`)
3. **Important**: Never commit this file to version control!

### Step 5: Share Your Google Sheet

1. Open your Google Sheet: [Your Sheet](https://docs.google.com/spreadsheets/d/1F2PLmOQC3J8G3K9j2Q6EH37hP7toKphSuCZN4jfVD7Q/edit)
2. Click the "Share" button
3. Add the service account email (found in `credentials.json` as `client_email`)
4. Give it "Editor" permissions
5. Click "Send"

## 📋 Google Sheet Format

Your Google Sheet should have these exact column headers in row 1:

| Column | Header | Description | Example |
|--------|--------|-------------|---------|
| A | Client | Client company name | "ABC Corp" |
| B | Project | Project name | "Website Redesign" |
| C | Amount | Project value (numbers only) | 5000 |
| D | Status | Project status | "Completed", "Ongoing", "Pending" |
| E | Deadline | Project deadline | "2024-02-15" |
| F | Start Date | Project start date | "2024-01-01" |
| G | Description | Project description | "Complete website overhaul" |

### Sample Data Row:
```
ABC Corp | Website Redesign | 5000 | Completed | 2024-02-15 | 2024-01-01 | Complete website overhaul
```

## 🎨 Dashboard Features

### Overview Page
- **KPI Cards**: Total earnings, active projects, pending payments, completed projects
- **Interactive Charts**: Monthly income trends, project status distribution
- **Recent Projects**: Quick view of latest projects with status indicators

### Projects Page
- **Advanced Search**: Search by client name or project title
- **Smart Filters**: Filter by status (All, Ongoing, Completed, Pending)
- **Sortable Table**: Click column headers to sort data
- **Status Indicators**: Visual status badges with color coding

### Finance Page
- **Income Analytics**: Total income, pending dues, net worth calculations
- **Monthly Breakdown**: Interactive bar chart showing monthly income
- **Payment Tracking**: Separate tables for paid and pending projects

### Settings Page
- **API Configuration**: Google Sheets API setup and testing
- **System Status**: Real-time connection status and data sync info
- **Data Export**: Export functionality for backup and analysis

## 🔧 Customization

### Changing Colors
Edit `static/css/dashboard.css` and modify the gradient variables:

```css
.bg-gradient-primary {
    background: linear-gradient(135deg, #your-color-1 0%, #your-color-2 100%);
}
```

### Adding New KPIs
1. Update the view in `dashboard/views.py`
2. Add the KPI card in the template
3. Style it in the CSS file

### Custom Charts
Modify the Chart.js configurations in the template files or add new charts using the enhanced `createChart()` function in `dashboard.js`.

## 🚀 Deployment

### For Production:

1. **Environment Variables**: Create a `.env` file with production settings
2. **Static Files**: Run `python manage.py collectstatic`
3. **Database**: Use PostgreSQL or MySQL instead of SQLite
4. **Security**: Update `SECRET_KEY` and set `DEBUG = False`
5. **HTTPS**: Enable SSL/TLS for secure connections

### Recommended Hosting:
- **Heroku**: Easy deployment with Git
- **DigitalOcean**: App Platform or Droplets
- **AWS**: Elastic Beanstalk or EC2
- **PythonAnywhere**: Simple Python hosting

## 🔒 Security Notes

- Keep `credentials.json` secure and never commit to version control
- Use environment variables for sensitive configuration
- Enable proper authentication in production
- Regularly update dependencies for security patches
- Use HTTPS in production environments

## 🐛 Troubleshooting

### Common Issues:

**1. Google Sheets API Not Working**
- Verify credentials.json is in the correct location
- Check that the service account email has access to your sheet
- Ensure Google Sheets API is enabled in your project

**2. Charts Not Displaying**
- Check browser console for JavaScript errors
- Ensure Chart.js is loading properly
- Verify data format in the template

**3. Styling Issues**
- Clear browser cache
- Check that CSS files are loading
- Verify Bootstrap and Font Awesome CDN links

**4. Database Errors**
- Run `python manage.py migrate` to apply migrations
- Check database permissions
- Verify Django settings configuration

### Getting Help:

1. Check the browser console for JavaScript errors
2. Review Django logs for backend issues
3. Verify Google Sheets API quotas and limits
4. Test with sample data first before connecting live sheets

## 📈 Performance Tips

- **Caching**: Implement Redis caching for frequently accessed data
- **Database**: Use database indexes for better query performance
- **Static Files**: Use a CDN for static file delivery
- **API Limits**: Implement rate limiting for Google Sheets API calls

## 🔄 Updates and Maintenance

- Regularly update Python packages: `pip install -r requirements.txt --upgrade`
- Monitor Google Sheets API usage and quotas
- Backup your database regularly
- Keep Django updated for security patches

## 📞 Support

For issues and questions:
1. Check this documentation first
2. Review the troubleshooting section
3. Check Django and Google Sheets API documentation
4. Test with sample data to isolate issues

---

**🎉 Congratulations!** You now have a professional freelancing dashboard that automatically syncs with your Google Sheets data. Enjoy tracking your projects and income with style!