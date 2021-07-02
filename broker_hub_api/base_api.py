import json
import logging
from urllib.parse import urljoin

import requests

from broker_hub_api import exceptions, helpers

log = logging.getLogger(__name__)


class CommonBrokerHubApi:
    def __init__(self, domain, access_key, secret_key, api_version='1'):
        self.api_url = 'https://{api_domain}/api/v{api_version}/'.format(api_domain=domain, api_version=api_version)
        self.access_key = access_key
        self.secret_key = secret_key

    def _request(self, url, method, data, headers=None):
        """
        :param url: request url
        :param method: request method, POST | GET
        :param data: request data
        :param headers: request headers
        :return: api response
        """
        log.debug('URL: %s' % url)
        log.debug('Data: %s' % str(data))
        log.debug('Headers: %s' % str(headers))

        response = requests.request(method, url, data=data, headers=headers)
        return self._response(response, response.content.decode('utf-8'))

    def _response(self, response, content):
        """
        :param response: api response
        :param content: api response body
        :return: if response header 200 or 201 return response data
        """
        status = response.status_code

        log.debug('Status: %s' % str(status))
        log.debug('Content: %s' % content)

        if content:
            content = json.loads(content)
        else:
            content = dict()

        if status in (200, 201):
            return content

        raise exceptions.ServiceError(status, response_data=content)

    def post(self, url, data: dict, headers=None):
        """
        :param url: endpoint api url
        :param data: request data
        :param headers: request headers
        :return: dict of data response
        """
        headers = dict() if headers is None else headers
        headers.update({
            'Content-Type': 'application/json; charset=utf-8',
        })

        if 'access_key' not in data:
            data['access_key'] = self.access_key
        if 'signature' not in data:
            data['signature'] = helpers.get_signature(self.secret_key, data)

        data_string = json.dumps(data)

        return self._request(
            urljoin(self.api_url, url),
            'POST',
            data=data_string,
            headers=headers
        )
