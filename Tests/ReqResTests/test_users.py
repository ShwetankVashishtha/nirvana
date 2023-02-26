import pytest

from RestUtils.ApiHttpMethods import *
from RestUtils.ApiAssertions import *

api_http_methods = ApiHttpMethods()


@pytest.mark.regression
def test_ok_users_list(base_url, users_end_point):
    print("Test the Get Request")

    # Add query parameters to the request
    params = {
        "user": 144
    }

    # Execute the request
    response = api_http_methods.get(base_url, users_end_point, headers=None, params=params)

    # Assert response code
    ApiAssertions.verify_ok_response_code(response)

    # Assert response time
    ApiAssertions.verify_response_time(response)

    # Assert response headers
    ApiAssertions.verify_response_header(response)

    # Print response body json
    resp_json = response.json()
    print(resp_json)
