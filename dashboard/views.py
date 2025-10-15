from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from .sheets_service import GoogleSheetsService
from collections import Counter
from datetime import datetime, timedelta

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'auth/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    sheets_service = GoogleSheetsService()
    projects = sheets_service.get_dashboard_data()
    
    # Ensure we have data
    if not projects:
        projects = sheets_service._get_sample_data()
    
    print(f"Dashboard: Found {len(projects)} projects")
    for p in projects[:2]:  # Debug first 2 projects
        print(f"Project: {p}")
    
    total_earnings = sum(p['amount'] for p in projects if p['status'] == 'Completed')
    active_projects = len([p for p in projects if p['status'] == 'Ongoing'])
    pending_payments = sum(p['amount'] for p in projects if p['status'] == 'Pending')
    completed_projects = len([p for p in projects if p['status'] == 'Completed'])
    
    status_counts = Counter(p['status'] for p in projects)
    
    print(f"KPIs: Earnings={total_earnings}, Active={active_projects}, Pending={pending_payments}, Completed={completed_projects}")
    print(f"Status counts: {dict(status_counts)}")
    
    monthly_income = {}
    for i in range(6):
        month = (datetime.now() - timedelta(days=30*i)).strftime('%Y-%m')
        monthly_income[month] = sum(p['amount'] for p in projects if p['status'] == 'Completed')
    
    context = {
        'total_earnings': total_earnings,
        'active_projects': active_projects,
        'pending_payments': pending_payments,
        'completed_projects': completed_projects,
        'projects': projects,
        'status_counts': dict(status_counts),
        'monthly_income': monthly_income,
    }
    return render(request, 'dashboard/overview.html', context)

def projects_list(request):
    sheets_service = GoogleSheetsService()
    projects = sheets_service.get_dashboard_data()
    
    # Ensure we have data
    if not projects:
        projects = sheets_service._get_sample_data()
    
    status_filter = request.GET.get('status')
    if status_filter:
        projects = [p for p in projects if p['status'] == status_filter]
    
    search = request.GET.get('search')
    if search:
        projects = [p for p in projects if search.lower() in p['client'].lower() or search.lower() in p['project'].lower()]
    
    return render(request, 'dashboard/projects.html', {'projects': projects})

def finance_summary(request):
    sheets_service = GoogleSheetsService()
    projects = sheets_service.get_dashboard_data()
    
    # Ensure we have data
    if not projects:
        projects = sheets_service._get_sample_data()
    
    monthly_data = {}
    for project in projects:
        if project['status'] == 'Completed':
            month = datetime.now().strftime('%Y-%m')
            monthly_data[month] = monthly_data.get(month, 0) + project['amount']
    
    total_income = sum(p['amount'] for p in projects if p['status'] == 'Completed')
    pending_dues = sum(p['amount'] for p in projects if p['status'] == 'Pending')
    
    context = {
        'total_income': total_income,
        'pending_dues': pending_dues,
        'monthly_data': monthly_data,
        'projects': projects,
    }
    return render(request, 'dashboard/finance.html', context)

def settings_view(request):
    return render(request, 'dashboard/settings.html')

def refresh_data(request):
    sheets_service = GoogleSheetsService()
    projects = sheets_service.get_dashboard_data()
    return JsonResponse({'status': 'success', 'count': len(projects)})