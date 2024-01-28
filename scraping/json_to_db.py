import json
import sqlite3
#from django.db import connections


conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
#connection = connections['default']
with open('lawyers.json', 'r',encoding='utf-8') as json_file:
    json_data = json.load(json_file)




for data in json_data:
 #with connection.cursor() as cursor:
  email = "default@gmail.com"
  password = "default"
  competences = "default"
  experiences = "default"

#   if email == "":
#         email ="default@gmail.com"
  cursor.execute('''
        INSERT INTO register_avocats (nom_complet, domaine_juridique, location, numero_telephone,competences,experiences, email,password, Description)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data["Name"],
        data["Categories"],
        data["Address"],
        data["Phone"],
        competences,
        experiences,
        email,
        password,
        data["Description"]
    ))


#print("Data inserted successfully.")
#print(len(json_data))


conn.commit()
conn.close()
