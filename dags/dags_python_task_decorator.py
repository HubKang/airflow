import pendulum
from airflow import DAG
from airflow.decorators import task


with DAG(
    dag_id="dags_python_task_decorator",
    schedule="0 2 * * *",
    start_date=pendulum.datetime(2024, 9, 23, tz="Asia/Seoul"),
    catchup=False,
    tags=["kang"],
):
    # [START howto_operator_python]
    @task(task_id="python_task_1")
    def print_context(some_input):
        print(some_input)

    python_task_1 = print_context('task decorator 실행')
    # [END howto_operator_python]