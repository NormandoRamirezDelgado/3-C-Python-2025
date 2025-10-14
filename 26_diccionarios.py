#Creación de Diccionarios
mi_diccionario = {
    "nombre": "Juan",
    "edad"  : 30,
    "ciudad": "Madrid",
}

print('')
#Creación de diccionarios con Constyructor dict
otro_diccionario = dict(nombre="Ana", edad=25, ciudad="Barcelona")

print('')
#Acceso a los datos
print(mi_diccionario["nombre"])  # Salida: Juan
print(mi_diccionario.get("profesion"))  # Salida: None
print(mi_diccionario.get("profesion", "No Existe la Llave"))  # Salida: No especificada

print('')
#Modificar y Adicionar Elementos al Diccionario
# Modificar un valor existente
mi_diccionario["edad"] = 31

# Añadir un nuevo par clave-valor
mi_diccionario["profesion"] = "Ingeniero"

print(mi_diccionario)
# Salida: {'nombre': 'Juan', 'edad': 31, 'ciudad': 'Madrid', 'profesion': 'Ingeniero'}

print('')
#Método Keys, devuelve vista de todas las llaves del diccionario
claves = mi_diccionario.keys()
print(claves)  # Salida: dict_keys(['nombre', 'edad', 'ciudad', 'profesion'])

print('')
#Método Values, devuelve vista de todas los datos del diccionario
valores = mi_diccionario.values()
print(valores)  # Salida: dict_values(['Juan', 31, 'Madrid', 'Ingeniero'])

print('')
#Método Items, devuelve vista de todas los claves - datos del diccionario
items = mi_diccionario.items()
print(items)  # Salida: dict_items([('nombre', 'Juan'), ('edad', 31), ('ciudad', 'Madrid'), ('profesion', 'Ingeniero')])

print('')
# Elimina la clave especificada y devuelve su valor. Si la clave no se encuentra, devuelve el valor_por_defecto si se proporciona; de lo contrario, lanza un KeyError.
ciudad = mi_diccionario.pop("ciudad")
print(ciudad)  # Salida: Madrid

print('')
# Elimina y devuelve el último par clave-valor insertado en el diccionario
ciudad = mi_diccionario.popitem()
print(ciudad)  # Salida: Madrid
print(mi_diccionario)

print('')
# Actualiza el diccionario con los pares clave-valor de otro diccionario o de un iterable de pares clave-valor. Si una clave ya existe, su valor es sobrescrito.
mi_diccionario.update({"pais": "España", "edad": 32})
print(mi_diccionario)
# Salida: {'nombre': 'Juan', 'edad': 32, 'profesion': 'Ingeniero', 'pais': 'España'}

print('')
# Clear elimina todo el contenido de un diccionario
mi_diccionario.clear()
print(mi_diccionario)

print('')
# Recorrido de diccionarios
mi_diccionario = {
    "nombre": "Juan",
    "edad"  : 30,
    "ciudad": "Madrid",
}
for clave in mi_diccionario:
    print(clave, mi_diccionario[clave])

print('')
# Iterar sobre las claves explicitamente
for clave in mi_diccionario.keys():
    print(clave)

print('')
# Iterar sobre los valores
for valor in mi_diccionario.values():
    print(valor)

print('')
# Función len
programador = {
    "nombre": "Ada", 
    "apellido": "Lovelace", 
    "año_nacimiento": 1815
}
print(len(programador))
# Salida: 3

print('')
# Devuelve una representación en formato de cadena (string) del diccionario.
configuracion = {
    "host": "localhost", 
    "puerto": 8080
}
config_str = str(configuracion)
print(config_str)
# Salida: "{'host': 'localhost', 'puerto': 8080}"
print(type(config_str))
# Salida: <class 'str'>

print('')
# Creación de Diccionarios de manera manual
# Creando un diccionario de configuración
configuracion_app = {
    "host"          : "localhost",
    "puerto"        : 8080,
    "debug_mode"    : True,
    "admin_users"   : ["admin", "gloria"]
}

print(configuracion_app)
# Salida: {'host': 'localhost', 'puerto': 8080, 'debug_mode': True, 'admin_users': ['admin', 'gloria']}

# Accediendo a un valor
print(f"El modo debug está activado: {configuracion_app['debug_mode']}")

print('')
# Crear diccionario de manera dinámica
nombre_usuario = "ana_g"
nivel_acceso = "editor"
id_sesion = 84391

# Empezar con un diccionario vacío
sesion_activa = {}

# Cargar datos desde variables
sesion_activa["usuario"] = nombre_usuario
sesion_activa["nivel"] = nivel_acceso
sesion_activa["id"] = id_sesion

print(sesion_activa)
# Salida: {'usuario': 'ana_g', 'nivel': 'editor', 'id': 84391}

print('')
diccionario = {}
for i in range(5):
    clave = input('Introducir Clave: ')
    valor = input('Introducir un Valor: ')
    diccionario[clave] = valor
print(diccionario)

print('')
# Crear diccionario que me dan las claves
diccionarioDos = {}
diccionarioDos['nombre'] = input('Introducir el valor: ')
diccionarioDos['paterno'] = input('Introducir el valor: ')
diccionarioDos['materno'] = input('Introducir el valor: ')
diccionarioDos['edad'] = input('Introducir el valor: ')
diccionarioDos['especialidad'] = input('Introducir el valor: ')
print(diccionarioDos)

print('')
lista = ['nombre', 'paterno', 'materno', 'edad', 'especialidad']
for llave in lista:
    valor = input(f'Introducir un Valor para {llave}: ')
    diccionarioDos[llave] = valor
print(diccionarioDos)
