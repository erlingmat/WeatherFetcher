import logging
import yaml
import urllib
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
		
        urltoread = data_loaded.get('service').get('api_url')
        countryinfo = data_loaded.get('configuration').get(self._project_config)
        logger.info('countryinfo=' + data_loaded.get('configuration'))
        for city in countryinfo.get('cities'):
        	logger.info('cityname=' + city)
        	filename = city + '.csv'
        	if os.path.exists(filename):
        		weather_data = urllib.urlopen(urltoread + "?q=" + city).read()
        		f = open(filename, 'w')
        		f.write(weather_data)
