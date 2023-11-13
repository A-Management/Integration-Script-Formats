""" A format/sample of the integration script """

import requests as _requests # Do not use this directly

import json
import pandas as pd, pandas
import logging 
import abc
import datetime as dt, datetime

logging = logging.basicConfig(level=logging.DEBUG)

class AbstractIntegration(abc.ABC):

    def request(self, method, url, **kwargs):
        """ This has to be used to accomodate agent requests """
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