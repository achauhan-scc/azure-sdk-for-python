# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: get_current_air_quality.py
DESCRIPTION:
    This API returns current air quality information that includes potential risks and suggested precautions.
USAGE:
    python get_current_air_quality.py

    Set the environment variables with your own values before running the sample:
    - AZURE_SUBSCRIPTION_KEY - your subscription key
"""
import os
import json

from azure.core.exceptions import HttpResponseError

subscription_key = os.getenv("AZURE_SUBSCRIPTION_KEY", "your subscription key")


def get_current_air_quality():
    from azure.core.credentials import AzureKeyCredential
    from azure.maps.weather import MapsWeatherClient

    maps_weather_client = MapsWeatherClient(credential=AzureKeyCredential(subscription_key))
    try:
        result = maps_weather_client.get_current_air_quality(coordinates=[25.0338053, 121.5640089])
        print(json.dumps(result, indent=4))

    except HttpResponseError as exception:
        if exception.error is not None:
            print(f"Error Code: {exception.error.code}")
            print(f"Message: {exception.error.message}")


if __name__ == "__main__":
    get_current_air_quality()
