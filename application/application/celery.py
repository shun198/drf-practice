import os

from celery import Celery
from celery.schedules import crontab

"""環境変数を設定"""
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "ag_smile_leaseback_crm_back.settings.dev"
)

"""Celeryをdjango.conf:settingsに設定"""
app = Celery("application")
app.config_from_object("django.conf:settings", namespace="CELERY")

"""登録された全てのDjangoアプリからタスクモジュールをロード"""
app.autodiscover_tasks()

"""tasks.pyから実行するメソッドをスケジューラに設定"""
app.conf.beat_schedule = {
    "print_task": {
        "task": "application.tasks.print_task",
        "schedule": crontab(hour="*/1"),
    },
}