import classes_db
import connection
import main


def country():
    ask = input("""country table
    1. INSERT
    2. DELETE
    3. UPDATE
    4. SELECT
    5. BACK
    >>>  """)
    if ask == "1":
        print("""columns
        1. country_id  2. name last 3. last_update""")
        name = (input("insert country name: "))
        result = classes_db.Country(name)
        print(result.insert())
        return country()
    elif ask == '2':
        print("""columns
        1. country_id  2. name last 3. last_update""")
        name = input("insert country name: ")
        country_id = int(input("insert country_id: "))
        result = classes_db.Country(name)
        print(result.delete(country_id))
        return country()
    elif ask == '3':
        print("""columns
        1. country_id  2. name last 3. last_update""")
        query = input("""qaysi malumotni yangilashni hohlaysiz:
        1. country_id
        2. country_name
        >>> """)
        if query == '1':
            result = classes_db.Country.get_id()
            for i in result:
                print(i[0])
            print('yuqoridagi idlarni tanlash mumkin emas')
            old_id = int(input('eski country_id ni kiriting: '))
            new_id = int(input('yangi id ni kiriting: '))
            natija = classes_db.Country.update_id(old_id, new_id)
            print(natija)
            return country()
        elif query == "2":
            name = input("insert country name: ")
            country_id = int(input("insert country_id: "))
            result = classes_db.Country(name)
            print(result.update(country_id))
            return country()
        else:
            print('invalid input')
            return country()
    elif ask == '4':
        ask = input("""
        1. all data
        2. conditional search
        >>>> """)
        if ask == '1':
            data = classes_db.Country.select('SELECT')
            for row in data:
                print(row)
            return country()
        elif ask == '2':
            ask_1 = input("""qaysi shart bo'yicha qidirmoqchisiz 
            1. country_id
            2. name
            3. search with all conditions
            4. ORDER by
            5. search by letter
            >>>>""")
            if ask_1 == '1':
                id = int(input('insert country_id: '))
                quer = f"""SELECT * FROM country WHERE country_id={id} ORDER BY country_id;"""
                result = classes_db.Country.select(quer)
                for row in result:
                    print(row)
                return country()
            elif ask_1 == '2':
                name = input('insert name: ')
                quer = f"""SELECT * FROM country WHERE name='{name}' ORDER BY country_id;"""
                result = classes_db.Country.select(quer)
                for i in result:
                    print(i)
                return country()
            elif ask_1 == '3':
                id = int(input('insert country_id: '))
                name = input('insert name: ')
                quer = f"""SELECT * FROM country WHERE country_id={id} and name='{name}' ORDER BY country_id;"""
                result = classes_db.Country.select(quer)
                for i in result:
                    print(i)
                return country()
            elif ask_1 == "4":
                quer = f"""SELECT * FROM country ORDER BY country_id;"""
                result = classes_db.Country.select(quer)
                for i in result:
                    print(i)
                return country()
            elif ask_1 == "5":
                letter = input('Enter the letter in the text you are looking for: ')
                quer = f"""SELECT * FROM country WHERE name LIKE '%{letter}%';"""
                result = classes_db.Country.select(quer)
                for i in result:
                    print(i)
                return country()
            else:
                print('ERROR')
                return country()
        else:
            print('ERROR')
            return country()
    elif ask == '5':
        return main.main()
    else:
        print('ERROR ')
        return country()


def city():
    ask = input("""city table
    1. INSERT
    2. DELETE
    3. UPDATE
    4. SELECT
    5. BACK
    >>>  """)
    if ask == '1':
        print("""           columns
               1. city_id  2.name  3. country_id 4. last_update""")
        name = input('insert name: ')
        data = classes_db.Country.get_id()
        print('mavjud country_idlar>>')
        for i in data:
            print(i[0])
        country_id = int(input('insert country_id: '))
        result = classes_db.City(name)
        print(result.insert(country_id))
        return city()
    elif ask == '2':
        print("""               columns
                1. city_id  2.name  3. country_id 4. last_update""")
        name = input('insert name: ')
        city_id = int(input('insert city_id: '))
        result = classes_db.City(name)
        print(result.delete(city_id, 'city', 'city_id'))
        return city()
    elif ask == '3':
        name = input('insert name: ')
        city_id = int(input('insert city_id: '))
        result = classes_db.City(name)
        print(result.update(city_id, 'city', 'city_id'))
        return city()
    elif ask == '4':
        query = input(""" qaysi shart bo'yicha qidirmoqchisiz
        1. all data
        2. city_id
        3. country_id
        4. name
        5. search by letter
        6. ORDER by
        >>> """)
        if query == '1':
            result = classes_db.City.select('SELECT', 'city')
            for i in result:
                print(i)
            return city()
        elif query == '2':
            city_id = int(input('insert city_id: '))
            query_2 =f"""SELECT*FROM city WHERE city_id = {city_id}"""
            result = classes_db.City.select(query_2, 'city')
            for i in result:
                print(i)
            return city()
        elif query == '3':
            country_id = int(input('insert country_id: '))
            query_2 = f"""SELECT*FROM city WHERE country_id = {country_id}"""
            result = classes_db.Country.select(query_2, 'city')
            for i in result:
                print(i)
            return city()
        elif query == '4':
            name = input('insert name: ')
            query_2 = f"""SELECT*FROM city WHERE name = '{name}'"""
            result = classes_db.City.select(query_2, 'city')
            for i in result:
                print(i)
            return city()
        elif query == '5':
            search = input('Enter the letter in the text you are looking for: ')
            query_2 = f"""SELECT*FROM city WHERE name LIKE '%{search}%'"""
            result = classes_db.City.select(query_2, 'city')
            for i in result:
                print(i)
            return city()
        elif query == '6':
            query_2 = f"""SELECT * FROM city ORDER BY city_id"""
            result = classes_db.City.select(query_2, 'city')
            for i in result:
                print(i)
            return city()
        else:
            print('Invalid')
            return city()
    elif ask == '5':
        return main.main()
    else:
        print('Invalid')
        return city()


