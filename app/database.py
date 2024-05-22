#? Contiene la clase "Database", la cual abstrae todavía más la interacción con la base
#? de datos establecida por Flask-SQLAlchemy

from sqlalchemy import text, select, Table
from app import app
from app import database


class Database:

    #* Constructor. Aquí declaramos las propiedades de la clase las cuales serán las tablas
    #* de la base de datos.
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

    def __getitem__(self, table_name: str = None):
        try:
            return getattr(self, table_name)
        except:
            raise KeyError(f"La tabla {table_name} no existe!")

    def select_all(self, table: Table = None):
        stmt = select(table)
        result = self.database.session.execute(stmt)
        return result.all()

    def select_columns(self, table: Table = None):
        columns = table.c
        return list(columns.keys())

    def select_tables(self):
        tables = self.database.metadata.tables
        return list(tables.keys())
