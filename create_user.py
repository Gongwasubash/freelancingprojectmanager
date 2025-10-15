import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'freelance_dashboard.settings')
django.setup()

from django.contrib.auth.models import User

# Delete existing admin user
User.objects.filter(username='admin').delete()

# Create new admin user
user = User.objects.create_superuser('admin', 'admin@test.com', 'admin123')
print('New admin user created')
print('Username: admin')
print('Password: admin123')
print('Go to: http://127.0.0.1:8000/login/')