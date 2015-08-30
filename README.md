# Press
RSS Searcher 
-cd into director 'press'
- run ' python manage.py syncdb'
-- create superuser
--- (yes)
--- username: any
--- email: any
--- password: any
- run ' python manage.py migrate'
- run ' python manage.py runserver'
- open browser to this link 'http://127.0.0.1:8000/rss/'