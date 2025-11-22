import sys
import os
from pathlib import Path

# Add your project directory to the Python path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
