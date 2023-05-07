"""
Gist code by vstoykov, you can check his original gist at:
https://gist.github.com/vstoykov/1390853/5d2e8fac3ca2b2ada8c7de2fb70c021e50927375
Changes:
Ignoring static file requests and a certain useless admin request from triggering the logger.
Updated statements to make it Python 3 friendly.
"""

import os
from typing import Any

from django.conf import settings
from django.db import connection


def terminal_width() -> int:
    """
    Function to compute the terminal width.
    """
    width = 0
    try:
        import fcntl
        import struct
        import termios

        s = struct.pack("HHHH", 0, 0, 0, 0)
        x = fcntl.ioctl(1, termios.TIOCGWINSZ, s)
        width = struct.unpack("HHHH", x)[1]
    except:
        pass
    if width <= 0:
        try:
            width = int(os.environ["COLUMNS"])
        except:
            pass
    if width <= 0:
        width = 80
    return width


def SqlPrintingMiddleware(get_response: Any) -> Any:
    def middleware(request: Any) -> Any:
        response = get_response(request)
        if (
            not settings.DEBUG
            or len(connection.queries) == 0
            or request.path_info.startswith(settings.MEDIA_URL)
            or "/admin/jsi18n/" in request.path_info
        ):
            return response

        indentation = 2
        print(f"\033[1;35m[SQL]\033[1;33m {request.method}\033[1;34m {request.path_info}\033[0m")
        # width = terminal_width()
        total_time = 0.0
        for query in connection.queries:
            nice_sql = query["sql"].replace('"', "").replace(",", ", ")
            sql = "\033[1;31m[{}]\033[0m {}".format(query["time"], nice_sql)
            total_time = total_time + float(query["time"])
            # while len(sql) > width - indentation:
            #     print("%s%s" % (" " * indentation, sql[: width - indentation]))
            # sql = sql[width - indentation :]
            print("{}{}\n".format(" " * indentation, sql))
        replace_tuple = (" " * indentation, str(total_time))
        print("%s\033[1;32m[TOTAL TIME: %s seconds]\033[0m" % replace_tuple)
        print("{}\033[1;32m[TOTAL QUERIES: {}]\033[0m".format(" " * indentation, len(connection.queries)))
        return response

    return middleware


def ApiPrintingMiddleware(get_response: Any) -> Any:
    def middleware(request: Any) -> Any:
        response = get_response(request)
        if (
            not settings.DEBUG
            or len(connection.queries) == 0
            or request.path_info.startswith(settings.MEDIA_URL)
            or "/admin/jsi18n/" in request.path_info
        ):
            return response

        print(f"\033[1;35m[API]\033[1;33m {request.method}\033[1;34m {request.path_info}\033[0m")
        return response

    return middleware
