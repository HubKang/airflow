import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
from common.common_func import regist

with DAG(
    dag_id="dags_python_with_op_args",
    schedule="0 2 * * *",
    start_date=pendulum.datetime(2024, 9, 23, tz="Asia/Seoul"),
    catchup=False,
    tags=["kang"]
) as dag:
    
    regist_t1 = PythonOperator(
        task_id = 'regist_t1',
        python_callable=regist,
        op_args = ['kjh','man','kr','seoul']
    )

    regist_t1
