from googletrans import Translator

# Texto que deseas traducir
texto_a_traducir = "Hello, how are you?"

# Crea una instancia del traductor
translator = Translator()

# Idioma de destino
idioma_destino = "es"  # Por ejemplo, español

# Realiza la traducción
traduccion = translator.translate(texto_a_traducir, dest=idioma_destino)

print(f"Texto original: {texto_a_traducir}")
print(f"Traducción ({idioma_destino}): {traduccion.text}")

