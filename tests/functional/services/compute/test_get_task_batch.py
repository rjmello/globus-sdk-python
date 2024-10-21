import globus_sdk
from globus_sdk._testing import load_response


def test_get_task_batch(compute_client: globus_sdk.ComputeClient):
    meta = load_response(compute_client.get_task_batch).metadata
    res = compute_client.get_task_batch(task_ids=[meta["task_id"], meta["task_id_2"]])
    assert res.http_status == 200
    assert meta["task_id"] in res.data["results"]
    assert meta["task_id_2"] in res.data["results"]
