# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ContextTagKeys(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The context tag keys."""

    AI_APPLICATION_VER = "ai.application.ver"
    AI_DEVICE_ID = "ai.device.id"
    AI_DEVICE_LOCALE = "ai.device.locale"
    AI_DEVICE_MODEL = "ai.device.model"
    AI_DEVICE_OEM_NAME = "ai.device.oemName"
    AI_DEVICE_OS_VERSION = "ai.device.osVersion"
    AI_DEVICE_TYPE = "ai.device.type"
    AI_LOCATION_IP = "ai.location.ip"
    AI_LOCATION_COUNTRY = "ai.location.country"
    AI_LOCATION_PROVINCE = "ai.location.province"
    AI_LOCATION_CITY = "ai.location.city"
    AI_OPERATION_ID = "ai.operation.id"
    AI_OPERATION_NAME = "ai.operation.name"
    AI_OPERATION_PARENT_ID = "ai.operation.parentId"
    AI_OPERATION_SYNTHETIC_SOURCE = "ai.operation.syntheticSource"
    AI_OPERATION_CORRELATION_VECTOR = "ai.operation.correlationVector"
    AI_SESSION_ID = "ai.session.id"
    AI_SESSION_IS_FIRST = "ai.session.isFirst"
    AI_USER_ACCOUNT_ID = "ai.user.accountId"
    AI_USER_ID = "ai.user.id"
    AI_USER_AUTH_USER_ID = "ai.user.authUserId"
    AI_CLOUD_ROLE = "ai.cloud.role"
    AI_CLOUD_ROLE_VER = "ai.cloud.roleVer"
    AI_CLOUD_ROLE_INSTANCE = "ai.cloud.roleInstance"
    AI_CLOUD_LOCATION = "ai.cloud.location"
    AI_INTERNAL_SDK_VERSION = "ai.internal.sdkVersion"
    AI_INTERNAL_AGENT_VERSION = "ai.internal.agentVersion"
    AI_INTERNAL_NODE_NAME = "ai.internal.nodeName"


class DataPointType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the metric data measurement."""

    MEASUREMENT = "Measurement"
    AGGREGATION = "Aggregation"


class SeverityLevel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Defines the level of severity for the event."""

    VERBOSE = "Verbose"
    INFORMATION = "Information"
    WARNING = "Warning"
    ERROR = "Error"
    CRITICAL = "Critical"
