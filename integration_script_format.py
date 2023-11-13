""" A format/sample of the integration script """

import requests as _requests # Do not use this directly

from requests_oauthlib import OAuth1
import json
import pandas as pd, pandas
import logging 
import abc
import datetime as dt, datetime

logging = logging.basicConfig(level=logging.DEBUG)

class AbstractIntegration(abc.ABC):

    def request(self, method, url, **kwargs):
        """ This has to be used to accomodate agent requests """
        return _requests.request(method, url, **kwargs, verify=self.contants["ssl_certificate_verification"])
        
    @abc.abstractmethod
    def update_asset(self, asset):
        """Update the integration fields of provided asset

            Arguments:
            asset -- Dictionary of asset fields with corr value over 0
            """
        
    @abc.abstractmethod
    def get_new_assets(self):
        """Return new assets

            Arguments:
            """
        
    @abc.abstractmethod
    def get_all_assets(self):
        """Return all assets to be added if they don't exist or updated if they do. 
            Only ran manually due to the possible issue with doing that.

            Arguments:
            """

class Integration(AbstractIntegration):

    constants = {"base_url":"", "ssl_certificate_verification":True, "integration_uid": "", "agent_uid": ""}
    headers = { 
        "User-Agent": "Asset Management",
        "Content-Type": "application/json",  
        "Accept": "application/json",
        }
    
    # OAUTH 1 Example:

    # OAUTH 2 Example:
    
    # Standard API Key Example:
    # def authenticate(self):
    #     self.headers["Api-Key"] = self.secure_token
    # def __init__(self):
    #     self.authenticate()

    # Basic Auth Example:
    # def request(self, *args, **kwargs):
    #     return super(self.__class__, self).request(*args, **kwargs, auth=(self.username, self.secure_token))


    
# Calling
Integration.username = ""
Integration.secure_token = ""
Integration.secure_additional = {} # This can be used to store additional OAUTH secrets
Integration.constants = {}

integration = Integration()
#integration.update_asset(asset)
