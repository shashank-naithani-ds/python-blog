# Python Django Blog

Blog made with python's Django framework.

## Installation

- Create virual enviroment in your project folder

    ```bash
    python -m venv nnv
    ```
    "nnv" is my virtual enviroment.

- Activate the environment 
   
    ```bash
        nnv\Scripts\activate
    ```
    Note: For deactivating use "deactivate" in terminal

- Install Django
    ```bash
    python -m django startproject 'projectname'
    ```
    Note: I use "pythonblog" as name.

- CD to "pythonblog" project directory and start the project.
    ```bash
    python manage.py runserver
    ```
    
## Create Articles Module
    ```bash
    python manage.py startapp articles
    ```