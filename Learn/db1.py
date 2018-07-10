import pyodbc 
import logging

#Test This one first.
def QuantScreenRouter():

    try:
        cnxn = pyodbc.connect(
                r'Driver={SQL Server Native Client 11.0};'
                r'SERVER=f6iq6q5hoj.database.windows.net;'
                r'DATABASE=QuantValue;'
                r'UID='
                r'PWD=!'
            )

        logging.warning("before_request")
        cursor = cnxn.cursor()
        cursor.execute("exec [dbo].[QuantScreenRouter] 'LONG_AO','Toronto'")
        results = cursor.fetchall()
        #entries = [dict(title=row['Symbol'], text=row[1]) for row in results]

        #for row in results:
        #    print(row.Symbol)

        cnxn.close()
        cursor.close()
        return results


    except ValueError:
        pass


QuantScreenRouter()