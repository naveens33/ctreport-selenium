import sqlite3
import os

class CTDataBase():
    def __init__(self):
        FILEPATH='D:\\CTDATA.db'
        self.conn = sqlite3.connect(FILEPATH)
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS ExecutionRecord
                     (Execution_ID INTEGER PRIMARY KEY AUTOINCREMENT,session_details TEXT,report_options TEXT)''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS TestRecord 
                     (Execution_ID INTEGER,
                     Test_ID INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,id TEXT,description TEXT,start_time TEXT,
                     end_time TEXT,duration TEXT,result TEXT,priority TEXT, log TEXT,  FOREIGN KEY (Execution_ID) REFERENCES ExecutionRecord (Execution_ID))''')
            #self.c.execute("INSERT INTO ExecutionRecord(1,details1,details2)")

    def insert_execution_record(self,session_details,report_options):
        query="INSERT INTO ExecutionRecord(session_details,report_options) VALUES(\""+session_details+"\",\""+report_options+"\")"
        print(query)
        self.c.execute(query)
        self.conn.commit()

    def insert_test_record(self,name,id,desc,start_time,end_time,duration,result,priority,log):
        sel_query = "SELECT MAX(Execution_ID)  FROM ExecutionRecord"
        self.c.execute(sel_query)
        data = self.c.fetchall()
        print(data)
        query = "INSERT INTO TestRecord(Execution_ID,name,id,description,start_time,end_time,duration,result,priority,log) " \
                "VALUES(\"" +str(data[0][0])+"\",\"" + name + "\",\"" + id + "\",\"" + desc + "\",\"" + start_time + "\",\"" + end_time + "\",\"" + duration \
                + "\",\"" +result +"\",\""+priority+"\",\""+log+"\")"
        print(query)
        self.c.execute(query)
        self.conn.commit()

