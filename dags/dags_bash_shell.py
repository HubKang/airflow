import datetime
import pendulum
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

# DAG 설정
with DAG(
    dag_id="dags_bash_shell",
    schedule="10 0 * * *",
    start_date=pendulum.datetime(2024, 9, 1, tz="Asia/Seoul"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["example", "kang"]
) as dag:

    # task 생성1
    shell_t1 = BashOperator(
        task_id="shell_t1",
        bash_command="opt/airflow/plugins/shell/test.sh KJH",
    )

    # task 생성2
    shell_t2 = BashOperator(
        task_id="shell_t2",
        bash_command="opt/airflow/plugins/shell/test.sh Win!",
    )

    # task의 수행 순서
    shell_t1 >> shell_t2
