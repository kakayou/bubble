import logging
from apscheduler.schedulers.background import BackgroundScheduler
from django.http import HttpResponse
from django_apscheduler.jobstores import DjangoJobStore, register_job
from django.views.decorators.csrf import csrf_exempt

log = logging.getLogger('run')
scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), 'default')


@register_job(scheduler, 'cron', id='test', hour=10, minute='*/1', args=['test'])
def load(arg):
    print(arg)


@csrf_exempt
def start_job(request):
    request_method = request.META['REQUEST_METHOD']
    if request_method != 'POST':
        return HttpResponse(status=500)
    try:
        scheduler.start()
        return HttpResponse(status=200)
    except Exception as e:
        log.error('start job error: %s' % e)
    scheduler.start()
