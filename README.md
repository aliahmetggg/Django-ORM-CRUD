# Django-ORM-CRUD
Making basic create read update delete operations on Django without any SQL code (ORM)

First you should create a virtual environment that include:
asgiref==3.5.0
backports.zoneinfo==0.2.1
Django==4.0.4
sqlparse==0.4.2

File struct should be:
->djangogo
  ->bookcrud
  ->venv
  
Then activate virtual environment with:
source venv/bin/activate

For the run CRUD operations first go into bookcrud with:
cd bookcrud/

***You must change values that inside crud files to make changes
You can run 
python manage.py shell  < read.py
because there is no need to change values

Run files that you want with:
python manage.py shell  < create.py
python manage.py shell  < read.py
python manage.py shell  < update.py
python manage.py shell  < delete.py

For the set up virtual environment you can follow:
https://www.linode.com/docs/guides/create-a-python-virtualenv-on-ubuntu-18-04/
document


