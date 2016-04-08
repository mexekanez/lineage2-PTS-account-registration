import pymssql

from lineage.utils import encrypt

MSSQL_HOST = ""
MSSQL_USER = ""
MSSQL_PASSWORD = ""

LIN2DB_NAME = "lin2db"
LIN2WORLD_NAME = "lin2world"

try:
    from local_settings import *
except Exception:
    print "Ubnable to find conf file"

def check_account(username, email, phone):
    output = {}
    with pymssql.connect(MSSQL_HOST, MSSQL_USER, MSSQL_PASSWORD, LIN2DB_NAME) as conn:
        with conn.cursor(as_dict=True) as cursor:
            cursor.execute('SELECT account FROM user_account WHERE account = %s', username)
            if cursor.fetchone():
                output['account']='Account already exists'
            cursor.execute('SELECT email FROM ssn WHERE email = %s', email)
            if cursor.fetchone():
                output['email']='Email already exists'
            cursor.execute('SELECT phone FROM ssn WHERE phone = %s', phone)
            if cursor.fetchone():
                output['phone']='Phone number already exists'
            return output

def add_account(account,password):
    # return encrypt(password)
    with pymssql.connect(MSSQL_HOST, MSSQL_USER, MSSQL_PASSWORD, LIN2DB_NAME) as conn:
        query = 'INSERT INTO user_auth (account,password,quiz1,quiz2,answer1,answer2) VALUES ({account},{password},{q1},{q2},{a1},{a2})'\
            .format(account='%s',password=encrypt(password),q1='%s',q2='%s',a1=encrypt(password),a2=encrypt(password))
        with conn.cursor() as cursor:
            cursor.execute(query,(account,'question1','question2'))
            # print cursor.tosql()
            conn.commit()

def add_ssn(ssn,name,email,phone):
    with pymssql.connect(MSSQL_HOST, MSSQL_USER, MSSQL_PASSWORD, LIN2DB_NAME) as conn:
        with conn.cursor() as cursor:
            cursor.execute('INSERT INTO ssn (ssn,name,email,job,phone,zip,addr_main,addr_etc,account_num) VALUES (%s,%s,%s,0,%s,12345,3 ,3 ,1)', (ssn,name,email,phone))
            conn.commit()


def add_user_info(account,ssn):
    with pymssql.connect(MSSQL_HOST, MSSQL_USER, MSSQL_PASSWORD, LIN2DB_NAME) as conn:
        with conn.cursor() as cursor:
            cursor.execute('INSERT INTO user_info (account,ssn,kind) VALUES (%s,%s, 99)', (account,ssn))
            conn.commit()

def add_user_account(account):
    with pymssql.connect(MSSQL_HOST, MSSQL_USER, MSSQL_PASSWORD, LIN2DB_NAME) as conn:
        with conn.cursor() as cursor:
            cursor.execute('INSERT INTO user_account (account, pay_stat) VALUES (%s, 1)', account)
            conn.commit()