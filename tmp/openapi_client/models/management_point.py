# coding: utf-8

"""
    ONECTA Cloud API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.boolean_characteristic import BooleanCharacteristic
from openapi_client.models.object_characteristic import ObjectCharacteristic
from openapi_client.models.string_array_characteristic import StringArrayCharacteristic
from openapi_client.models.string_characteristic import StringCharacteristic
from typing import Optional, Set
from typing_extensions import Self

class ManagementPoint(BaseModel):
    """
    ManagementPoint
    """ # noqa: E501
    embedded_id: Optional[StrictStr] = Field(default=None, description="The id of the embedded device, this id can contain a number or a string.", alias="embeddedId")
    management_point_type: Optional[StrictStr] = Field(default=None, description="The type of a management point", alias="managementPointType")
    management_point_sub_type: Optional[StrictStr] = Field(default=None, description="The sub type of a management point", alias="managementPointSubType")
    management_point_category: Optional[StrictStr] = Field(default=None, description="The category of a management point", alias="managementPointCategory")
    name: Optional[StringCharacteristic] = None
    on_off_mode: Optional[StringArrayCharacteristic] = Field(default=None, alias="onOffMode")
    consumption_data: Optional[ObjectCharacteristic] = Field(default=None, alias="consumptionData")
    ip_address: Optional[StringCharacteristic] = Field(default=None, alias="ipAddress")
    mac_address: Optional[StringCharacteristic] = Field(default=None, alias="macAddress")
    firmware_version: Optional[StringCharacteristic] = Field(default=None, alias="firmwareVersion")
    serial_number: Optional[StringCharacteristic] = Field(default=None, alias="serialNumber")
    model_info: Optional[StringCharacteristic] = Field(default=None, alias="modelInfo")
    software_version: Optional[StringCharacteristic] = Field(default=None, alias="softwareVersion")
    sensory_data: Optional[ObjectCharacteristic] = Field(default=None, alias="sensoryData")
    control_mode: Optional[StringArrayCharacteristic] = Field(default=None, alias="controlMode")
    powerful_mode: Optional[StringArrayCharacteristic] = Field(default=None, alias="powerfulMode")
    operation_mode: Optional[StringArrayCharacteristic] = Field(default=None, alias="operationMode")
    temperature_control: Optional[ObjectCharacteristic] = Field(default=None, alias="temperatureControl")
    is_in_error_state: Optional[BooleanCharacteristic] = Field(default=None, alias="isInErrorState")
    is_in_warning_state: Optional[BooleanCharacteristic] = Field(default=None, alias="isInWarningState")
    is_in_caution_state: Optional[BooleanCharacteristic] = Field(default=None, alias="isInCautionState")
    is_in_installer_state: Optional[BooleanCharacteristic] = Field(default=None, alias="isInInstallerState")
    is_in_emergency_state: Optional[BooleanCharacteristic] = Field(default=None, alias="isInEmergencyState")
    is_holiday_mode_active: Optional[BooleanCharacteristic] = Field(default=None, alias="isHolidayModeActive")
    is_powerful_mode_active: Optional[BooleanCharacteristic] = Field(default=None, alias="isPowerfulModeActive")
    error_code: Optional[StringCharacteristic] = Field(default=None, alias="errorCode")
    schedule: Optional[ObjectCharacteristic] = None
    holiday_mode: Optional[ObjectCharacteristic] = Field(default=None, alias="holidayMode")
    heatup_mode: Optional[StringArrayCharacteristic] = Field(default=None, alias="heatupMode")
    setpoint_mode: Optional[StringArrayCharacteristic] = Field(default=None, alias="setpointMode")
    fan_control: Optional[ObjectCharacteristic] = Field(default=None, alias="fanControl")
    humidity_control: Optional[ObjectCharacteristic] = Field(default=None, alias="humidityControl")
    firmware_update: Optional[ObjectCharacteristic] = Field(default=None, alias="firmwareUpdate")
    firmware_update_status: Optional[StringArrayCharacteristic] = Field(default=None, alias="firmwareUpdateStatus")
    __properties: ClassVar[List[str]] = ["embeddedId", "managementPointType", "managementPointSubType", "managementPointCategory", "name", "onOffMode", "consumptionData", "ipAddress", "macAddress", "firmwareVersion", "serialNumber", "modelInfo", "softwareVersion", "sensoryData", "controlMode", "powerfulMode", "operationMode", "temperatureControl", "isInErrorState", "isInWarningState", "isInCautionState", "isInInstallerState", "isInEmergencyState", "isHolidayModeActive", "isPowerfulModeActive", "errorCode", "schedule", "holidayMode", "heatupMode", "setpointMode", "fanControl", "humidityControl", "firmwareUpdate", "firmwareUpdateStatus"]

    @field_validator('management_point_type')
    def management_point_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['gateway', 'climateControl', 'domesticHotWaterFlowThrough', 'domesticHotWaterTank', 'indoorUnitHydro', 'outdoorUnit', 'userInterface']):
            raise ValueError("must be one of enum values ('gateway', 'climateControl', 'domesticHotWaterFlowThrough', 'domesticHotWaterTank', 'indoorUnitHydro', 'outdoorUnit', 'userInterface')")
        return value

    @field_validator('management_point_sub_type')
    def management_point_sub_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['mainZone', 'additonalZone']):
            raise ValueError("must be one of enum values ('mainZone', 'additonalZone')")
        return value

    @field_validator('management_point_category')
    def management_point_category_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['primary', 'secondary']):
            raise ValueError("must be one of enum values ('primary', 'secondary')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ManagementPoint from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of name
        if self.name:
            _dict['name'] = self.name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of on_off_mode
        if self.on_off_mode:
            _dict['onOffMode'] = self.on_off_mode.to_dict()
        # override the default output from pydantic by calling `to_dict()` of consumption_data
        if self.consumption_data:
            _dict['consumptionData'] = self.consumption_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ip_address
        if self.ip_address:
            _dict['ipAddress'] = self.ip_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mac_address
        if self.mac_address:
            _dict['macAddress'] = self.mac_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of firmware_version
        if self.firmware_version:
            _dict['firmwareVersion'] = self.firmware_version.to_dict()
        # override the default output from pydantic by calling `to_dict()` of serial_number
        if self.serial_number:
            _dict['serialNumber'] = self.serial_number.to_dict()
        # override the default output from pydantic by calling `to_dict()` of model_info
        if self.model_info:
            _dict['modelInfo'] = self.model_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of software_version
        if self.software_version:
            _dict['softwareVersion'] = self.software_version.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sensory_data
        if self.sensory_data:
            _dict['sensoryData'] = self.sensory_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of control_mode
        if self.control_mode:
            _dict['controlMode'] = self.control_mode.to_dict()
        # override the default output from pydantic by calling `to_dict()` of powerful_mode
        if self.powerful_mode:
            _dict['powerfulMode'] = self.powerful_mode.to_dict()
        # override the default output from pydantic by calling `to_dict()` of operation_mode
        if self.operation_mode:
            _dict['operationMode'] = self.operation_mode.to_dict()
        # override the default output from pydantic by calling `to_dict()` of temperature_control
        if self.temperature_control:
            _dict['temperatureControl'] = self.temperature_control.to_dict()
        # override the default output from pydantic by calling `to_dict()` of is_in_error_state
        if self.is_in_error_state:
            _dict['isInErrorState'] = self.is_in_error_state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of is_in_warning_state
        if self.is_in_warning_state:
            _dict['isInWarningState'] = self.is_in_warning_state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of is_in_caution_state
        if self.is_in_caution_state:
            _dict['isInCautionState'] = self.is_in_caution_state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of is_in_installer_state
        if self.is_in_installer_state:
            _dict['isInInstallerState'] = self.is_in_installer_state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of is_in_emergency_state
        if self.is_in_emergency_state:
            _dict['isInEmergencyState'] = self.is_in_emergency_state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of is_holiday_mode_active
        if self.is_holiday_mode_active:
            _dict['isHolidayModeActive'] = self.is_holiday_mode_active.to_dict()
        # override the default output from pydantic by calling `to_dict()` of is_powerful_mode_active
        if self.is_powerful_mode_active:
            _dict['isPowerfulModeActive'] = self.is_powerful_mode_active.to_dict()
        # override the default output from pydantic by calling `to_dict()` of error_code
        if self.error_code:
            _dict['errorCode'] = self.error_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of schedule
        if self.schedule:
            _dict['schedule'] = self.schedule.to_dict()
        # override the default output from pydantic by calling `to_dict()` of holiday_mode
        if self.holiday_mode:
            _dict['holidayMode'] = self.holiday_mode.to_dict()
        # override the default output from pydantic by calling `to_dict()` of heatup_mode
        if self.heatup_mode:
            _dict['heatupMode'] = self.heatup_mode.to_dict()
        # override the default output from pydantic by calling `to_dict()` of setpoint_mode
        if self.setpoint_mode:
            _dict['setpointMode'] = self.setpoint_mode.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fan_control
        if self.fan_control:
            _dict['fanControl'] = self.fan_control.to_dict()
        # override the default output from pydantic by calling `to_dict()` of humidity_control
        if self.humidity_control:
            _dict['humidityControl'] = self.humidity_control.to_dict()
        # override the default output from pydantic by calling `to_dict()` of firmware_update
        if self.firmware_update:
            _dict['firmwareUpdate'] = self.firmware_update.to_dict()
        # override the default output from pydantic by calling `to_dict()` of firmware_update_status
        if self.firmware_update_status:
            _dict['firmwareUpdateStatus'] = self.firmware_update_status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ManagementPoint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "embeddedId": obj.get("embeddedId"),
            "managementPointType": obj.get("managementPointType"),
            "managementPointSubType": obj.get("managementPointSubType"),
            "managementPointCategory": obj.get("managementPointCategory"),
            "name": StringCharacteristic.from_dict(obj["name"]) if obj.get("name") is not None else None,
            "onOffMode": StringArrayCharacteristic.from_dict(obj["onOffMode"]) if obj.get("onOffMode") is not None else None,
            "consumptionData": ObjectCharacteristic.from_dict(obj["consumptionData"]) if obj.get("consumptionData") is not None else None,
            "ipAddress": StringCharacteristic.from_dict(obj["ipAddress"]) if obj.get("ipAddress") is not None else None,
            "macAddress": StringCharacteristic.from_dict(obj["macAddress"]) if obj.get("macAddress") is not None else None,
            "firmwareVersion": StringCharacteristic.from_dict(obj["firmwareVersion"]) if obj.get("firmwareVersion") is not None else None,
            "serialNumber": StringCharacteristic.from_dict(obj["serialNumber"]) if obj.get("serialNumber") is not None else None,
            "modelInfo": StringCharacteristic.from_dict(obj["modelInfo"]) if obj.get("modelInfo") is not None else None,
            "softwareVersion": StringCharacteristic.from_dict(obj["softwareVersion"]) if obj.get("softwareVersion") is not None else None,
            "sensoryData": ObjectCharacteristic.from_dict(obj["sensoryData"]) if obj.get("sensoryData") is not None else None,
            "controlMode": StringArrayCharacteristic.from_dict(obj["controlMode"]) if obj.get("controlMode") is not None else None,
            "powerfulMode": StringArrayCharacteristic.from_dict(obj["powerfulMode"]) if obj.get("powerfulMode") is not None else None,
            "operationMode": StringArrayCharacteristic.from_dict(obj["operationMode"]) if obj.get("operationMode") is not None else None,
            "temperatureControl": ObjectCharacteristic.from_dict(obj["temperatureControl"]) if obj.get("temperatureControl") is not None else None,
            "isInErrorState": BooleanCharacteristic.from_dict(obj["isInErrorState"]) if obj.get("isInErrorState") is not None else None,
            "isInWarningState": BooleanCharacteristic.from_dict(obj["isInWarningState"]) if obj.get("isInWarningState") is not None else None,
            "isInCautionState": BooleanCharacteristic.from_dict(obj["isInCautionState"]) if obj.get("isInCautionState") is not None else None,
            "isInInstallerState": BooleanCharacteristic.from_dict(obj["isInInstallerState"]) if obj.get("isInInstallerState") is not None else None,
            "isInEmergencyState": BooleanCharacteristic.from_dict(obj["isInEmergencyState"]) if obj.get("isInEmergencyState") is not None else None,
            "isHolidayModeActive": BooleanCharacteristic.from_dict(obj["isHolidayModeActive"]) if obj.get("isHolidayModeActive") is not None else None,
            "isPowerfulModeActive": BooleanCharacteristic.from_dict(obj["isPowerfulModeActive"]) if obj.get("isPowerfulModeActive") is not None else None,
            "errorCode": StringCharacteristic.from_dict(obj["errorCode"]) if obj.get("errorCode") is not None else None,
            "schedule": ObjectCharacteristic.from_dict(obj["schedule"]) if obj.get("schedule") is not None else None,
            "holidayMode": ObjectCharacteristic.from_dict(obj["holidayMode"]) if obj.get("holidayMode") is not None else None,
            "heatupMode": StringArrayCharacteristic.from_dict(obj["heatupMode"]) if obj.get("heatupMode") is not None else None,
            "setpointMode": StringArrayCharacteristic.from_dict(obj["setpointMode"]) if obj.get("setpointMode") is not None else None,
            "fanControl": ObjectCharacteristic.from_dict(obj["fanControl"]) if obj.get("fanControl") is not None else None,
            "humidityControl": ObjectCharacteristic.from_dict(obj["humidityControl"]) if obj.get("humidityControl") is not None else None,
            "firmwareUpdate": ObjectCharacteristic.from_dict(obj["firmwareUpdate"]) if obj.get("firmwareUpdate") is not None else None,
            "firmwareUpdateStatus": StringArrayCharacteristic.from_dict(obj["firmwareUpdateStatus"]) if obj.get("firmwareUpdateStatus") is not None else None
        })
        return _obj

