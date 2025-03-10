import streamlit as st
import validaciones

# Título de la app
st.title("📌 Formulario de Productos - Confitería Dulcino")

# Ingreso del nombre del producto
nombre = st.text_input("Ingrese el nombre del producto:")

# Ingreso del precio del producto
precio = st.text_input("Ingrese el precio del producto:")

# Selección de categorías (usamos checkboxes para seleccionar múltiples opciones)
CATEGORIAS_VALIDAS = ["Chocolates", "Caramelos", "Mashmelos", "Galletas", "Salados", "Gomas de mascar"]
categorias = st.multiselect("Seleccione las categorías del producto:", CATEGORIAS_VALIDAS)

# Estado del producto en venta (Radio button)
estado = st.radio("¿El producto está en venta?", ["Si", "No"])

# Botón para agregar el producto
if st.button("Agregar Producto"):
    # Validación del nombre
    if not validaciones.validar_nombre(nombre):
        st.error("❌ El nombre no debe tener más de 20 caracteres.")
    else:
        try:
            # Validación del precio
            precio = float(precio)
            if not validaciones.validar_precio(precio):
                st.error("❌ El precio debe estar entre 0.01 y 999.00 soles.")
            elif not validaciones.validar_categorias(categorias):
                st.error("❌ Una o más categorías ingresadas no son válidas.")
            elif not validaciones.validar_estado(estado.lower()):
                st.error("❌ Debe seleccionar 'Si' o 'No'.")
            else:
                st.success("✅ Felicidades, su producto se agregó.")
        except ValueError:
            st.error("❌ Por favor verifique el campo del precio. Debe ser un número.")

