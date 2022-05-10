from datetime import date 
from dbhelperVozParkinson import DBHelper

db = DBHelper()

hoy = date.today()


condicion = hoy
db.update_estado(condicion)