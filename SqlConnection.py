import sqlite3


class SQLConnection():

  def __init__(self,business_object:str,database:str)
    try:
      self._conn=sqlite3.connect(database)
    except:
      
     
