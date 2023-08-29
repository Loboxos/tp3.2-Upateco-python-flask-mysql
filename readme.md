## Creacion del entorno virtual y requerimientos

```cmd
python -m venv <nombre_del_entorno>

<nombre_del_entorno>\Scripts\activate

pip freeze > requirements.txt o pip install -r requirements.txt para instalar

pip install flask 
```
## creacion carpetas + estruc
/../Ejercicios_tp3_2/  
***|-- app/***    
  - **| |-- static|**
  - **| |-- __init__.py||**  
  - **| |-- database.py||**  

***|--config.py***   
***|--run.py***

# instalador conector MySql
```cmd
pip install mysql-connector-python.
```