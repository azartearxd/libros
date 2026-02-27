# =============================================================================
# 1️⃣ LIBRERÍAS
# =============================================================================
import requests
from bs4 import BeautifulSoup
import pandas as pd

# =============================================================================
# 2️⃣ OBTENCIÓN DEL HTML
# =============================================================================
url = "https://elfondoenlinea.com/"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# =============================================================================
# 3️⃣ EXTRACCIÓN DE DATOS
# =============================================================================
titulos = soup.find_all("p", class_="titulo-mini-slider")
autores = soup.find_all("p", class_="autor-mini-slider")
precios = soup.find_all("ul", class_="nav fce-precios")

# =============================================================================
# 4️⃣ ALMACENAMIENTO EN ARREGLO
# =============================================================================
libros = []

for i in range(len(titulos)):
    titulo = titulos[i].text.strip()
    autor = autores[i].text.strip()
    
    precio_original = precios[i].find("s")
    precio_original = precio_original.text.strip() if precio_original else "No disponible"
    
    precio_descuento = precios[i].find("span")
    precio_descuento = precio_descuento.text.strip() if precio_descuento else "No disponible"
    
    libros.append([titulo, autor, precio_original, precio_descuento])

# =============================================================================
# 5️⃣ CONVERTIR A DATAFRAME
# =============================================================================
df = pd.DataFrame(libros, columns=["Titulo", "Autor", "Precio Original", "Precio Descuento"])

print(df)

# (Opcional) Guardar como CSV
df.to_csv("libros_fce.csv", index=False, encoding="utf-8")

print("✅ DataFrame creado y archivo CSV guardado.")