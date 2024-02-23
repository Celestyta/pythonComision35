def verificar_calificacion(nota1, nota2, nota3):
    # Calcular el promedio de las notas
    promedio = (nota1 + nota2 + nota3) / 3

    # Verificar si el promedio es mayor o igual a 6
    if promedio >= 6:
        return "Aprobado"
    else:
        return "Reprobado"

# Ejemplo de uso de la función
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

resultado = verificar_calificacion(nota1, nota2, nota3)
print("El estudiante está:", resultado)