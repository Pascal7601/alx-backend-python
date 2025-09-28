from django.core.exceptions import PermissionDenied
import datetime
class RequestLoggingMiddleware:
    """
    logs each user’s requests to a file requests.log, including the
    timestamp, user and the request path.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path
        request_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user = request.user if request.user.is_authenticated else "Anonymous"

        with open("requests.log", "a") as f:
            f.write(f"[{request_time}] - User: {user} - Path: {path}\n")

        response = self.get_response(request)

        return response


class RestrictAccessByTimeMiddleware:
    """
    restricts access to the messaging up during certain
    hours of the day ( outside 9PM and 6PM.)
    """

    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        current_time = datetime.datetime.now().time()
        hour = current_time.hour
        if not (18 <= hour > 21):
            raise PermissionDenied("Access denied at this time")

        response = self.get_response(request)

        return response
