1. Database Connections
2. File Processing
3. Operating system level operations
4. REST API Calls
5. Data Processing


Database Connectivity
---------------------

1. create a connection object

	conn = mysql.connector.connect(host,db,userid,passwd)
	
	host -> location of database localhost // ipaddress / 192.10.1.1:3400
	


2. create a cursor object
    cursor = conn.cursor()


3. execute()
   execute_many()
   fetchAll()
   fetchOne()
   
