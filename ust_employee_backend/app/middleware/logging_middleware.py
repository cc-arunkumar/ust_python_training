from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from typing import Callable

from database.mongodb import log_activity


class LoggingMiddleware(BaseHTTPMiddleware):
	"""Simple middleware that logs incoming requests and their response status to MongoDB.

	This is best-effort logging; failures won't affect request handling.
	"""

	async def dispatch(self, request: Request, call_next: Callable) -> Response:
		raw_emp_id = request.headers.get("x-emp-id")
		try:
			emp_id = int(raw_emp_id) if raw_emp_id is not None else None
		except (ValueError, TypeError):
			emp_id = None
		action = f"{request.method} {request.url.path}"

		# proceed with the request
		response = await call_next(request)

		# best-effort: log after response is ready
		try:
			log_activity(emp_id, action, resource_type="request", resource_id=None)
		except Exception:
			# never raise from middleware logging
			pass

		return response

