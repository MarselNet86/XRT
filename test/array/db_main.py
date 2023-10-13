import asyncpg
from os import getenv
from dotenv import load_dotenv
from datetime import datetime


async def connect_db() -> asyncpg.Connection:
    load_dotenv(r'C:\Users\scham\OneDrive\Рабочий стол\AiogramTemplate-main\bot\misc\.env')
    connection = await asyncpg.connect(
        user=getenv('DB_USER'),
        password=getenv('DB_PASSWORD'),
        database=getenv('DB_NAME'),
        host=getenv('DB_HOST')
        )
    return connection


async def create_table() -> None:
    connection = await connect_db()
    async with connection.transaction():
        await connection.execute('''      
            CREATE TABLE IF NOT EXISTS data_table (
                crm text,
                worksite_short_name text,
                assignee_name varchar,
                open_date timestamp,
                create_ki timestamp,
                start_ki timestamp,
                stop_ki timestamp,
                close_ki timestamp,
                ks_3 timestamp,
                ks_23 timestamp,
                interval varchar,
                status_fk int REFERENCES statuses(id),
                status_time interval,
                commentary text,
                login text,
                date_close timestamp,
                request_time timestamp
            );   
            ''')
        print('[INFO] Table created successfully')


async def get_array_data():
    connection = await connect_db()
    async with connection.transaction():
        data = await connection.fetch('SELECT * FROM data_table')

        return data


async def insert_new_array(data) -> None:
    connection = await connect_db()
    async with connection.transaction():
        await connection.execute(
            '''
            INSERT INTO data_table (
            crm, worksite_short_name, assignee_name, 
            open_date, create_ki, start_ki, stop_ki, 
            close_ki, ks_3, ks_23, interval, status, 
            status_time, commentary, login, date_close, request_time
            ) 
            VALUES (
            $1, $2, $3, $4, $5, $6, $7, $8, $9, 
            $10, $11, $12, $13, $14, $15, $16, $17
            )
            ''',
            data['CRM'], data['WORKSITE_SHORT_NAME'], data['ASSIGNEE_NAME'],
            data.get('OPEN_DATE'), data.get('CREATE_KI'), data.get('START_KI'),
            data.get('STOP_KI'), data.get('CLOSE_KI'), data.get('KS_3'), data['KS_23'],
            data['INTERVAL'], data['STATUS'], data.get('STATUS_TIME'), data['COMMENTARY'],
            data['LOGIN'], data.get('DATE_CLOSE'), data['REQUEST_TIME']
        )


async def change_array(data) -> None:
    connection = await connect_db()
    async with connection.transaction():
        await connection.execute(
            '''
            UPDATE data_table SET worksite_short_name = $1, assignee_name = $2, close_ki = $3 WHERE crm = $4
            ''',
            data['WORKSITE_SHORT_NAME'], data['ASSIGNEE_NAME'],
            data.get('CLOSE_KI'), data['CRM']
        )
