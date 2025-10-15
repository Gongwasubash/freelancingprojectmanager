import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'freelance_dashboard.settings')
django.setup()

from django.contrib.auth.models import User
User.objects.all().delete()
user = User.objects.create_user('admin', 'admin@test.com', 'admin123')
user.is_staff = True
user.is_superuser = True
user.save()
print('User created: admin/admin123')