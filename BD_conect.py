import psycopg2
import json
from time import sleep
from datetime import datetime


# TODO: Separar os processos de banco de dados em outro arquivo FEITO!!
def db_connect():
    # TODO: Pegar os valores de um arquivo acessos.cfg ( usar: configparser.ConfigParser() )
    _host = "localhost"
    _port = 15432
    _user = "postgres"
    _pass = "postgres"

    return psycopg2.connect(host=_host, port=_port, user=_user, password=_pass)


def execute_query_insert(query):
    conn = db_connect()
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
    finally:
        conn.close()

# TODO: Criar metodo para consulta ao banco de dados
# def execute_query_select(query):

def consultar_db(sql):
  con = conecta_db()
  cur = con.cursor()
  cur.execute(sql)
  recset = cur.fetchall()
  registros = []
  for rec in recset:
    registros.append(rec)
  con.close()
  return registros


