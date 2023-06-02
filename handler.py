import json

from opentelemetry import trace

def hello(event, context):
    # Creates a tracer from the global tracer provider
    tracer = trace.get_tracer("my.tracer.name")
    with tracer.start_as_current_span("span-name") as span:
        body = {
            "message": "Go Serverless v1.0! Your function executed successfully!",
            "input": event
        }

        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
