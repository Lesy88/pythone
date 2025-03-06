import sqlalchemy
print(sqlalchemy.__version__)

import psycopg2
print(psycopg2.__version__)


from sqlalchemy import create_engine, text 
from sqlalchemy import create_engine

# Connessione al database
engine = create_engine("mysql+mysqlconnector://root:root@localhost/crm_its")

# Connessione diretta al database per eseguire una query SQL
with engine.connect() as connection:
    # Usa il metodo 'text' per eseguire una query SQL
    result = connection.execute(text("SELECT * FROM studenti"))

    # Stampa i risultati
    for row in result:
        print(row)