import classes_db
import main


def customer():
    ask = input("""customer table
    1. INSERT
    2. DELETE
    3. UPDATE
    4. SELECT
    5. BACK
    >>>  """)
    if ask == '1':
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        phone_number = input("insert phone number: ")
        birth_date = input("insert birth date: ")
        password = input("insert password: ")
        data_x = classes_db.Country.get_id('address', 'address_id')
        print('mavjud address_id lar')
        for i in data_x:
            print(i[0])
        address_id = int(input('insert address_id: '))
        data = classes_db.Customer(first_name, last_name, password)
        print(data.insert(phone_number, birth_date, address_id))
        return customer()
    elif ask == '2':
        query_x = input("""
        1. deleted by customer_id
        2. deleted by first_name
        3. deleted by customer_id and first_name
        >>>> """)
        if query_x == '1':
            customer_id = int(input('insert customer_id: '))
            query = f'DELETE FROM customer WHERE customer_id ={customer_id}'
            print(classes_db.Customer.delete(query))
            return customer()
        elif query_x == '2':
            first_name = input('insert first_name: ')
            query = f"""DELETE FROM customer WHERE first_name = '{first_name}"""
            print(classes_db.Customer.delete(query))
            return customer()
        elif query_x == '3':
            first_name = input('insert first_name: ')
            customer_id = int(input('insert customer_id: '))
            query = f"""DELETE FROM customer WHERE first_name = '{first_name}' and customer_id = {customer_id}"""
            print(classes_db.Customer.delete(query))
            return customer()
        else:
            print('invalid')
            return customer()
    elif ask == '3':
        print("""
        1. customer_id
        2. first_name
        3. last_name
        4. birth_date
        5. password
        6. address_id""")
        column = input("""insert column name: """)
        if column == 'customer_id':
            customer_id = int(input('insert search by customer_id: '))
            new_data = int(input('insert new customer_id: '))
            print(classes_db.Customer.update(customer_id, column, new_data))
            return customer()
        elif column == 'address_id':
            data_x = classes_db.Country.get_id('address', 'address_id')
            print('mavjud address_id lar')
            for i in data_x:
                print(i[0])
            customer_id = int(input('insert search by customer_id: '))
            new_data = int(input('insert new address_id: '))
            print(classes_db.Customer.update(customer_id, column, new_data))
            return customer()
        elif column == 'first_name' or column == 'last_name' or column == 'phone_number' or column == 'birth_date' or column == 'password':
            customer_id = int(input('insert search by customer_id: '))
            new_data = input('insert new data: ')
            print(classes_db.Customer.update(customer_id, column, new_data))
            return customer()
        else:
            print('invalid')
            return customer()
    elif ask == '4':
        query_2 = input("""
        1. all data
        2. conditional search
        >>> """)
        if query_2 == '1':
            data = classes_db.Customer.select('SELECT')
            for i in data:
                print(i)
            return customer()
        elif query_2 == '2':
            query_x = input("""
            1. search by customer_id
            2. search by first_name
            3. search by last_name
            4. search by address_id
            5. search by all query
            >>> """)
            if query_x == '1':
                id = int(input('insert search by customer_id: '))
                quer = f"""SELECT * FROM customer WHERE customer_id = {id};"""
                data = classes_db.Customer.select(quer, 'customer')
                for i in data:
                    print(i)
                return customer()
            elif query_x == '2':
                first_name = input('insert search by first_name: ')
                quer = f"""SELECT * FROM customer WHERE first_name = '{first_name}';"""
                data = classes_db.Customer.select(quer, 'customer')
                for i in data:
                    print(i)
                return customer()
            elif query_x == '3':
                last_name = input('insert search by last_name: ')
                quer = f"""SELECT * FROM customer WHERE last_name = '{last_name}';"""
                data = classes_db.Customer.select(quer, 'customer')
                for i in data:
                    print(i)
                return customer()
            elif query_x == '4':
                address_id = int(input('insert search by address_id: '))
                quer = f"""SELECT * FROM customer WHERE address_id = {address_id};"""
                data = classes_db.Customer.select(quer, 'customer')
                for i in data:
                    print(i)
                return customer()
            elif query_x == '5':
                customer_id = input('insert search by customer_id: ')
                first_name = input('insert search by first name: ')
                last_name = input('insert search by last name: ')
                address_id = input('insert search by address_id: ')
                quer = f"""SELECT * FROM customer WHERE customer_id = {customer_id} AND first_name = '{first_name}' AND last_name = '{last_name}' AND address_id = {address_id};"""
                data = classes_db.Customer.select(quer, 'customer')
                for i in data:
                    print(i)
                return customer()
            else:
                print('invalid')
                return customer()
        else:
            print('invalid')
            return customer()
    elif ask == '5':
        return main.main()
    else:
        print('invalid')
        return customer()


