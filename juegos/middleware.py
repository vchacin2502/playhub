import time

class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        inicio = time.time()
        response = self.get_response(request)
        duracion = time.time() - inicio

        usuario = (
            request.user.username
            if request.user.is_authenticated
            else 'anonimo'
        )

        print(
            f"[{request.method}] {request.path} | "
            f"usuario={usuario} | "
            f"{duracion:.4f}s"
        )

        return response
