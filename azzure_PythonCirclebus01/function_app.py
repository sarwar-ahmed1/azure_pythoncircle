import azure.functions as func

import logging

import circle

app = func.FunctionApp()

# Learn more at aka.ms/pythonprogrammingmodel

@app.function_name(name="PythonCircle")
@app.route(route="pythoncircle", auth_level=func.AuthLevel.ANONYMOUS)
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python circle trigger function processed a request.")

    radius = req.params.get("radius")
    if not radius:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            radius = req_body.get("radius")

    if radius:
        try:
            radius = float(radius)
            response = circle.Circle(radius)
            return func.HttpResponse(
                f"Here is your circle, perimeter {response.perimeter()} and area: {response.area()}",
                status_code=200,
            )
        except ValueError:
            return func.HttpResponse(
                "No circle could be generated, please pass a valid radius",
                status_code=200,
            )
    else:
        return func.HttpResponse(
            "No circle could be generated, please pass a valid radius", status_code=200
        )