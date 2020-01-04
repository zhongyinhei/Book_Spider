import pymysql

class main(object):
  def insert_first(self,code,series_list):
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
      sql = ''
      cursor=db.cursor()
      if len(series_list) == 1:
        sql = "insert into table_main (series1,openid) value '"+series_list[0]+"','"+code+"' "
      if len(series_list) == 2:
        sql="insert into table_main (series1,series2,openid) value ('"+series_list[0]+"','"+series_list[1]+"','"+code+"') "
      if len(series_list) == 3:
        sql = "insert into table_main (series1,series2,series3,openid) value ('"+series_list[0]+"','"+series_list[1]+"','"+series_list[2]+"','"+code+"') "
      print(sql)
      cursor.execute(sql)
      db.commit()
      db.close()
      return "success"