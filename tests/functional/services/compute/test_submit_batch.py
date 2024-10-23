import globus_sdk
from globus_sdk._testing import load_response


def test_submit(compute_client: globus_sdk.ComputeClient):
    meta = load_response(compute_client.submit).metadata
    batch_doc = {
        "tasks": {
            meta["function_id"]: [meta["task_args"], meta["task_args_2"]],
        },
        "task_group_id": meta["task_group_id"],
        "create_queue": True,
        "user_runtime": {
            "globus_compute_sdk_version": "2.29.0",
            "globus_sdk_version": "3.46.0",
            "python_version": "3.11.9",
        },
    }

    res = compute_client.submit(endpoint_id=meta["endpoint_id"], data=batch_doc)

    assert res.http_status == 200
    assert res.data["request_id"] == meta["request_id"]
    assert res.data["task_group_id"] == meta["task_group_id"]
    assert res.data["endpoint_id"] == meta["endpoint_id"]
    assert res.data["tasks"] == {
        meta["function_id"]: [meta["task_id"], meta["task_id_2"]]
    }
