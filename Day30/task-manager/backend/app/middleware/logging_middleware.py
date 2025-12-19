"""import json
from datetime import datetime
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.database.mongodb import api_logs_collection
from app.auth.jwt_handler import decode_token


class MongoLoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):
        request_body = None
        user_info = None

        # ---------- READ REQUEST BODY (only if JSON) ----------
        try:
            content_type = (request.headers.get("content-type") or "").lower()
            # Only attempt to read & parse JSON bodies. Avoid consuming multipart/form-data
            # (file uploads) or other non-JSON payloads which would break downstream
            # request parsing (UploadFile, form data, etc.).
            if "application/json" in content_type:
                body_bytes = await request.body()
                if body_bytes:
                    request_body = json.loads(body_bytes.decode())
            else:
                request_body = None
        except Exception:
            request_body = None

        # ---------- READ USER FROM JWT ----------
        auth_header = request.headers.get("Authorization")
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]
            try:
                user_info = decode_token(token)
            except:
                user_info = None

        response = None
        error_message = None

        try:
            response = await call_next(request)
            status_code = response.status_code
        except Exception as e:
            status_code = 500
            error_message = str(e)
            raise e

        # ---------- LOG DOCUMENT ----------
        log_document = {
            "timestamp": datetime.utcnow(),
            "method": request.method,
            "path": request.url.path,
            "status_code": status_code,
            "user": {
                "emp_id": user_info.get("emp_id") if user_info else None,
                "role": user_info.get("role") if user_info else None
            },
            "request_body": request_body,
            "error": error_message
        }

        api_logs_collection.insert_one(log_document)

        return response
"""

import json
from datetime import datetime
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.database.mongodb import api_logs_collection
from app.utils.auth import decode_token  # Updated import

class MongoLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_body = None
        user_info = None
        # ---------- READ REQUEST BODY ----------
        try:
            body_bytes = await request.body()
            if body_bytes:
                request_body = json.loads(body_bytes.decode())
        except:
            request_body = None
        # ---------- READ USER FROM JWT ----------
        auth_header = request.headers.get("Authorization")
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]
            try:
                user_info = decode_token(token)
            except:
                user_info = None
        response = None
        error_message = None
        try:
            response = await call_next(request)
            status_code = response.status_code
        except Exception as e:
            status_code = 500
            error_message = str(e)
            raise e
        # ---------- LOG DOCUMENT ----------
        log_document = {
            "timestamp": datetime.utcnow(),
            "method": request.method,
            "path": request.url.path,
            "status_code": status_code,
            "user": {
                "emp_id": user_info.get("emp_id") if user_info else None,
                "role": user_info.get("role") if user_info else None
            },
            "request_body": request_body,
            "error": error_message
        }
        api_logs_collection.insert_one(log_document)
        return response