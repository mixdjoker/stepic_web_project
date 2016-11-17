from cgi import parse_qs


def app(environ, start_response):
    query = parse_qs(environ['QUERY_STRING'], keep_blank_values=True)
    body = []
    for qs_key, qs_val in query.items():
        for qs_item in qs_val:
            body.append("%s=%s\r\n" % (qs_key, qs_item))

    status = '200 OK'
    headers = [('Content-type', 'text/plain')]

    start_response(status, headers)
    return body
