from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Default settings for the DAG
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

# Define the DAG
with DAG(
    dag_id='weather_data_pipeline',
    default_args=default_args,
    start_date=datetime(2025, 5, 2),
    schedule_interval=None,  # manually trigger
    catchup=False
) as dag:

    # Task 1: Data Collection (dummy for now)
    collect_data = BashOperator(
        task_id='collect_data',
        bash_command='echo "✅ Data collected!"'
    )

    # Task 2: Data Preprocessing
    preprocess_data = BashOperator(
        task_id='preprocess_data',
        bash_command='python C:\Users\Admin\Desktop\mlops-ass3\mlops_assignment3\data\processed_data.py'
    )

    # Task sequence
    collect_data >> preprocess_data
