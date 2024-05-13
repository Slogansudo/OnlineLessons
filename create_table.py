import connection



def create_table():
    country_table = """
    CREATE TABLE country(
    country_id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    last_update TIMESTAMP DEFAULT now());"""

    city_table = """
       CREATE TABLE city(
       city_id SERIAL PRIMARY KEY,
       name VARCHAR(50),
       country_id INT REFERENCES country(country_id),
       last_update TIMESTAMP DEFAULT now());"""

    address_table = """
           CREATE TABLE address(
           address_id SERIAL PRIMARY KEY,
           name VARCHAR(50),
           city_id INT REFERENCES city(city_id),
           last_update TIMESTAMP DEFAULT now());"""

    customer_table = """
           CREATE TABLE customer(
           customer_id SERIAL PRIMARY KEY,
           first_name VARCHAR(40),
           last_name VARCHAR(40),
           phone_number VARCHAR(12),
           birth_date TIMESTAMP NOT NULL,
           password VARCHAR(16),
           address_id INT REFERENCES address(address_id),
           last_update TIMESTAMP DEFAULT now());"""

    product_table = """
           CREATE TABLE product(
           product_id SERIAL PRIMARY KEY,
           title VARCHAR(50),
           description VARCHAR(40),
           rating FLOAT NOT NULL, 
           last_update TIMESTAMP DEFAULT now(),
           create_date DATE);"""

    product_customer_table = """
           CREATE TABLE product_customer(
           product_customer_id SERIAL PRIMARY KEY,
           product_id INT REFERENCES product(product_id),
           customer_id INT REFERENCES customer(customer_id),
           last_update TIMESTAMP DEFAULT now());"""

    payment_status_table = """
           CREATE TABLE payment_status(
           payment_status_id SERIAL PRIMARY KEY,
           name VARCHAR(50),
           last_update TIMESTAMP DEFAULT now());"""

    payment_type_table = """
           CREATE TABLE payment_type(
           payment_type_id SERIAL PRIMARY KEY,
           name VARCHAR(50),
           last_update TIMESTAMP DEFAULT now());"""

    payment_table = """
           CREATE TABLE payment(
           payment_id SERIAL PRIMARY KEY,
           product_customer_id INT REFERENCES product_customer(product_customer_id),
           amount FLOAT,
           payment_type_id INT REFERENCES payment_type(payment_type_id),
           payment_status_id INT REFERENCES payment_status(payment_status_id),
           last_update TIMESTAMP DEFAULT now());"""

    product_type_table = """
           CREATE TABLE product_type(
           product_type_id SERIAL PRIMARY KEY,
           color VARCHAR(30) NOT NULL,
           price INT NOT NULL,
           name VARCHAR(50),
           product_id INT REFERENCES product(product_id));"""

    category_table = """
           CREATE TABLE category(
           category_id SERIAL PRIMARY KEY,
           title VARCHAR(50),
           description VARCHAR(50),
           last_update TIMESTAMP DEFAULT now(),
           create_date DATE DEFAULT now());"""

    product_category_table = """
           CREATE TABLE product_category(
           product_category_id SERIAL PRIMARY KEY,
           product_id INT REFERENCES product(product_id),
           category_id INT REFERENCES category(category_id),
           last_update TIMESTAMP DEFAULT now());"""
    punk_table = """
           CREATE TABLE punk(
           punk_id SERIAL PRIMARY KEY,
           name VARCHAR(50),
           address_id INT REFERENCES address(address_id),
           last_update TIMESTAMP DEFAULT now());"""

    store_table = """
           CREATE TABLE store(
           store_id SERIAL PRIMARY KEY,
           name VARCHAR(50),
           description VARCHAR(50),
           address_id INT REFERENCES address(address_id),
           last_update TIMESTAMP DEFAULT now());"""

    data_table = {
        "country_table": country_table,
        "city_table": city_table,
        "address_table": address_table,
        "customer_table": customer_table,
        "product_table": product_table,
        "product_customer_table": product_customer_table,
        "payment_status_table": payment_status_table,
        "payment_type_table": payment_type_table,
        "payment_table": payment_table,
        "product_type_table": product_type_table,
        "category_table": category_table,
        "product_category_table": product_category_table,
        "punk_table": punk_table,
        "store_table": store_table
    }
    for i in data_table:
        print(f"{i} {connection.Database.connect(data_table[i], 'CREATE')}")
    return main.main()

