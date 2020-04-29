# coding: utf-8

"""
    Synonyms API

    Retrieves the sets of synonyms for a given word.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.probes_api import ProbesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestProbesApi(unittest.TestCase):
    """ProbesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.probes_api.ProbesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_liveness(self):
        """Test case for get_liveness

        """
        pass

    def test_get_readiness(self):
        """Test case for get_readiness

        """
        pass


if __name__ == '__main__':
    unittest.main()
