#importar el pymongo para la conexion 
import pymongo

#create la base de datos "dbJhostynGavilanezL00081412"
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbJhostynGavilanezL00081412"] #dbJhostynGavilanezL00081412

#retornamos a la lista del sistema de bases de datos
print(myclient.list_database_names())

#verificamos si existe la "dbJhostynGavilanezL00081412" 
dblist = myclient.list_database_names()

if "dbJhostynGavilanezL00081412" in dblist:
    print("La base de datos Existe")
else: 
    print("La base de datos  no existe")
    





