
# Daniel Cu Sanchez
# A01703613

import numpy as np

def similitud_coseno(vector1, vector2):
    producto_punto = np.dot(vector1, vector2)
    norma_vector1 = np.linalg.norm(vector1)
    norma_vector2 = np.linalg.norm(vector2)
    similitud = producto_punto / (norma_vector1 * norma_vector2)
    return similitud

def bolsa_de_palabras(texto1, texto2):
    palabras = list(set(texto1.split() + texto2.split()))
    vector1 = [texto1.split().count(palabra) for palabra in palabras]
    vector2 = [texto2.split().count(palabra) for palabra in palabras]
    return vector1, vector2

def tfidf(texto1, texto2):
    palabras = list(set(texto1.split() + texto2.split()))
    vector1 = [texto1.split().count(palabra) * np.log(2 / (texto1.split().count(palabra) + texto2.split().count(palabra))) for palabra in palabras]
    vector2 = [texto2.split().count(palabra) * np.log(2 / (texto1.split().count(palabra) + texto2.split().count(palabra))) for palabra in palabras]
    return vector1, vector2

# Textos de ejemplo
texto1 = "Internet efectivo en comunidades rurales, somos ALTERNET"
texto2 = "Internet en comunidades rurales, rompemos la brecha digital somos ALTERNET"

# Vectorización utilizando la técnica de Bolsa de Palabras
vector_bolsa1, vector_bolsa2 = bolsa_de_palabras(texto1, texto2)

# Vectorización utilizando la técnica de tf-idf
vector_tfidf1, vector_tfidf2 = tfidf(texto1, texto2)

# Cálculo de la similitud utilizando la medida del coseno
similitud_bolsa = similitud_coseno(vector_bolsa1, vector_bolsa2)
similitud_tfidf = similitud_coseno(vector_tfidf1, vector_tfidf2)

print("Similitud utilizando bolsa de palabras: 💰", similitud_bolsa)
print("Similitud utilizando tf-idf 😈:", similitud_tfidf)
