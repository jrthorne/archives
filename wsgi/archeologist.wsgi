import os
import sys
import site

# Add the site-packages of the chosen virualenv to work with
site.addsitedir('/home/jason/.virtualenvs/archeologist/lib/python2.7/site-packages')

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

# activate your virtual env
activate_env=os.path.expanduser("/home/jason/.virtualenvs/archeologist/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
