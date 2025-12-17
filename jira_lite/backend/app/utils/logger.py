from app.db.mongodb import logs_collection
from app.models.mongo_models import log_document

def create_log(
    *,
    emp_id: str,
    roles: list,
    module: str,
    action: str,
    description: str,
    status: str,
    resource_id: str | None = None,
    old_value: dict | None = None,
    new_value: dict | None = None
):
    log = log_document(
        emp_id=emp_id,
        roles=roles,
        module=module,
        action=action,
        description=description,
        status=status,
        resource_id=resource_id,
        old_value=old_value,
        new_value=new_value
    )

    logs_collection.insert_one(log)
