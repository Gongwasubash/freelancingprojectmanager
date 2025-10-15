import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'freelance_dashboard.settings')
django.setup()

from django.contrib.auth.models import User

user = User.objects.get(username='admin')
user.set_password('admin123')
user.save()
print('Password reset successfully')
print('Username: admin')
print('Password: admin123')