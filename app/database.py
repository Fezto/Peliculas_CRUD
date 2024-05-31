#? Contiene la clase "Database", la cual abstrae todavía más la interacción con la base
#? de datos establecida por Flask-SQLAlchemy

from sqlalchemy import text, select, Table, insert
from app import app
from app import database


class Database:

    #* Constructor. Aquí declaramos las propiedades de la clase
    #* las cuales serán las tablas de la base de datos.
    def __init__(self):
        self.database = database

        with app.app_context():
            self.database.reflect()

        self.addresses: Table = self.database.metadata.tables["addresses"]
        self.brands: Table = self.database.metadata.tables["brands"]
        self.categories: Table = self.database.metadata.tables["categories"]
        self.clients: Table = self.database.metadata.tables["clients"]
        self.colors: Table = self.database.metadata.tables["colors"]
        self.genders: Table = self.database.metadata.tables["genders"]
        self.materials: Table = self.database.metadata.tables["materials"]
        self.order_details: Table = self.database.metadata.tables["order_details"]
        self.orders: Table = self.database.metadata.tables["orders"]
        self.products: Table = self.database.metadata.tables["products"]
        self.sizes: Table = self.database.metadata.tables["sizes"]
        self.subscriptions: Table = self.database.metadata.tables["subscriptions"]
        self.type_subscriptions: Table = self.database.metadata.tables["type_subscriptions"]

    #* Sobrecarga del operador []. Nos permite acceder a las propiedades
    #* de la clase mediante corchetes. En vez de db.tabla, podemos usar
    #* db[tabla], lo que facilita el acceso dinámicamente.
    def __getitem__(self, table_name: str = None):
        try:
            return getattr(self, table_name)
        except:
            raise KeyError(f"La tabla {table_name} no existe!")

    #* Regresa todos los registros de una tabla
    def select_all(self, table: Table = None):
        stmt = select(table)
        result = self.database.session.execute(stmt)
        return result.all()

    #* Regresa una lista con el nombre de todas las columnas
    def select_columns(self, table: Table = None):
        columns = table.c
        return list(columns.keys())

    #* Regresa una lista con el nombre de todas las tablas
    def select_tables(self):
        tables = self.database.metadata.tables
        return list(tables.keys())

    #* Inserta uno o varios registros
    def insert_into(self, table: Table = None, data: dict = None ):
        print("Insertando!....")
        stmt = insert(table).values(**data)

        self.database.session.execute(stmt)
        self.database.session.commit()

    #* Regresa datos relevantes de todas las columnas de cierta tabla
    def select_columns_data(self, table: Table = None):
        table_info = {}

        for column in table.c:
            table_info[column.name] = {
                "name": str(column.name),
                "type": str(column.type),
                "nullable": column.nullable,
                "default": str(column.default.arg) if column.default is not None else None,
                "primary_key": column.primary_key,
                "foreign_key": column.foreign_keys
            }

        return table_info