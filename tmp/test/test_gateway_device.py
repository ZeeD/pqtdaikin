# coding: utf-8

"""
    ONECTA Cloud API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.gateway_device import GatewayDevice

class TestGatewayDevice(unittest.TestCase):
    """GatewayDevice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GatewayDevice:
        """Test GatewayDevice
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GatewayDevice`
        """
        model = GatewayDevice()
        if include_optional:
            return GatewayDevice(
                is_cloud_connection_up = openapi_client.models.boolean_characteristic.BooleanCharacteristic(),
                timestamp = '2018-11-13T20:20:39.000Z',
                mananagement_points = [
                    openapi_client.models.management_point.ManagementPoint(
                        embedded_id = '', 
                        management_point_type = 'gateway', 
                        management_point_sub_type = 'mainZone', 
                        management_point_category = 'primary', 
                        name = openapi_client.models.string_characteristic.StringCharacteristic(), 
                        on_off_mode = openapi_client.models.string_array_characteristic.StringArrayCharacteristic(), 
                        consumption_data = openapi_client.models.object_characteristic.ObjectCharacteristic(), 
                        ip_address = openapi_client.models.string_characteristic.StringCharacteristic(), 
                        mac_address = openapi_client.models.string_characteristic.StringCharacteristic(), 
                        firmware_version = openapi_client.models.string_characteristic.StringCharacteristic(), 
                        serial_number = openapi_client.models.string_characteristic.StringCharacteristic(), 
                        model_info = openapi_client.models.string_characteristic.StringCharacteristic(), 
                        software_version = openapi_client.models.string_characteristic.StringCharacteristic(), 
                        sensory_data = openapi_client.models.object_characteristic.ObjectCharacteristic(), 
                        control_mode = openapi_client.models.string_array_characteristic.StringArrayCharacteristic(), 
                        powerful_mode = openapi_client.models.string_array_characteristic.StringArrayCharacteristic(), 
                        operation_mode = openapi_client.models.string_array_characteristic.StringArrayCharacteristic(), 
                        temperature_control = openapi_client.models.object_characteristic.ObjectCharacteristic(), 
                        is_in_error_state = openapi_client.models.boolean_characteristic.BooleanCharacteristic(), 
                        is_in_warning_state = openapi_client.models.boolean_characteristic.BooleanCharacteristic(), 
                        is_in_caution_state = openapi_client.models.boolean_characteristic.BooleanCharacteristic(), 
                        is_in_installer_state = openapi_client.models.boolean_characteristic.BooleanCharacteristic(), 
                        is_in_emergency_state = openapi_client.models.boolean_characteristic.BooleanCharacteristic(), 
                        is_holiday_mode_active = openapi_client.models.boolean_characteristic.BooleanCharacteristic(), 
                        is_powerful_mode_active = openapi_client.models.boolean_characteristic.BooleanCharacteristic(), 
                        error_code = openapi_client.models.string_characteristic.StringCharacteristic(), 
                        schedule = openapi_client.models.object_characteristic.ObjectCharacteristic(), 
                        holiday_mode = openapi_client.models.object_characteristic.ObjectCharacteristic(), 
                        heatup_mode = openapi_client.models.string_array_characteristic.StringArrayCharacteristic(), 
                        setpoint_mode = openapi_client.models.string_array_characteristic.StringArrayCharacteristic(), 
                        fan_control = openapi_client.models.object_characteristic.ObjectCharacteristic(), 
                        humidity_control = openapi_client.models.object_characteristic.ObjectCharacteristic(), 
                        firmware_update = openapi_client.models.object_characteristic.ObjectCharacteristic(), 
                        firmware_update_status = openapi_client.models.string_array_characteristic.StringArrayCharacteristic(), )
                    ],
                id = '',
                embedded_id = '123459999',
                device_model = 'Altherma'
            )
        else:
            return GatewayDevice(
        )
        """

    def testGatewayDevice(self):
        """Test GatewayDevice"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