def product():
    ask = input("""product table
    1. INSERT
    2. DELETE
    3. UPDATE
    4. SELECT
    5. BACK
    >>>  """)
    if ask == '1':
        title = input('insert title: ')
        rating = float(input('insert rating: '))
        description = input('insert description: ')
        create_date = input('insert create date: ')
        data = classes_db.Product(title, rating)
        print(data.insert(description, create_date))
        return product()
    elif ask == '2':
        query_x = input("""
        1. deleted by title
        2. deleted by product_id
        >>>> """)
        if query_x == '1':
            title = input('insert title: ')
            print(classes_db.Product.delete('title', title))
            return product()
        elif query_x == '2':
            product_id = int(input('insert product_id: '))
            print(classes_db.Product.delete('product_id', product_id))
            return product()
        else:
            print('invalid')
            return product()
    elif ask == '3':
        ask_2 = input("""
        1. updated by title
        2. updated by product_id
        3. updated by create_date
        4. updated by rating
        >>>> """)
        if ask_2 == '1':
            title = input('insert new title: ')
            product_id = int(input('enter the product id of the reference to be changed: '))
            query = f"""UPDATE product SET title = '{title}' WHERE product_id = {product_id};"""
            print(classes_db.Product.update(query))
            return product()
        elif ask_2 == '2':
            data = classes_db.Country.get_id('product', 'product_id')
            for i in data:
                print(i[0])
            print('yuqoridagi product_id larni tanlash mumkin emas')
            product_id = int(input('insert new product_id: '))
            product_id_1 = int(input('enter the product id of the reference to be changed: '))
            query = f"""UPDATE product SET product_id = {product_id} WHERE product_id = {product_id_1};"""
            print(classes_db.Product.update(query))
            return product()
        elif ask_2 == "3":
            create_date = input('insert new create_date: ')
            product_id = int(input('enter the product id of the reference to be changed: '))
            query = f"""UPDATE product SET create_date = '{create_date}' WHERE product_id = {product_id};"""
            print(classes_db.Product.update(query))
            return product()
        elif ask_2 == '4':
            rating = input('insert new rating: ')
            product_id = int(input('enter the product id of the reference to be changed: '))
            query = f"""UPDATE product SET rating = {rating} WHERE product_id = {product_id};"""
            print(classes_db.Product.update(query))
            return product()
        else:
            print('invalid')
            return product()
    elif ask == '4':
        ask_x = input("""
        1. all data
        2. conditional search
        >>> """)
        if ask_x == '1':
            query = f"""SELECT * FROM product"""
            data = classes_db.Product.select(query)
            for row in data:
                print(row)
            return product()
        elif ask_x == '2':
            ask_y = input("""
            1. search by product_id
            2. search by title
            3. search by product_id and title
            4. search by title letter LIKE
            >>>> """)
            if ask_y == '1':
                product_id = int(input('enter the product_id: '))
                query = f"""SELECT * FROM product WHERE product_id = {product_id};"""
                data = classes_db.Product.select(query)
                for row in data:
                    print(row)
                return product()
            elif ask_y == '2':
                title = input('enter the title: ')
                query = f"""SELECT * FROM product WHERE title = '{title}';"""
                data = classes_db.Product.select(query)
                for row in data:
                    print(row)
                return product()
            elif ask_y == '3':
                product_id = input('input the product_id: ')
                title = input('input the title: ')
                query = f"""SELECT * FROM product WHERE product_id = {product_id} AND title = '{title}';"""
                data = classes_db.Product.select(query)
                for row in data:
                    print(row)
                return product()
            elif ask_y == '4':
                letter = input('input the letter: ')
                query = f"""SELECT * FROM product WHERE letter LIKE '%{letter}%';"""
                data = classes_db.Product.select(query)
                for i in data:
                    print(i)
                return product()
            else:
                print('invalid input')
                return product()
        else:
            print('invalid')
            return product()
    else:
        print('invalid input')
        return product()


