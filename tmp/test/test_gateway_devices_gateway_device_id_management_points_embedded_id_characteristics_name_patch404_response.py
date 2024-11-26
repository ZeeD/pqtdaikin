# coding: utf-8

"""
    ONECTA Cloud API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.gateway_devices_gateway_device_id_management_points_embedded_id_characteristics_name_patch404_response import GatewayDevicesGatewayDeviceIdManagementPointsEmbeddedIdCharacteristicsNamePatch404Response

class TestGatewayDevicesGatewayDeviceIdManagementPointsEmbeddedIdCharacteristicsNamePatch404Response(unittest.TestCase):
    """GatewayDevicesGatewayDeviceIdManagementPointsEmbeddedIdCharacteristicsNamePatch404Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GatewayDevicesGatewayDeviceIdManagementPointsEmbeddedIdCharacteristicsNamePatch404Response:
        """Test GatewayDevicesGatewayDeviceIdManagementPointsEmbeddedIdCharacteristicsNamePatch404Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GatewayDevicesGatewayDeviceIdManagementPointsEmbeddedIdCharacteristicsNamePatch404Response`
        """
        model = GatewayDevicesGatewayDeviceIdManagementPointsEmbeddedIdCharacteristicsNamePatch404Response()
        if include_optional:
            return GatewayDevicesGatewayDeviceIdManagementPointsEmbeddedIdCharacteristicsNamePatch404Response(
                code = 'GATEWAY_DEVICE_MISSING',
                message = ''
            )
        else:
            return GatewayDevicesGatewayDeviceIdManagementPointsEmbeddedIdCharacteristicsNamePatch404Response(
                code = 'GATEWAY_DEVICE_MISSING',
                message = '',
        )
        """

    def testGatewayDevicesGatewayDeviceIdManagementPointsEmbeddedIdCharacteristicsNamePatch404Response(self):
        """Test GatewayDevicesGatewayDeviceIdManagementPointsEmbeddedIdCharacteristicsNamePatch404Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
