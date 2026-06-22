progress_store = {}


def update_progress(
    job_id: str,
    step: str
):
    if job_id not in progress_store:
        progress_store[job_id] = []

    if (
        step
        not in progress_store[job_id]
    ):
        progress_store[job_id].append(
            step
        )

def get_progress(
    job_id: str
):
    return progress_store.get(
        job_id,
        []
    )