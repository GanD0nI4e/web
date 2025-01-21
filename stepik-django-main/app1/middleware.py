import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class LoggingMiddleware:
    """
    Middleware for logging request and response data.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log incoming request
        start_time = datetime.now()
        logger.info(f"Request: {request.method} {request.path} - {request.body.decode('utf-8') if request.body else 'No Body'}")

        # Get the response
        response = self.get_response(request)

        # Log response
        duration = (datetime.now() - start_time).total_seconds()
        logger.info(
            f"Response: {response.status_code} - {response.content.decode('utf-8') if hasattr(response, 'content') else 'No Content'} - Time taken: {duration} seconds"
        )

        return response
