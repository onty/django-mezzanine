from __future__ import unicode_literals

import os

#PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
#ettings_module = "%s.settings" % PROJECT_ROOT.split(os.sep)[-1]
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)
os.environ.setdefault("DJANGO_SETTINGS_MODULE","settings")


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
