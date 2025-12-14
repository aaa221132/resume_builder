@echo off
echo Creating superuser...

python manage.py shell -c "from django.contrib.auth.models import User; User.objects.filter(username='admin').delete(); User.objects.create_superuser('admin', 'admin@example.com', '12345')"

echo Superuser created:
echo login: admin
echo password: 12345

pause
