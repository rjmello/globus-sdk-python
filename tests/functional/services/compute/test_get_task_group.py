import globus_sdk
from globus_sdk._testing import load_response


def test_get_task_group(compute_client: globus_sdk.ComputeClient):
    meta = load_response(compute_client.get_task_group).metadata
    res = compute_client.get_task_group(task_group_id=meta["task_group_id"])
    assert res.http_status == 200
    assert meta["task_group_id"] == res.data["taskgroup_id"]
    assert meta["task_id"] == res.data["tasks"][0]["id"]
    assert meta["task_id_2"] == res.data["tasks"][1]["id"]
