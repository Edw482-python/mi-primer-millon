from more_itertools import chunked

def ejecutar_tareas():
    print("¡Hola desde mi proyecto configurado!")

    # Imaginemos una lista de cosas pendientes de la casa o el mercado
    tareas_pendientes = [
        "Comprar pollo", 
        "Hacer arroz", 
        "Lavar ropa", 
        "Pagar servicios", 
        "Limpiar cocina", 
        "Comprar café"
    ]

    # Usamos la función 'chunked' para dividir las tareas en grupos de 2
    tareas_por_dia = list(chunked(tareas_pendientes, 2))

    print("\n--- Todas las tareas ---")
    print(tareas_pendientes)

    print("\n--- Tareas divididas en pares ---")
    for dia, tareas in enumerate(tareas_por_dia, 1):
        print(f"Grupo {dia}: {tareas}")


# Aquí es donde ocurre la magia de la variable especial
if __name__ == "__main__":
    ejecutar_tareas()
