from globus_sdk._testing.models import RegisteredResponse, ResponseSet

from ._common import (
    ENDPOINT_ID,
    FUNCTION_ID,
    TASK_ARGS,
    TASK_ARGS_2,
    TASK_GROUP_ID,
    TASK_ID,
    TASK_ID_2,
)

REQUEST_ID = "5158de19-10b5-4deb-9d87-a86c1dec3460"

SUBMIT_BATCH_RESPONSE = {
    "request_id": REQUEST_ID,
    "task_group_id": TASK_GROUP_ID,
    "endpoint_id": ENDPOINT_ID,
    "tasks": {
        FUNCTION_ID: [TASK_ID, TASK_ID_2],
    },
}

RESPONSES = ResponseSet(
    metadata={
        "endpoint_id": ENDPOINT_ID,
        "function_id": FUNCTION_ID,
        "task_id": TASK_ID,
        "task_id_2": TASK_ID_2,
        "task_args": TASK_ARGS,
        "task_args_2": TASK_ARGS_2,
        "task_group_id": TASK_GROUP_ID,
        "request_id": REQUEST_ID,
    },
    default=RegisteredResponse(
        service="compute",
        path=f"/v2/endpoints/{ENDPOINT_ID}/submit",
        method="POST",
        json=SUBMIT_BATCH_RESPONSE,
    ),
)
