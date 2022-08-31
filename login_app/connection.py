import psycopg2
from django.db import connections


class databaseConn:
    
    def getConnectionPostgres(self):
        try:
            con = connections['default'].cursor()
            return con
        except Exception as e:
            print('e',e)
    
    def getResultSet_named_params(self, con, query):
        try:
            con.execute(query)
            rows = con.fetchall()
            colnames = [desc[0] for desc in con.description]
            l=[]
            #print(colnames)
            # data= {}
            for x in range(len(rows)):
                data= {}
                for y in range(len(colnames)):
                    data[colnames[y]]=rows[x][y]
                l.append(data)               
            con.close()
            # print (l)
            return l

        except Exception as e:
            print('e',e)
    