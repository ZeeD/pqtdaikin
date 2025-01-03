# coding: utf-8

"""
    ONECTA Cloud API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.gateway_device_body import GatewayDeviceBody

class TestGatewayDeviceBody(unittest.TestCase):
    """GatewayDeviceBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GatewayDeviceBody:
        """Test GatewayDeviceBody
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GatewayDeviceBody`
        """
        model = GatewayDeviceBody()
        if include_optional:
            return GatewayDeviceBody(
                embedded_id = '123459999',
                device_model = 'Altherma'
            )
        else:
            return GatewayDeviceBody(
        )
        """

    def testGatewayDeviceBody(self):
        """Test GatewayDeviceBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
