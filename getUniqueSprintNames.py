import configparser
import logging
import pandas as pd
config = configparser.RawConfigParser()
config.read('config.properties')

logging.basicConfig(filename='log/example.log', encoding='utf-8', level=logging.DEBUG)
logging.info(config.get('DatabaseSection', 'database.dbname'))


df = pd.read_csv (r'C:\Users\maurice.saliba\OneDrive - GO PLC\MANAGEMENT\JIRA\datascraper\INPUT FILES\APIC-26-CERUPG-261.csv')


