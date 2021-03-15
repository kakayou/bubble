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
