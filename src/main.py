from src.core.logger import logger


import requests

logger.info("Hi")
logger.debug("hello")

url = "https://www.google.com"
requests.get(url)