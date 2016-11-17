from urllib import parse


def application(environ, start_response):
    query = parse.parse_qs(environ['QUERY_STRING'], keep_blank_values=True)
    body = []
    for qs_key, qs_val in query.items():
        for qs_item in qs_val:
            body.append("{}={}\r\n".format(qs_key, qs_item))

    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]

    start_response(status, headers)
    return body
