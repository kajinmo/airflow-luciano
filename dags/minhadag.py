from time import sleep
from airflow.decorators import dag, task
from datetime import datetime

@dag(
        dag_id='minha_primeira_dag',
        description='minha etl braba',
        schedule='* * * * *',
        start_date=datetime(2025,3,13),
        catchup=False
)

def pipeline():
    @task
    def primeira_msg():
        print("minha primeira dag")
        sleep(2)
    
    @task
    def segunda_msg():
        print("minha segunda dag")
        sleep(2)

    @task          
    def terceira_msg():
        print("minha terceira dag")
        sleep(2)
    
    @task
    def quarta_msg():
        print('dag finalizada')
    
    t1 = primeira_msg()
    t2 = segunda_msg()
    t3 = terceira_msg()
    t4 = quarta_msg()
    
    t1 >> t2 >> t3 >> t4

