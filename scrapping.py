import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


PRODUCTO = "Aceite"
lista_productos = []

"""
Esta sección se encarga de ejecutar el driver de Selenium para poder abrir el navegador.
El driver varía en dependencia del navegador que se use y la versión del mismo.
"""

driver_path = "D:\Estudio\Investigaciones\Programar\geckodriver-v0.31.0-win64\geckodriver.exe"
driver = webdriver.Firefox(executable_path=driver_path)
driver.get("https://www.supermarket23.com/")

time.sleep(15) # Hay que esperar un tiempo en dependencia de la velocidad de Internet que se tenga, para que cargue la página
provincia = driver.find_element(By.CSS_SELECTOR, "#province") # Buscar el menú Provincia
provincia.click()

habana = driver.find_element_by_xpath("/html/body/modal-container/div/div/app-location-dialog/div[2]/div/div[1]/select/option[3]")
habana.click() # Busca La Habana y la selecciona.
municipio = driver.find_element_by_xpath("/html/body/modal-container/div/div/app-location-dialog/div[2]/div/div[2]/select/option[2]")
municipio.click() # Busca Playa y la selecciona. Esta parte se puede hacer diferente, lo hice así porque es más directo.
aceptar = driver.find_element_by_xpath("/html/body/modal-container/div/div/app-location-dialog/div[3]/button")
aceptar.click() # Se da click en el botón Aceptar

time.sleep(10) # Espera un tiempo de respuesta de la página

barra = driver.find_element_by_xpath("/html/body/app-root/app-main/app-frontend/app-nd-header/header/section[1]/div[1]/div/input")
barra.send_keys(PRODUCTO)
barra.send_keys(Keys.ENTER) # Busca la barra de búsqueda de productos, se escribe el producto que se desea buscar y se da Enter.

time.sleep(10) # Espera un tiempo de respuesta de la página

# primero = driver.find_element_by_xpath("/html/body/app-root/app-main/app-frontend/app-search/div/div/div[2]/div/div[3]/div[1]/app-product-block-v/div/div[2]")
# print(primero.text)
productos = driver.find_elements(By.CSS_SELECTOR, ".product_content") # Se obtienen todos los productos de Aceite
print(type(productos))
for cada_producto in productos:
    # print(cada_producto.text)
    nuevo_producto = cada_producto.text.split("\n")
    nombre_producto = nuevo_producto[0]
    marca_producto = nuevo_producto[1]
    precio_producto = nuevo_producto[2]
    dicc_prod = {
        "nombre_producto": nombre_producto,
        "marca_producto": marca_producto,
        "precio_producto": precio_producto
    }
    lista_productos.append(dicc_prod) # Se guarda cada producto en una lista, y cada objeto de la lista es un diccionario con el Nombre, Marca y Precio Actual del Producto.


print(lista_productos)