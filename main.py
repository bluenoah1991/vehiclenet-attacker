# Create by CodeMeow

# -*- coding:utf-8 -*- 

import urllib2

import sys
reload(sys)
sys.setdefaultencoding('utf8')

WEATHER_URI = 'http://vehiclenet-python-0-codemeow.myalauda.cn/carlink/weather/findWeather.htm?city=%s'

def fetch_weather(city_name):
    print 'Try to fetch the weather in %s' % city_name
    try:
        #import pdb
        #pdb.set_trace()
        city_encode_name = city_name.encode('utf-8')
        city_encode_name = urllib2.quote(city_encode_name)
        response = urllib2.urlopen(WEATHER_URI % city_encode_name)
        content = response.read()
        if content == str(201) or content == str(501):
            print 'Return error code: %s (%s)' % (content, city_name)
        return 1
    except urllib2.HTTPError, e:
        print 'Error: %s (%s)' % (e.code, city_name)
    finally:
        return 0

if __name__ == '__main__':
    #import pdb
    #pdb.set_trace()
    print 'Begin read \'city_name.txt\' file'
    f = open('city_name.txt', 'r')
    i_total = 0
    i_success = 0
    for line in f.readlines():
        line = line.strip()
        line = line.decode('unicode_escape')
        if not len(line) or line.startswith('#'):
            continue
        i_success += fetch_weather(line)
        i_total += 1
    print 'Finished (Total: %s, Success: %s)' % (i_total, i_success)
    f.close()