# Rama: rama-integrante4
def contar_vocales(texto):
    vocales = sum(1 for letra in texto.lower() if letra in "aeiouáéíóú")
    print(f"[Integrante 4 - Israel]: La frase '{texto}' tiene {vocales} vocales")

contar_vocales("Aprendiendo Git en equipo")
