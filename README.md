# XML TO CSV CONVERTER

Episode metadata that is provided by studios as one XML for one episode is not a preferred data format when scheduling a season with multiple episodes.
A season given as a single CSV file is much more prefered by our team and helps ensure our scheduling process is done efficiently and error free.
This program converts selected XMLs into a single CSV file which can be exported, saved, and viewed as a table.

#### This project can be found [here](https://metadata-converter.herokuapp.com/). 

## GET STARTED
### Set up Python virtual environment:
In Terminal:
```bash
python -m venv venv
source venv/Scripts/activate
```

### Install the project's packages:
In terminal:
```bash
pip install -r requirements.txt
```

### Run initial migrations in the project:
In terminal:
```bash
python manage.py migrate
```

### Apply changes:
git add .
git commit -m "<description of changes>"
git push heroku master
