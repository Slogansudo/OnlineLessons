from connection import Database


class Country:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def select(quer, table="country"):
        if quer == 'SELECT':
            query = f"""SELECT * FROM {table}"""
            return Database.connect(query, 'SELECT')
        else:
            return Database.connect(quer, 'SELECT')

    def insert(self, table="country"):
        query = f"""INSERT INTO {table}(name) VALUES('{self.name}')"""
        return Database.connect(query, 'INSERT')

    def update(self, country_id, table="country", column="country_id"):
        query = f"""UPDATE {table} SET name = '{self.name}' WHERE {column}={country_id}"""
        return Database.connect(query, 'UPDATE')

    def delete(self, country_id, table='country', column="country_id"):
        query = f"""DELETE FROM {table} WHERE name = '{self.name}' and {column} = {country_id}"""
        return Database.connect(query, 'DELETE')

    @staticmethod
    def update_id(old_id, new_id, column_name='country_id', table="country"):
        query = f"""UPDATE {table} SET {column_name}={new_id} WHERE {column_name}={old_id}"""
        return Database.connect(query, 'UPDATE')

    @staticmethod
    def get_id(table="country", column_name='country_id'):
        query = f"""SELECT {column_name} FROM {table}"""
        return Database.connect(query, 'SELECT')


class City(Country):
    def __init__(self, name):
        super().__init__(name)

    def insert(self, country_id, table="city"):
        query = f"""INSERT INTO {table}(name, country_id) VALUES('{self.name}', {country_id});"""
        return Database.connect(query, 'INSERT')


class Address(Country):
    def __init__(self, name):
        super().__init__(name)

    def insert(self, city_id, table='address'):
        query = f"""INSERT INTO {table}(name, city_id) VALUES('{self.name}',{city_id});"""
        return Database.connect(query, 'INSERT')


class Customer:
    def __init__(self, first_name, last_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.__password = password

    def insert(self, phone_number, birth_date, address_id, table="customer"):
        query = f"""INSERT INTO {table}(first_name, last_name, phone_number, birth_date, password, address_id) VALUES(
        '{self.first_name}',  '{self.last_name}', '{phone_number}', '{birth_date}', '{self.__password}', {address_id}); """
        return Database.connect(query, 'INSERT')

    @staticmethod
    def delete(query):
        return Database.connect(query, 'DELETE')

    @staticmethod
    def update(customer_id, column, new_data, table="customer"):
        if new_data is int:
            query = f"""UPDATE {table} SET {column}={new_data} WHERE customer_id={customer_id};"""
            return Database.connect(query, 'UPDATE')
        else:
            query = f"""UPDATE {table} SET {column}='{new_data}' WHERE customer_id={customer_id}"""
            return Database.connect(query, 'UPDATE')

    @staticmethod
    def select(quer, table="customer"):
        if quer == 'SELECT':
            query = f"""SELECT * FROM {table};"""
            return Database.connect(query, 'SELECT')
        else:
            return Database.connect(quer, 'SELECT')


class Product:
    def __init__(self, title: str, rating: float):
        self.title = title
        self.rating = rating

    def insert(self, description, create_date, table="product"):
        query = f"""INSERT INTO {table}(title, description, rating, create_date) VALUES (
        '{self.title}', '{description}', {self.rating}, '{create_date}');"""
        return Database.connect(query, 'INSERT')

    @staticmethod
    def delete(column, data, table="product"):
        if data is int and column == 'product_id':
            query = f"""DELETE FROM {table} WHERE {column}={data};"""
            return Database.connect(query, 'DELETE')
        else:
            query = f"""DELETE FROM {table} WHERE {column}= '{data}';"""
            return Database.connect(query, "DELETE")

    @staticmethod
    def update(query):
        return Database.connect(query, "UPDATE")

    @staticmethod
    def select(query):
        return Database.connect(query, "SELECT")

class Product_customer:
    @staticmethod
    def insert(product_id, customer_id, table="product_customer"):
        query = f"""INSERT INTO {table}(product_id, customer_id) VALUES({product_id}, {customer_id}); """
        return Database.connect(query, 'INSERT')

    @staticmethod
    def delete(data, column, table="product_customer"):
        query = f"""DELETE FROM {table} WHERE {column}={data};"""
        return Database.connect(query, 'DELETE')

    @staticmethod
    def update(column, data, search_column, search_data, table="product_customer"):
        if search_data is int and data is int:
            query = f"""UPDATE {table} SET {column}={data} WHERE {search_column}={search_data};"""
        elif search_data is int and data is str:
            query = f"""UPDATE {table} SET {column}='{data}' WHERE {search_column}={search_data};"""
        elif search_data is str and data is int:
            query = f"""UPDATE {table} SET {column}={data} WHERE {search_column}='{search_data}';"""
        else:
            query = f"""UPDATE {table} SET {column}='{data}' WHERE {search_column}='{search_data}';"""
        return Database.connect(query, 'UPDATE')

    @staticmethod
    def select(query):
        return Database.connect(query, "SELECT")


class Product_type(Country):
    def __init__(self, name):
        super().__init__(name)

    def insert(self, color: str, price: int, product_id: int, table="product_type"):
        query = f"""INSERT INTO {table}(color, price, name, product_id) VALUES('{color}', {price}, '{self.name}', {product_id});"""
        return Database.connect(query, 'INSERT')
