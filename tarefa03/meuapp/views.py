from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def usuarios(request):
    listausuarios=[
        {"nome": "antonieta","idade": 7,"matricula":20261181110280, "cidade": "lagoa de velhos"},
        {"nome": "messias","idade": 19,"matricula":20261181110028, "cidade": "lagoa de velhos"},
        {"nome": "ianderson","idade": 27,"matricula":20261181110180, "cidade": "lagoa de velhos"},
        {"nome": "vanderson","idade": 26,"matricula":20261181110080, "cidade": "lagoa de velhos"},
        {"nome": "baltazar","idade": 45,"matricula":20261181110380, "cidade": "sp-sao paulo"},

    ]
    context = {
        "usuarios": listausuarios,
    }
    return render(request, "usuarios.html", context)
    