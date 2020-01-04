import pymssql

class Main(object) :
   def get_data(self):
    conn = pymssql.connect("localhost", "sa", "w@19980215", "neepu_pro")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM seats_1")
    data = cursor.fetchall()
    listx = list(data)
    return(listx)


