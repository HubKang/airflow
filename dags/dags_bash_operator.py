from __future__ import annotations
import datetime
import pendulum
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

# DAG 설정
with DAG(
    dag_id="example_bash_operator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2024, 9, 20, tz="Asia/Seoul"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["example", "example2"],
    params={"example_key": "example_value"},
) as dag:

    # task 생성1
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo who am i",
    )

    # task 생성2
    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )

    # task의 수행 순서
    bash_t1 >> bash_t2
