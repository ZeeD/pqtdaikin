# coding: utf-8

"""
    ONECTA Cloud API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.sites_inner import SitesInner

class TestSitesInner(unittest.TestCase):
    """SitesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SitesInner:
        """Test SitesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SitesInner`
        """
        model = SitesInner()
        if include_optional:
            return SitesInner(
                gateway_devices = [
                    ''
                    ],
                id = '',
                name = '',
                role = 'user',
                location = openapi_client.models.site_body_location.SiteBody_location(
                    country_code = '', 
                    place_id = '', 
                    latitude = 1.337, 
                    longitude = 1.337, 
                    level = 'coordinates', ),
                users = [
                    openapi_client.models.site_body_users_inner.SiteBody_users_inner(
                        id = '', 
                        role = 'user', )
                    ]
            )
        else:
            return SitesInner(
        )
        """

    def testSitesInner(self):
        """Test SitesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
