# Render Deployment Guide

## 🚀 Quick Deploy Steps

### 1. Push to GitHub
```bash
git init
git add .
git commit -m "Initial deployment"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/freelancing-dashboard.git
git push -u origin main
```

### 2. Create Render Service
1. Go to [render.com](https://render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Use these settings:
   - **Name**: freelancing-dashboard
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn freelance_dashboard.wsgi:application --bind 0.0.0.0:$PORT`

### 3. Environment Variables
Add these in Render dashboard:

| Key | Value |
|-----|-------|
| `DEBUG` | `False` |
| `SECRET_KEY` | (auto-generated) |
| `GOOGLE_SHEET_ID` | `1F2PLmOQC3J8G3K9j2Q6EH37hP7toKphSuCZN4jfVD7Q` |
| `GOOGLE_CREDENTIALS_JSON` | (paste your credentials.json content) |

### 4. Default Login
- **Username**: `admin`
- **Password**: `admin123`

## 📋 Files Included
- ✅ `build.sh` - Build script with superuser creation
- ✅ `render.yaml` - Render configuration
- ✅ `requirements.txt` - Dependencies with production packages
- ✅ `.gitignore` - Excludes sensitive files
- ✅ Production settings with security configurations
- ✅ WhiteNoise for static files
- ✅ Authentication-protected views
- ✅ Chatbot with voice transcription
- ✅ Google Sheets integration

## 🔧 Troubleshooting
- Check Render logs if deployment fails
- Ensure GOOGLE_CREDENTIALS_JSON is valid JSON
- Verify Google Sheets API is enabled
- Share your sheet with service account email

Your dashboard will be live at: `https://your-app-name.onrender.com`