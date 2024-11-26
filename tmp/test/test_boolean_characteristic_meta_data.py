# coding: utf-8

"""
    ONECTA Cloud API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.boolean_characteristic_meta_data import BooleanCharacteristicMetaData

class TestBooleanCharacteristicMetaData(unittest.TestCase):
    """BooleanCharacteristicMetaData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BooleanCharacteristicMetaData:
        """Test BooleanCharacteristicMetaData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BooleanCharacteristicMetaData`
        """
        model = BooleanCharacteristicMetaData()
        if include_optional:
            return BooleanCharacteristicMetaData(
                error = 'INVALID_CHARACTERISTIC',
                settable = True,
                deprecated = '',
                value = True
            )
        else:
            return BooleanCharacteristicMetaData(
        )
        """

    def testBooleanCharacteristicMetaData(self):
        """Test BooleanCharacteristicMetaData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()