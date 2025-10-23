# project_b/app/tasks.py
from celery import shared_task

@shared_task
def process_user_data(data):
    print(f"Received: {data}")
