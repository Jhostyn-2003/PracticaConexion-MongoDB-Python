#se importa la libreria de mongoDB para la conexion
import pymongo

MONGO_HOST = "localhost"
MONGO_PUERTO = "27017"
MONGO_TIEMPO_FUERA = 1000

#Conexion de la base de datos
MONGO_URI = "mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"

#Se apunta a la abase de datos miscelanea y la coleccion books
MONGO_BASEDATOS = "miscelanea"
MONGO_COLECCION = "books"

#se genera la conexion 
cliente = pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
baseDatos = cliente [MONGO_BASEDATOS]
coleccion = baseDatos[MONGO_COLECCION]

#return la lista de coleccion en la base de datos 
print(baseDatos.list_collection_names())

#verificamos si existe la coleccion dentro de la base de datos 
collist = baseDatos.list_collection_names()
if "books" in collist:
    print("La coleccion existe")

#buscamos en el primer documento la coleccion
documentoUno = coleccion.find_one()
print(documentoUno)


#se retorna todos los documentos de la coleccion book y se escr
for documentoUno in coleccion.find():
    print(documentoUno)

#este sirve para verificar el estado del documento uno, de la coleccion books
for EstadoDocumento in coleccion.find({},{"status":1}):
    print(EstadoDocumento)

#Query advanzadas Nº 3
myquery ={"status":{"$gt":"p"}}

mydoc = coleccion.find(myquery)
for DocumentoTres in mydoc:
    print(DocumentoTres)



