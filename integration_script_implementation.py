""" A format/sample of the integration script """

########
# PREP #
########


# Put these on seperate files so its not in scope
import requests as _requests 
import hashlib 


# These are in scope
from requests_oauthlib import OAuth1
import json
import pandas as pd, pandas
import logging 
import abc
import datetime as dt, datetime

from assets.custom_logging import get_logger

level = logging.DEBUG
logging = get_logger(level=level, add_file_handler=False)
#logging = get_logger(file=f"{os.path.dirname(__file__)}/logs/{os.path.basename(__file__)}.log", level=level)
#Use snmp log handler in future? 

class AbstractIntegration(abc.ABC):

    def agent_request(self, method="POST", url_addition = "/call", data=""):
        agent_headers = {"Api-Key": self.AGENT_API_KEY, "Token": hashlib.sha512(datetime.utcnow().strftime("%Y-%m-%d").encode()).hexdigest()}
        resp = _requests.request(method=method, url=self.AGENT_BASE_URL + url_addition, headers=agent_headers, data=data)
        return resp

    def request(self, method, url, **kwargs):
        if self.contants["agent_uid"].strip == "":
            try:
                if self.contants["ssl_certificate_verification"] == "ALWAYS" or self.contants["ssl_certificate_verification"] == "TRY_FIRST":
                    return _requests.request(method, url, **kwargs, verify=True)
                elif self.contants["ssl_certificate_verification"] == "NEVER":
                    return _requests.request(method, url, **kwargs, verify=False)
            except _requests.exceptions.SSLError as e:
                if self.contants["ssl_certificate_verification"] == "TRY_FIRST":
                    return _requests.request(method, url, **kwargs, verify=False)
                else:
                    raise e
        else:
            data = {
                "method": method,
                "url": url,
                "verify_setting": self.contants["ssl_certificate_verification"],
                **kwargs
            }
            return self.agent_request(data=json.dumps(data))
        
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

# Integration Format #

class Integration(AbstractIntegration):

    constants = {"base_url":"", "ssl_certificate_verification":"", "integration_uid": "", "agent_uid": ""}
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



# Maybe?
fields = {
        "app_UID": "", "main_IP": "", "IPs": [], "main_name": "", "names": [], "main_MAC": "", "MACs": [],
        "main_user": "", "users": [], "service_tag": "", "agent": False, "site": "", "groups": [], "tags": [], 
        "last_checked_in": "", "first_found": "", "asset_page_url": "", "connection_type": "", "OS": "", 
        "version": "", "category": ""
        }

