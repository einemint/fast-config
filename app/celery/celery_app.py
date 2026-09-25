from celery import Celery

celery_app = Celery(
    "worker",
    broker= "",
    backend= "",
    include=[""]
)

celery_app.conf.update(
    task_track_started=True,
    task_time_limit=3600,
    worker_prefetch_multiplier=1,
    timezone="UTC",
    enable_utc=True,
)