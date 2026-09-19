import json


def salva_arquivo(lista):
    with open ("Ingresso.json","w",encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, indent=4, ensure_ascii=False)


def abrir_arquivo():
    try:
        with open("ingresso.json", "r", encoding="utf-8") as arquivo:
            ingressos = json.load(arquivo)
            return ingressos
    except FileNotFoundError:
            return []