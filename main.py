import svc.functions as fn

def handler(event, context):
    print(event)

    result = fn.make_get_request(event["url"])
    if "error" in result:
        return make_error_response(result["error"])

    return make_success_response(result)


def make_success_response(result: dict):
    return {"statusCode": 200, **result}

def make_error_response(err: any):
    return {"statusCode": 500, "error": err}

if __name__ == "__main__":
    res = handler({"url": "https://randomuser.me/api"}, {})
    print(res)

