#o controller é responsavel por todas as minhas funções
# agora pra puxar pra dag, só uso o controller
from airflow.decorators import dag, task
from include.controller import gerar_numero_aleatorio, fetch_pokemon_data, add_pokemon_to_db

from datetime import datetime


# não quero nenhuma logica de negocio aqui, quero 
# quero que essa função externa seja chamada na task
# criar a dag


@dag(
        dag_id='api_postgres',
        description='pipeline para capturar pokemon',
        schedule='* * * * *',
        start_date=datetime(2025,3,15),
        catchup=False
)

def api_postgres():
    

    @task(task_id='gerar_numero_aleatorio')
    def task_gerar_numero_aleatorio():
        return gerar_numero_aleatorio()
    
    @task(task_id='fetch_pokemon_data')
    def task_fetch_pokemon_data():
        return fetch_pokemon_data()
    
    @task(task_id='add_pokemon_to_db')
    def task_add_pokemon_to_db():
        return add_pokemon_to_db()
    
    t1 = task_gerar_numero_aleatorio
    t2 = task_fetch_pokemon_data
    t3 = task_add_pokemon_to_db

    t1 >> t2 >> t3

api_postgres()