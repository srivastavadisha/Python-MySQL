import DatabaseLayer as db_layer

def setting_up_database():
	db_obj = db_layer.set_up_database()
	return db_obj

def insert_into_bl():
    val=setting_up_database()
    db_obj=val
    #db_layer.connect_to_database()
    a=int(input("Enter bookid:\n"))
    b=input("Enter bookname:\n")
    c=int(input("Enter price:\n"))
    db_layer.insert_into_database(db_obj,a,b,c)
    print("insert success")

def insert_with_parameter(bookid,bookname,price):
    val=setting_up_database()
    db_obj=val
    #db_layer.connect_to_database()
    db_layer.insert_into_database(db_obj,bookid,bookname,price)
    print("insert success")

def update_to_bl():
    val=setting_up_database()
    x=int(input("Set BookId:\n"))
    y=int(input("Where BookId:\n"))
    db_layer.update_to_database(val,x,y)
    print("update success")

def select_from_bl():
    val=setting_up_database()
    x=int(input("Select where BookId is:\n"))
    db_layer.select_from_database(val,x)
    print("select success")

def delete_from_bl():
    val=setting_up_database()
    x=input("Delete where title is:\n")
    db_layer.delete_from_database(val,x)
    print("delete success")

#def func in businesslayer and in that func call another func of databaselayer
