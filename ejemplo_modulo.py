import ejemplo_modulo_importable

print("__name__ propio de ejemplo_modulo", __name__)

ejemplo_modulo_importable.datos()


if __name__ == "__main__":
    print("Soy el programa principal --> ejemplo_modulo")