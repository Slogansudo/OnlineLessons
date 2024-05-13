import classes_db
import tables_change
import tables_change_2
import tables_change_3
import create_table


def main():
    print('This is main page')
    query = input("""
    1. address            8. category
    2. city               9. product_category
    3. country            10. payment
    4. customer           11. payment_type
    5. product            12. payment_status
    6. product_customer   13. punk
    7. product_type       14. store
    15. Create
    
    >>>>  """)
    if query == '1':
        return tables_change.address()
    elif query == '2':
        return tables_change.city()
    elif query == '3':
        return tables_change.country()
    elif query == '4':
        return tables_change_2.customer()
    elif query == '5':
        return tables_change_2.product()
    elif query == '6':
        return tables_change_2.product_customer()
    elif query == '7':
        return tables_change_2.product_type()
    elif query == '8':
        return tables_change_2.category()
    elif query == '9':
        return tables_change_2.product_category()
    elif query == '10':
        return tables_change_3.payment()
    elif query == '11':
        return tables_change_3.payment_type()
    elif query == '12':
        return tables_change_3.payment_status()
    elif query == '13':
        return tables_change_3.punk()
    elif query == '14':
        return tables_change_3.store()
    elif query == '15':
        return create_table.create_table()
    else:
        print('Error')
        return main()


if __name__ == '__main__':
    main()
