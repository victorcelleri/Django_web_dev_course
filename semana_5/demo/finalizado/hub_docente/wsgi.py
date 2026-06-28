import os
import sys
from pathlib import Path
from dotenv import load_dotenv

path = Path(__file__).resolve().parent.parent
if str(path) not in sys.path:
    sys.path.insert(0, str(path))

load_dotenv(path / '.env')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hub_docente.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
