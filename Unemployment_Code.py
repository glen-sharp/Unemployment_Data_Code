import mysql.connector
import pandas as pd

try:
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="11sharpG",
    database="data_practise"
    )

    sql_select_Query = "select * from unemployment_dataset"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()

    df = pd.DataFrame(records, columns=['date','unrate','unrate_men','unrate_women',
                                        'unrate_16_to_17','unrate_18_to_19','unrate_20_to_24',
                                        'unrate_25_to_34','unrate_35_to_44','unrate_45_to_54',
                                        'unrate_55_over'])
    df['date'] = pd.to_datetime(df['date'])#.dt.date
    df = df.sort_values(by='date')
    df['date'] = df['date'].dt.strftime('%d-%m-%Y')
    df = df.reset_index(drop=True)
    print(df.head())

except mysql.connector.Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if mydb.is_connected():
        mydb.close()
        cursor.close()
        print("MySQL connection is closed")