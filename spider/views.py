import logging
from apscheduler.schedulers.background import BackgroundScheduler
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datas.views import latest_term

log = logging.getLogger('run')
scheduler = BackgroundScheduler()


def load():
    start = "00001"
    term = latest_term()
    log.info("the latest term in db is %s" % term)
    # end = latest_term()
    # log.info("the latest term is %s" % end)

    # if int(end) > term[0]:
    #     start = term[0]
    #     data = crawler.crawler_data(str(start + 1), end)
    #     print(data)
    #     db.t_facility_insert(data)


@csrf_exempt
def start_job(request):
    request_method = request.META['REQUEST_METHOD']
    if request_method != 'GET':
        return HttpResponse(status=500)
    try:
        scheduler.add_job(load, 'interval', seconds=30)
        scheduler.start()
        return HttpResponse(status=200)
    except Exception as e:
        log.error('start job error: %s' % e)
    scheduler.start()
