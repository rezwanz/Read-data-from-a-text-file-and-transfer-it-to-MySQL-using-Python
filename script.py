import pandas as pd
import mysql.connector
import schedule
import time

# Function to read data from a CSV file and insert into MySQL database
def insert_data():
    # Replace 'your_file.csv' with the actual path to your CSV file
    file_path = 'D:\\xampp\\htdocs\\Python\\sample.csv'
    
    # Read data from the CSV file using pandas
    df = pd.read_csv(file_path)
    
    # MySQL database connection parameters
    db_host = 'localhost'
    db_user = 'root'
    db_password = ''
    db_port = '3306'
    db_name = 'test_python'
    
    # Connect to MySQL database
    connection = mysql.connector.connect(host=db_host, user=db_user, password=db_password, port=db_port, database=db_name)
    
    # Create a MySQL cursor
    cursor = connection.cursor()
    
    # Iterate through rows in the DataFrame and insert into MySQL table
    for index, row in df.iterrows():
        # Assuming your table has columns 'identifier', 'first_name', 'last_name'
        query = "INSERT INTO txt_data (identifier, first_name, last_name) VALUES (%s, %s, %s)"
        values = (row['identifier'], row['first_name'], row['last_name'])
        
        cursor.execute(query, values)
    
    # Commit the changes
    connection.commit()
    
    # Close the cursor and connection
    cursor.close()
    connection.close()

# Schedule the script to run every 5 minutes
schedule.every(5).minutes.do(insert_data)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)