# ADDRESS PAGE
def address():
    ask = input("""address table
    1. INSERT
    2. DELETE
    3. UPDATE
    4. SELECT
    5. BACK
    >>>  """)
    if ask == "1":
        name = input('insert name: ')
        result = classes_db.Address(name)
        data = classes_db.Country.get_id('city', 'city_id')
        for i in data:
            print(i[0])
        print('mavjud city_id lar ')
        city_id = input('insert city_id: ')
        print(result.insert(city_id))
        return address()
    elif ask == '2':
        name = input('insert name: ')
        address_id = input('insert address_id: ')
        result = classes_db.Address(name)
        print(result.delete(address_id, 'address', 'address_id'))
        return address()
    elif ask == '3':
        print("""columns
        1. address_id  2. name 3. city_id 3. last_update""")
        query = input("""qaysi malumotni yangilashni hohlaysiz:
        1. address_id
        2. address_name
        3. city_id
        >>> """)
        if query == '1':
            result_1 = classes_db.Country.get_id('address', 'address_id')
            for j in result_1:
                print(j[0])
            print('yuqoridagi idlarni tanlash mumkin emas')
            old_id = int(input('eski address_id ni kiriting: '))
            new_id = int(input('yangi id ni kiriting: '))
            natija = classes_db.Address.update_id(old_id, new_id, 'address_id', 'address')
            print(natija)
            return address()
        elif query == '2':
            name = input('insert name: ')
            address_id = int(input('insert address_id: '))
            result = classes_db.Address(name)
            print(result.update(address_id, 'address', 'address_id'))
            return address()
        elif query == '3':
            print('mavjud city_id lar>>>')
            data = classes_db.Country.get_id('city', 'city_id')
            for i in data:
                print(i[0])
            city_id_1 = input('insert old city_id: ')
            city_id_2 = input('insert new city_id: ')
            print(classes_db.Address.update_id(city_id_1, city_id_2, 'city_id', 'address'))
            return address()
        else:
            print('ERROR')
            return address()
    elif ask == '4':
        query = input("""
        1. all data
        2. conditional search
        >>> """)
        if query == '1':
            result_1 = classes_db.Address.select('SELECT', 'address')
            for i in result_1:
                print(i)
            return address()
        elif query == '2':
            query_2 = input("""
            1. search by city_id 
            2. search by name
            3. search by address_id
            4. Order by
            5. Search by letter
            >>>>> """)
            if query_2 == '1':
                city_id = input('insert city_id: ')
                query_x = f"""SELECT * FROM address WHERE city_id = {city_id};"""
                result = classes_db.Address.select(query_x, 'address')
                for i in result:
                    print(i)
                return address()
            elif query_2 == '2':
                name = input('insert name: ')
                query_x = f"""SELECT * FROM address WHERE name = '{name}';"""
                result = classes_db.Address.select(query_x, 'address')
                for i in result:
                    print(i)
                return address()
            elif query_2 == '3':
                address_id = input('insert address_id: ')
                query_x = f"""SELECT * FROM address WHERE address_id = {address_id};"""
                result = classes_db.Address.select(query_x, 'address')
                for i in result:
                    print(i)
                return address()
            elif query_2 == '4':
                query_x = f"""SELECT * FROM address ORDER BY address_id;"""
                result = classes_db.Address.select(query_x, 'address')
                for i in result:
                    print(i)
                return address()
            elif query_2 == '5':
                letter = input('insert letter: ')
                query_x = f"""SELECT * FROM address WHERE name LIKE '%{letter}%';"""
                result = classes_db.Address.select(query_x, 'address')
                for i in result:
                    print(i)
                return address()
            else:
                print('Invalid')
                return address()
        else:
            print('Invalid')
            return address()
    elif ask == '5':
        return main.main()
    else:
        print('Invalid')
        return address()

