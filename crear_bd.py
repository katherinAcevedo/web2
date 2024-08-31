# importar la libreria para gestionar la BD
import sqlite3

# establecer la conexion 
conexion = sqlite3.connect('web2.sqlite3')
cursor = conexion.cursor()

#eliminar tabla 
cursor.execute("""
DROP TABLE IF EXISTS productos;
""")


 #crear tabla 
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
   id INTEGER PRIMARY KEY,
   categoria TEXT NOT NULL,
   marca TEXT NOT NULL,
   nombre TEXT NOT NULL,
   descripcion TEXT NOT NULL,
   precio INTEGER NOT NULL
 );
""")

# INSERTA DATOS INICIALES 
datos = [
    (101, 'celular', 'Apple', 'iphone 15', '128GB+6GB RAM, Pantalla 6.1p, Chip A16 Bionic, cable Tipo C, Camara 48MP', 4599900),
    (104, 'celular', 'Samsung', 'Galaxy s23', '128GB+6GB RAM, Pantalla 6.1p, Chip A16 Bionic, cable Tipo C, Camara 48MP', 4599900),
    (201, 'Portatil', 'Apple', 'Macbook pro M2', '128GB+6GB RAM, Pantalla 6.1p, Chip A16 Bionic, cable Tipo C, Camara 48MP', 4599900),
    (203, 'Portatil', 'Asus', 'Laptop ROG zephyrus', '128GB+6GB RAM, Pantalla 6.1p, Chip A16 Bionic, cable Tipo C, Camara 48MP', 4599900),
    (207, 'Portatil', 'HP', 'Laotop 14-fq1012la', '128GB+6GB RAM, Pantalla 6.1p, Chip A16 Bionic, cable Tipo C, Camara 48MP', 4599900),
    (208, 'Portatil', 'Lenovo', 'Todo en uno', '128GB+6GB RAM, Pantalla 6.1p, Chip A16 Bionic, cable Tipo C, Camara 48MP', 4599900),
    (301, 'Tablet', 'Apple', 'ipad 10gen', '128GB+6GB RAM, Pantalla 6.1p, Chip A16 Bionic, cable Tipo C, Camara 48MP', 4599900),
    (302, 'Tablet', 'Amazon', 'kindle oasis 10gen', '128GB+6GB RAM, Pantalla 6.1p, Chip A16 Bionic, cable Tipo C, Camara 48MP', 4599900),
    (304, 'Tablet', 'Huawei', 'MatePad SE 10.1', '128GB+6GB RAM, Pantalla 6.1p, Chip A16 Bionic, cable Tipo C, Camara 48MP', 4599900),

]

cursor.executemany("""
INSERT INTO productos VALUES (?, ?, ?, ?, ?, ?);
""", datos)

# grabar

conexion.commit()
conexion.close()
