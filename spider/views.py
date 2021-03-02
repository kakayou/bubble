from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_job

# 实例化调度器
scheduler = BackgroundScheduler()
# 调度器使用默认的DjangoJobStore()
scheduler.add_jobstore(DjangoJobStore(), 'default')


# 每天8点半执行这个任务
@register_job(scheduler, 'cron', id='test', hour=8, minute=30, args=['test'])
def load():
    # 具体要执行的代码
    pass


scheduler.start()
