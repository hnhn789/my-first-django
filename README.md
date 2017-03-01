# mysite

## Getting Started

Make sure you are using a virtual environment of some sort (e.g. `virtualenv` or
`pyenv`).

```
pip install -r requirements.txt
./manage.py migrate
./manage.py loaddata sites
./manage.py runserver
```



# To Save Backend Data
python manage.py dumpdata --exclude=auth --exclude=contenttypes -o fixtures/outputs.json


# Before Deploying
Change the DATABASE NAME variable in "mysite/settings.py"
