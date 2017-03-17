import logging
import yaml
import urllib2
from urllib import urlencode
import os.path

logger = logging.getLogger(__name__)

class Process:

    def __init__(self, project_config, project_yml):
        self._project_config = project_config
        self._project_yml = project_yml

    def process(self):
        logger.info('Implement business logic')
        with open(self._project_yml, 'r') as stream:
		    data_loaded = yaml.load(stream)
        logger.info('urltoload=' + data_loaded.get('service').get('api_url'))
		
        apitoread = data_loaded.get('service').get('api_url')
        countryinfo = data_loaded.get('configuration').get(self._project_config)
        logger.info('countryinfo=' + data_loaded.get('configuration'))

        for city in countryinfo.get('cities'):
        	logger.info('cityname=' + city)
        	filename = city + '.csv'
        	if os.path.exists(filename):
                logger.info('Calling API')
                _parameters = 'q=' + city + '&key=92f88c62ac9c497dac1221747171703'
                urltoread = apitoread + "?" + urlencode(_parameters);
        		weather_data = urllib2.urlopen(urltoread  ).read()

        		f = open(filename, 'w')
        		f.write(weather_data)
