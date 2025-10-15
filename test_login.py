import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'freelance_dashboard.settings')
django.setup()

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Test authentication
user = authenticate(username='admin', password='admin123')
if user:
    print('Authentication successful')
    print(f'User: {user.username}')
    print(f'Active: {user.is_active}')
    print(f'Staff: {user.is_staff}')
    print(f'Superuser: {user.is_superuser}')
else:
    print('Authentication failed')
    users = User.objects.all()
    print(f'Available users: {[u.username for u in users]}')