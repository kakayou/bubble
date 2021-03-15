import logging

from django.db.models import Max
from django.shortcuts import render

from datas import models

log = logging.getLogger('run')


def latest_term():
    max_term = models.History.objects.all().aggregate(Max("term"))
    return max_term


def save_history(history_terms):
    length = len(history_terms)
    if length > 0:
        data_list = list()
        try:
            for i in range(length):
                data_list.append(models.History(term=history_terms["term"],
                                                red1=history_terms["red1"],
                                                red2=history_terms["red2"],
                                                red3=history_terms["red3"],
                                                red4=history_terms["red4"],
                                                red5=history_terms["red5"],
                                                red6=history_terms["red6"]))
                models.History.objects.bulk_create(data_list)
        except Exception as e:
            log.error("save history term error %s" % e)
