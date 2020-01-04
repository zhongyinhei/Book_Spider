import pymysql

class main(object):
  def if_first(self,code):
      host='localhost'
      user='root'
      passwd=''
      port=3306
      db='neepu_pro'
      db=pymysql.connect(
         host=host,
         user=user,
         passwd=passwd,
         db=db,
         port=port,
         charset='utf8',
         cursorclass = pymysql.cursors.DictCursor
         )
      cursor=db.cursor()
      sql="select * from table_main where openid = '"+code+"' "
      cursor.execute(sql)
      try:
        cursor.execute(sql)
        result=cursor.rowcount
        if result  == 0:
           return "false"
        else:
           return "true"
      except:
        return "erro"