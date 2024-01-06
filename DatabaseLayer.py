import mysql.connector

def connect_to_database():
	try:
		mydb=mysql.connector.connect(
	    	host='localhost' ,
	    	user='root',
	    	password='113008',
	    	database='db1'
			    )
		#print("In connect_to_database TRY Block")
		return mydb
	except:
		#print("In connect_to_database Except Block")
		return None

def insert_into_database(db_obj,param_id,param_name,param_price):
	s="INSERT INTO book (bookid,title,price) VALUES(%s,%s,%s)"
	b1=(param_id, param_name, param_price)
	cursor_var = db_obj.cursor()
	cursor_var.execute(s,b1)
	db_obj.commit()

def update_to_database(db_obj,param_id1,param_id2):
	s="UPDATE book SET bookid=%s WHERE bookid=%s"
	b2=(param_id1, param_id2)
	cursor_var = db_obj.cursor()
	cursor_var.execute(s,b2)
	db_obj.commit()

def select_from_database(db_obj,param_id3):
	#s="SELECT * from book where bookid = %s"
	b3=(param_id3,)
	cursor_var = db_obj.cursor()
	cursor_var.execute("SELECT * from book where bookid = %s",b3)
	print("lol")
	for x in cursor_var:
		print (x)
	print("lol")
	#db_obj.commit()
	
def delete_from_database(db_obj,param_name1):
	s="DELETE FROM book WHERE title=%s"
	b4=(param_name1,)
	cursor_var = db_obj.cursor()
	cursor_var.execute(s,b4)
	db_obj.commit()


def set_up_database():
	db_connected = connect_to_database()
	if db_connected is None:
		print("Connect to Database Not Successded-------");
		exit(0)
	print("Connect to DataBase Succeded\n")
	return db_connected

def db_core_func():
	db_connected = set_up_database()
	while True:
		q=int(input("Enter a no.: "))
		if(q==1):
			#insert
			print("\nInsert into database:")
			r=int(input("Enter BookId\n"))
			n=input("Enter Title\n")
			m=int(input("Enter Price\n"))
			insert_into_database(db_connected,r,n,m)
			print("Insert Success\n")
		elif(q==2):
			#update
			print("\nUpdate to database:")
			x=int(input("Set BookId\n"))
			y=int(input("Where BookId\n"))
			update_to_database(db_connected,x,y)
			print("Update Success\n")
		elif(q==4):
			#delete
			print("\nDelete from database:")
			a=input("Delete where title is: ")
			delete_from_database(db_connected,a)
			print("Delete Success\n")
		elif(q==3):
			#select
			print("\nSelect from database:")
			p=int(input("Select where bookid is\n"))
			select_from_database(db_connected,p)
			print("Select Success\n")
		elif(q==0):
			print("\nExit")
			exit(0)
		else:
			print("\nInvalid\n")


	# As the program run start take value from console  
	# if value is 1 : insert functionality 
	# if value is 2 : select funtionality 
	# if value is 3 : delete functionality 
	# if value is 4 : update functionality 
	# if value is 0 : exit the loop 
	# other input is invalid 


print("Initialise DataBaseLayer.py : outside of main ")

if __name__=="__main__":
	print("I am in Main of DB.py ")
	db_core_func()