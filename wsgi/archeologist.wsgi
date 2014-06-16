import os
import sys
# need both the surveys site directory
myPath      = '/www/archeologistRoot'
if myPath not in sys.path:
    sys.path.append(myPath)
# end if

# and the django application below
myPath      = '/www/archeologistRoot/archeologist'
if myPath not in sys.path:
    sys.path.append(myPath)
# end if

os.environ['DJANGO_SETTINGS_MODULE']    = 'archeologist.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
