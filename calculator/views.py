from django.http import JsonResponse


def add(request):
    try:
        a = float(request.GET.get("a", 0))
        b = float(request.GET.get("b", 0))
    except ValueError:
        return JsonResponse({"error": "Invalid input"}, status=400)
    return JsonResponse({"result": a + b})


def subtract(request):
    try:
        a = float(request.GET.get("a", 0))
        b = float(request.GET.get("b", 0))
    except ValueError:
        return JsonResponse({"error": "Invalid input"}, status=400)
    return JsonResponse({"result": a - b})


def multiply(request):
    try:
        a = float(request.GET.get("a", 0))
        b = float(request.GET.get("b", 0))
    except ValueError:
        return JsonResponse({"error": "Invalid input"}, status=400)
    return JsonResponse({"result": a * b})


def divide(request):
    try:
        a = float(request.GET.get("a", 0))
        b = float(request.GET.get("b", 0))
    except ValueError:
        return JsonResponse({"error": "Invalid input"}, status=400)
    if b == 0:
        return JsonResponse({"error": "Division by zero"}, status=400)
    return JsonResponse({"result": a / b})
