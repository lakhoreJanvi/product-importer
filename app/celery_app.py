from celery import Celery
import os
from dotenv import load_dotenv

load_dotenv()

broker = os.getenv('CELERY_BROKER_URL', 'redis://redis:6379/1')
backend = os.getenv('CELERY_RESULT_BACKEND', 'redis://redis:6379/2')

celery = Celery(
    "product_importer",
    broker=broker,
    backend=backend,
    include=["app.tasks"]
)

celery.conf.task_routes = {
    "app.tasks.*": {"queue": "import_queue"},
}

celery.autodiscover_tasks(["app"])
