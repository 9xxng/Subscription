import requests
import mysql.connector

# 공공데이터 API 호출
api_url = "https://api.example.com/data"  # 공공데이터 API URL
response = requests.get(api_url)
data = response.json()

# MySQL 데이터베이스 연결
db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="public_data"
)

cursor = db.cursor()

# API 데이터 MySQL에 삽입
for item in data['items']:
    field1 = item['field1']
    field2 = item['field2']
    field3 = item['field3']

    query = "INSERT INTO api_data (data_field1, data_field2, data_field3) VALUES (%s, %s, %s)"
    values = (field1, field2, field3)
    
    cursor.execute(query, values)

db.commit()
cursor.close()
db.close()
