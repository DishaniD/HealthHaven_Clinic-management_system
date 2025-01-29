set project_name=hospital
start cmd /k "vhospital\Scripts\activate && cd %project_name% && py manage.py runserver"
start chrome http://127.0.0.1:8000/