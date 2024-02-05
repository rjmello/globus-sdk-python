import globus_sdk
from globus_sdk._testing import load_response


def test_get_endpoint(client):
    meta = load_response(client.get_endpoint).metadata

    get_response = client.get_endpoint()

    assert get_response["DATA_TYPE"] == "endpoint#1.2.0"
    assert get_response["display_name"] == meta["display_name"]
    assert get_response["id"] == meta["endpoint_id"]


def test_update_endpoint(client):
    meta = load_response(client.update_endpoint).metadata

    update_doc = globus_sdk.EndpointDocument(display_name=meta["display_name"])
    update_response = client.update_endpoint(update_doc)

    assert update_response["DATA_TYPE"] == "result#1.0.0"
    assert update_response["message"] == f"Updated endpoint {meta['endpoint_id']}"


def test_update_endpoint_including_endpoint_in_response(client):
    meta = load_response(client.update_endpoint, case="include_endpoint").metadata

    update_doc = globus_sdk.EndpointDocument(display_name=meta["display_name"])
    update_response = client.update_endpoint(update_doc, include=["endpoint"])

    assert update_response["DATA_TYPE"] == "endpoint#1.2.0"
    assert update_response["display_name"] == meta["display_name"]
    assert update_response["id"] == meta["endpoint_id"]
