import validaciones

def formulario():
    print("📌 Ingreso de productos - Confitería Dulcino 📌")

    # Nombre del producto
    nombre = input("Ingrese el nombre del producto: ")
    if not validaciones.validar_nombre(nombre):
        print("❌ Error: El nombre no debe tener más de 20 caracteres.")
        return
    
    # Precio del producto
    try:
        precio = float(input("Ingrese el precio del producto: "))
        if not validaciones.validar_precio(precio):
            print("❌ Error: El precio debe estar entre 0.01 y 999.00 soles.")
            return
    except ValueError:
        print("❌ Error: Por favor verifique el campo del precio.")
        return

    # Categorías del producto
    categorias = input("Ingrese las categorías separadas por coma (Ejemplo: Chocolates,Galletas): ").split(",")
    if not validaciones.validar_categorias(categorias):
        print("❌ Error: Una o más categorías ingresadas no son válidas.")
        return

    # Estado del producto en venta
    estado = input("¿El producto está en venta? (Si/No): ").strip().lower()
    if not validaciones.validar_estado(estado):
        print("❌ Error: Debe responder 'Si' o 'No'.")
        return

    print("✅ Felicidades, su producto se agregó.")

# Ejecutar formulario
if __name__ == "__main__":
    formulario()
