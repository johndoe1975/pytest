import datetime
from django.db import connection
import  django.http.response

class LogMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        time_start = datetime.datetime.now()
        response = self.get_response(request)
        assert isinstance(response, django.http.response.HttpResponse)
        print(response.get("content-type"))
        if response.get("content-type", "").lower().startswith("text/html"):
            total_queries_time = 0.0
            for q in connection.queries:
                total_queries_time += float(q['time'])
            time_end = datetime.datetime.now()
            duration = time_end-time_start
            report = (
                " <br> Total execution time: {} ms <br>"
                "Number of queries: {} <br>"
                "Time of queries execution: {} ms <br>"
            ).format(duration.total_seconds() * 1000, len(connection.queries), total_queries_time * 1000)
            ind = response.content.rfind(b"</body>")
            response.content = response.content[:ind] + report.encode("utf-8") + response.content[ind:]

        return response