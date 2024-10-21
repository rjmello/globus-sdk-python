import copy

from globus_sdk._testing.models import RegisteredResponse, ResponseSet

from ._common import TASK_DOC, TASK_ID, TASK_ID_2

TASK_DOC_2 = copy.deepcopy(TASK_DOC)
TASK_DOC_2["task_id"] = TASK_ID_2

TASK_BATCH_DOC = {
    "response": "batch",
    "results": {
        TASK_ID: TASK_DOC,
        TASK_ID_2: TASK_DOC_2,
    },
}

RESPONSES = ResponseSet(
    metadata={"task_id": TASK_ID, "task_id_2": TASK_ID_2},
    default=RegisteredResponse(
        service="compute",
        path="/v2/tasks/batch",
        method="POST",
        json=TASK_BATCH_DOC,
    ),
)
