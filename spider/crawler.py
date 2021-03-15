import logging

import requests
from django.db.models import Max
from lxml import etree
from datas import models

log = logging.getLogger('run')


def latest_term():
    url = "http://datachart.500.com/ssq"
    response = requests.get(url)
    response = response.text
    selector = etree.HTML(response)
    end = selector.xpath('//input[@name="to"]/@value')[0]
    return end


def crawler_data(start, end):
    data = list()
    url = "http://datachart.500.com/ssq/history/newinc/history.php?start=" + start + "&end=" + end
    response = requests.get(url)
    response = response.text
    selector = etree.HTML(response)
    for i in selector.xpath('//tr[@class="t_tr1"]'):
        term = i.xpath('td/text()')[0]
        red = i.xpath('td/text()')[1:7]
        blue = i.xpath('td/text()')[7]
        row = (int(term), int(red[0]), int(red[1]), int(red[2]), int(red[3]), int(red[4]), int(red[5]), int(blue))
        data.append(row)
    return data


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


def get_last_term():
    max_term = models.History.objects.all().aggregate(Max("term"))
    return max_term
