# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
# pylint: disable=wrong-import-position

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._patch import *  # pylint: disable=unused-wildcard-import


from ._models_py3 import (  # type: ignore
    APIKeyRequest,
    Annotation,
    AnnotationError,
    AnnotationsListResult,
    ApplicationInsightsComponent,
    ApplicationInsightsComponentAPIKey,
    ApplicationInsightsComponentAPIKeyListResult,
    ApplicationInsightsComponentAnalyticsItem,
    ApplicationInsightsComponentAnalyticsItemProperties,
    ApplicationInsightsComponentAvailableFeatures,
    ApplicationInsightsComponentBillingFeatures,
    ApplicationInsightsComponentDataVolumeCap,
    ApplicationInsightsComponentExportConfiguration,
    ApplicationInsightsComponentExportRequest,
    ApplicationInsightsComponentFavorite,
    ApplicationInsightsComponentFeature,
    ApplicationInsightsComponentFeatureCapabilities,
    ApplicationInsightsComponentFeatureCapability,
    ApplicationInsightsComponentListResult,
    ApplicationInsightsComponentProactiveDetectionConfiguration,
    ApplicationInsightsComponentProactiveDetectionConfigurationRuleDefinitions,
    ApplicationInsightsComponentQuotaStatus,
    ApplicationInsightsComponentWebTestLocation,
    ApplicationInsightsWebTestLocationsListResult,
    ComponentPurgeBody,
    ComponentPurgeBodyFilters,
    ComponentPurgeResponse,
    ComponentPurgeStatusResponse,
    ComponentsResource,
    ErrorFieldContract,
    ErrorResponse,
    InnerError,
    LinkProperties,
    MyWorkbook,
    MyWorkbookError,
    MyWorkbookResource,
    MyWorkbooksListResult,
    Operation,
    OperationDisplay,
    OperationListResult,
    PrivateLinkScopedResource,
    TagsResource,
    WebTest,
    WebTestGeolocation,
    WebTestListResult,
    WebTestPropertiesConfiguration,
    WebtestsResource,
    WorkItemConfiguration,
    WorkItemConfigurationError,
    WorkItemConfigurationsListResult,
    WorkItemCreateConfiguration,
    Workbook,
    WorkbookError,
    WorkbookResource,
    WorkbooksListResult,
)

from ._application_insights_management_client_enums import (  # type: ignore
    ApplicationType,
    CategoryType,
    FavoriteSourceType,
    FavoriteType,
    FlowType,
    IngestionMode,
    ItemScope,
    ItemScopePath,
    ItemType,
    ItemTypeParameter,
    PurgeState,
    RequestSource,
    SharedTypeKind,
    WebTestKind,
)
from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "APIKeyRequest",
    "Annotation",
    "AnnotationError",
    "AnnotationsListResult",
    "ApplicationInsightsComponent",
    "ApplicationInsightsComponentAPIKey",
    "ApplicationInsightsComponentAPIKeyListResult",
    "ApplicationInsightsComponentAnalyticsItem",
    "ApplicationInsightsComponentAnalyticsItemProperties",
    "ApplicationInsightsComponentAvailableFeatures",
    "ApplicationInsightsComponentBillingFeatures",
    "ApplicationInsightsComponentDataVolumeCap",
    "ApplicationInsightsComponentExportConfiguration",
    "ApplicationInsightsComponentExportRequest",
    "ApplicationInsightsComponentFavorite",
    "ApplicationInsightsComponentFeature",
    "ApplicationInsightsComponentFeatureCapabilities",
    "ApplicationInsightsComponentFeatureCapability",
    "ApplicationInsightsComponentListResult",
    "ApplicationInsightsComponentProactiveDetectionConfiguration",
    "ApplicationInsightsComponentProactiveDetectionConfigurationRuleDefinitions",
    "ApplicationInsightsComponentQuotaStatus",
    "ApplicationInsightsComponentWebTestLocation",
    "ApplicationInsightsWebTestLocationsListResult",
    "ComponentPurgeBody",
    "ComponentPurgeBodyFilters",
    "ComponentPurgeResponse",
    "ComponentPurgeStatusResponse",
    "ComponentsResource",
    "ErrorFieldContract",
    "ErrorResponse",
    "InnerError",
    "LinkProperties",
    "MyWorkbook",
    "MyWorkbookError",
    "MyWorkbookResource",
    "MyWorkbooksListResult",
    "Operation",
    "OperationDisplay",
    "OperationListResult",
    "PrivateLinkScopedResource",
    "TagsResource",
    "WebTest",
    "WebTestGeolocation",
    "WebTestListResult",
    "WebTestPropertiesConfiguration",
    "WebtestsResource",
    "WorkItemConfiguration",
    "WorkItemConfigurationError",
    "WorkItemConfigurationsListResult",
    "WorkItemCreateConfiguration",
    "Workbook",
    "WorkbookError",
    "WorkbookResource",
    "WorkbooksListResult",
    "ApplicationType",
    "CategoryType",
    "FavoriteSourceType",
    "FavoriteType",
    "FlowType",
    "IngestionMode",
    "ItemScope",
    "ItemScopePath",
    "ItemType",
    "ItemTypeParameter",
    "PurgeState",
    "RequestSource",
    "SharedTypeKind",
    "WebTestKind",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