def product_customer():
    ask = input("""product_customer table
    1. INSERT
    2. DELETE
    3. UPDATE
    4. SELECT
    5. BACK
    >>>  """)
    if ask == '1':
        data = classes_db.Country.get_id('product', 'product_id')
        print('majud product_id lar')
        for row in data:
            print(row[0])
        product_id = input('input product_id: ')
        data_1 = classes_db.Country.get_id('customer', 'customer_id')
        print('majud customer_id lar')
        for row in data_1:
            print(row[0])
        customer_id = input('input customer_id: ')
        print(classes_db.Product_customer.insert(product_id, customer_id))
        return product_customer()
    elif ask == '2':
        column = input('insert column name: ')
        data = input('insert new data: ')
        print(classes_db.Product_customer.delete(data, column))
        return product_customer()
    elif ask == '3':
        search_column = input('insert search column name: ')
        search_data = input('insert search data: ')
        column = input('insert column name for new data: ')
        data = input('insert new data: ')
        print(classes_db.Product_customer.update(column, data, search_column, search_data))
        return product_customer()
    elif ask == "4":
        query_x = input("""
        1. all data
        2. conditional search
        >>>> """)
        if query_x == '1':
            query = f"""SELECT * FROM product_customer"""
            data = classes_db.Product_customer.select(query)
            for row in data:
                print(row)
            return product_customer()
        elif query_x == '2':
            query_y = input("""
            1. search by product_customer_id
            2. search by customer_id and product_id
            >>> """)
            if query_y == '1':
                product_customer_id = input('input product_customer_id: ')
                query = f"""SELECT * FROM product_customer WHERE product_customer_id = {product_customer_id};"""
                data = classes_db.Product_customer.select(query)
                for row in data:
                    print(row)
                return product_customer()
            elif query_y == '2':
                product_id = input('input product_id: ')
                customer_id = input('input customer_id: ')
                query = f"""SELECT * FROM product_customer WHERE customer_id = {customer_id} AND product_id = {product_id};"""
                data_1 = classes_db.Product_customer.select(query)
                for row in data_1:
                    print(row)
                return product_customer()
            else:
                print('invalid')
                return product_customer()
        else:
            print('invalid')
            return product_customer()
    elif ask == '5':
        return main.main()
    else:
        print('invalid')
        return product_customer()


def product_type():
    ask = input("""product_type table
    1. INSERT
    2. DELETE
    3. UPDATE
    4. SELECT
    5. BACK
    >>>  """)
    if ask == '1':
        name = input('input product name: ')
        price = input('input product price: ')
        data = classes_db.Country.get_id('product', 'product_id')
        print('mavjud product_id lar')
        for row in data:
            print(row[0])
        product_id = input('input product_id: ')
        color = input('input color: ')
        data_x = classes_db.Product_type(name)
        print(data_x.insert(color, price, product_id))
        return product_type()

    elif ask == '2':
        pass
    elif ask == '3':
        pass
    elif ask == '4':
        pass
    elif ask == '5':
        return main.main()
    else:
        print("Invalid")
        return product_type()


def category():
    ask = input("""category table
    1. INSERT
    2. DELETE
    3. UPDATE
    4. SELECT
    5. BACK
    >>>  """)
    if ask == '1':
        pass
    elif ask == '2':
        pass
    elif ask == '3':
        pass
    elif ask == '4':
        pass
    elif ask == '5':
        return main.main()
    else:
        print("Invalid")
        return category()


def product_category():
    ask = input("""product_category table
    1. INSERT
    2. DELETE
    3. UPDATE
    4. SELECT
    5. BACK
    >>>  """)
    if ask == '1':
        pass
    elif ask == '2':
        pass
    elif ask == '3':
        pass
    elif ask == '4':
        pass
    elif ask == '5':
        return main.main()
    else:
        print("Invalid")
        return product_category()



