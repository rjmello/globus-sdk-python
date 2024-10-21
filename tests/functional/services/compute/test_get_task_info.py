import globus_sdk
from globus_sdk._testing import load_response


def test_get_task(compute_client: globus_sdk.ComputeClient):
    meta = load_response(compute_client.get_task).metadata
    res = compute_client.get_task(task_id=meta["task_id"])
    assert res.http_status == 200
    assert res.data["task_id"] == meta["task_id"]
