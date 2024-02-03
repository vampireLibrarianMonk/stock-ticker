#!/bin/bash
# Apply Django migrations
echo "Applying Django migrations..."
micromamba run -n $(head -1 /home/user/stock-ticker/environment.yml | cut -d' ' -f2) /home/user/stock-ticker/stocks/manage.py migrate

# Start the Django development server
echo "Starting Django development server..."
micromamba run -n $(head -1 /home/user/stock-ticker/environment.yml | cut -d' ' -f2) /home/user/stock-ticker/stocks/manage.py runserver 0.0.0.0:8000
