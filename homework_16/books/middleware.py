import logging
import time


logger = logging.getLogger(__name__)


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        logger.info(
            "Request: %s %s | User: %s",
            request.method,
            request.path,
            (
                request.user.username
                if request.user.is_authenticated
                else "Anonymous"
            ),
        )

        response = self.get_response(request)

        execution_time = (
            time.time() - start_time
        )

        logger.info(
            "Response: %s | Path: %s | Time: %.3f sec",
            response.status_code,
            request.path,
            execution_time,
        )

        return response
