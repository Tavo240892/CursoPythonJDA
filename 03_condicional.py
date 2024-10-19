cerrarPrograma = 0

print("EJERCICIOS CONDICIONALES\nEn este programa encontraras diferentes ejercicios que podras ejecutar según tu elección.")

while cerrarPrograma == 0:

    seleccion = int(input("A continuación encontraras un listado con las diferentes opciones (ejercicios) que puedes ejecutar.\nEscribe el numero de la opción para ejecutar el programa.\n1. Es una persona mayor de edad o no?\n2. Verificar si un número es positivo, negativo o cero.\n3. Determinar si un estudiante aprobó o no.\n4. Comprobar si un número es par o impar.\n5. Verificar si un número está dentro de un rango.\n6. Clasificación de Números.\n"))

    if seleccion == 1:

        # Actividad 5 Realiza un if donde determine si una persona es mayor de edad o no

        print("Digita la edad de una persona y descubre si es mayor o menor de edad")

        edad = int(input("Digita tu edad "))

        if edad >= 18:
            print("la persona es mayor de edad")
        else:
            print("la persona es menor de edad")

    elif seleccion == 2:

        # Nivel básico:
        # Verificar si un número es positivo, negativo o cero
        # Descripción: Crea un programa que pida al usuario un número y verifique si es positivo, negativo o cero.

        print("Digita un numero entero y descubre si es positivo, negativo o cero")

        def verificar_numero(numero):
            if numero < 0:
                salida = "El numero es negativo"
            elif numero == 0:
                salida = "El numero es cero"
            else:
                salida = "El numero es positivo"
            return salida

        dato = int(input("Digita el numero "))    
        print(verificar_numero(dato))

    elif seleccion == 3:

        # Determinar si un estudiante aprobó o no
        # Descripción: Crea un programa que pida la calificación de un estudiante y determine si ha aprobado (60 o más) o no.

        print("Digita la calificación de un estudiante y descubre si reprobo o aprobo el curso")

        def resultado_estudiante(calificacion):
            if calificacion > 0 and calificacion < 60:
                salida = "El estudiante reprobo"
            elif calificacion >= 60 and calificacion <= 100:
                salida = "El estudiante aprobo"
            else:
                salida = "El valor es incorrecto, digita un valor entre cero y 100"
            return salida
            
        resultado = int(input("Digita la calificacion del estudiante, siendo 0 la calificación mas baja y 100 la calificación mas alta "))
        print(resultado_estudiante(resultado))

    elif seleccion == 4:

        # Nivel intermedio:
        # Comprobar si un número es par o impar
        # Descripción: Crea un programa que pida al usuario un número y determine si es par o impar.

        print("Digita un numero entero y descubre si el valor es positivo o negativo")

        def par_impar(numero):
            esparimpar = numero % 2
            if esparimpar == 0:
                salida = "El numero es par"
            else:
                salida = "El numero es impar"
            return salida

        resultadoParImpar = int(input("Digita el numero: "))
        print(par_impar(resultadoParImpar))

    elif seleccion == 5:

        # Verificar si un número está dentro de un rango
        # Descripción: Crea un programa que pida al usuario un número y verifique si está en el rango de 1 a 10 (inclusive).

        print("Digita un numero entero y descubre si esta dentro del rango de numeros de uno a diez.")

        def dentro_rango(numero):
            if numero > 0 and numero <= 10:
                return "El nuero que escribiste esta dentro del rango"
            else:
                return "El nuero que escribiste esta fuera del rango"

        resultadoRango = int(input("Digita un muero entero: "))
        print(dentro_rango(resultadoRango))

    # Nivel Avanzado:

    elif seleccion == 6:

        # Clasificación de Números
        # Descripción: Crea una función que reciba una lista de números enteros y clasifique cada número como "positivo", "negativo" o "cero". La función debe devolver un diccionario que contenga el conteo de cada categoría.

        # Requisitos:

        # Utilizar if, elif y else para clasificar los números.
        # Deberá considerar si el número es impar o par, y agregar esta información al diccionario.

        numeros = []
        numDicPositivo = []
        numDicNegativo = []
        numDicCero = []
        numDicPar = []
        numDicImpar = []

        cantidad = int(input("Digita el numero maximo de numeros que quieres clasificar: "))

        for i in range(cantidad):    
            numero = int(input(f"Digita el numero {i + 1}: "))
            numeros.append(numero)

        for i in numeros:
            if i > 0:
                numPositivo = i
                numDicPositivo.append(numPositivo)
                if i % 2 == 0:
                    numPar = i
                    numDicPar.append(numPar)
                else:
                    numImpar = i
                    numDicImpar.append(numImpar)
            elif i < 0:
                numNegativo = i
                numDicNegativo.append(numNegativo)
            elif i == 0:
                numCero = i
                numDicCero.append(numCero)

        diccionario = {'Positivo':numDicPositivo,'Negativo':numDicNegativo,'Cero':numDicCero,'Par':numDicPar,'Impar':numDicImpar}

        print(diccionario)

    # Cálculo de Tarifas de Envío
    # Descripción: Diseña una función que calcule la tarifa de envío basada en el peso del paquete y el destino. La tarifa debe ser calculada usando las siguientes reglas:

    # Menos de 1 kg: $5
    # De 1 a 5 kg: $10
    # Más de 5 kg: $20
    # Si el destino es internacional, sumar un recargo del 50% al costo total.
    # Requisitos:

    # Usa if y else para determinar el costo según el peso.
    # Usa if adicional para comprobar si el envío es internacional y calcular el recargo correspondiente.
    
    else:
        print("La opcion que digitaste es incorrecta")

    cerrarPrograma = int(input("Digita el numero 0 si deseas ejecutar otro ejercicio o 1 si deseas cerrar el programa: "))