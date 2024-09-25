import datetime
import pendulum
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
# from plugins.common.common_func import get_sftp     #DAG 개발시 인식하는 paht
from common.common_func import get_sftp               #airflow 가 인식하는 path

# DAG 설정
with DAG(
    dag_id="dags_python_import_func",
    schedule="10 6 * * *",s
    start_date=pendulum.datetime(2024, 9, 23, tz="Asia/Seoul"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["example", "kang"]
) as dag:
    
    task_get_sftp = PythonOperator(
        task_id = 'task_get_sftp',
        python_callable=get_sftp
    )

    