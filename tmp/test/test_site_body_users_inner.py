# coding: utf-8

"""
    ONECTA Cloud API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.site_body_users_inner import SiteBodyUsersInner

class TestSiteBodyUsersInner(unittest.TestCase):
    """SiteBodyUsersInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SiteBodyUsersInner:
        """Test SiteBodyUsersInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SiteBodyUsersInner`
        """
        model = SiteBodyUsersInner()
        if include_optional:
            return SiteBodyUsersInner(
                id = '',
                role = 'user'
            )
        else:
            return SiteBodyUsersInner(
        )
        """

    def testSiteBodyUsersInner(self):
        """Test SiteBodyUsersInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
