import mysql.connector
try:
    conn = mysql.connector.connect(
        host ="localhost",
        user ="userpython",
        passwd ="123456",
        database ="arabicinfo"
        )
    cur =conn.cursor()
    cur.execute("""
                 create procedure zino_emp(in p_empno int , in p_empname varchar (99) character set utf8)
                 BEGIN
                      insert into emp 
                      values(p_empno ,convert( p_empname using utf8));
                 END
                 """)

except mysql.connector.Error as e:
    print(e)
    
    
    
    
