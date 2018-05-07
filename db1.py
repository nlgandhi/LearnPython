import pyodbc 


def QuantScreenRouter():
    cnxn = pyodbc.connect(
        r'Driver={SQL Server Native Client 11.0};'
        r'SERVER=f6iq6q5hoj.database.windows.net;'
        r'DATABASE=QuantValue;'
        r'UID=connectsoft@f6iq6q5hoj;'
        r'PWD=buysell1!'
        )

    cursor = cnxn.cursor()
    cursor.execute("exec [dbo].[QuantScreenRouter]('LONG_AO','Toronto')")

    for row in cursor:
        print(row.Symbol)

    cnxn.close()
    cursor.close()


QuantScreenRouter()