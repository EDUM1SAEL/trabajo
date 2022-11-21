opcion=int(input("\n Menu\n ---------------------------\n\t"+
                 "1.Mayor y menor\n\t2.Tres valores mayor\n\t3.solicitud de tres valores multiplo\n\t4.promedio par e impar\n\t 5.Telefonia\n\t6.Mostrar la tabla de multiplicación de un valor ingresado\n\t 7.Mostrar el listado de números impares de 1 \n\t 8.Mostrar los números múltiplos de un número\n\t9.salir" +
                 "\n favor ingrese una opción :"));
while(opcion !=9):
    if (opcion ==1):
        n1=int(input("introduzca el primer numero:"));
        n2=int(input("introduzca el segundo numero:"));
        if (n1>n2):
            print("el primer numero es el mayor");
        elif (n1<n2):
            print("el segundo numero es el mayor");
        else:
            print("los numeros son iguales");
        opcion = int(input("\n Menu\n ---------------------------\n\t" +
                           "1.Mayor y menor\n\t2.Tres valores mayor\n\t3.solicitud de tres valores multiplo\n\t4.promedio par e impar\n\t 5.Telefonia\n\t6.Mostrar la tabla de multiplicación de un valor ingresado\n\t 7.Mostrar el listado de números impares de 1 \n\t 8.Mostrar los números múltiplos de un número\n\t9.salir" +
                           "\n favor ingrese una opción :"));
    elif(opcion==2):
        n1 = int(input("Digite el primer numero: "));
        n2 = int(input("Digite el segundo numero: "));
        n3 = int(input("Digite el tercer numero: "));

        if (n1 > n2):
            mayor = int(n1);
        else:
            mayor = int(n2);

        if (n3 > mayor):
            mayor = int(n3);

        print("El mayor número es: ", mayor);
        opcion = int(input("\n Menu\n ---------------------------\n\t" +
                           "1.Mayor y menor\n\t2.Tres valores mayor\n\t3.solicitud de tres valores multiplo\n\t4.promedio par e impar\n\t 5.Telefonia\n\t6.Mostrar la tabla de multiplicación de un valor ingresado\n\t 7.Mostrar el listado de números impares de 1 \n\t 8.Mostrar los números múltiplos de un número\n\t9.salir" +
                           "\n favor ingrese una opción :"));
    elif (opcion == 3):
        n1 = int(input("Digite el primer numero: "));
        n2 = int(input("Digite el segundo numero: "));
        n3 = int(input("Digite el tercer numero: "));
        prom=int((n1+n2+n3))/3;
        print(prom);
        if (prom%7==0):
            print("el numero es multiplo de 7 ");
        else:
            print("el numero no es multiplo de 7");
        opcion = int(input("\n Menu\n ---------------------------\n\t" +
                           "1.Mayor y menor\n\t2.Tres valores mayor\n\t3.solicitud de tres valores multiplo\n\t4.promedio par e impar\n\t 5.Telefonia\n\t6.Mostrar la tabla de multiplicación de un valor ingresado\n\t 7.Mostrar el listado de números impares de 1 \n\t 8.Mostrar los números múltiplos de un número\n\t9.salir" +
                           "\n favor ingrese una opción :"));
    elif (opcion == 4):
        n1 = int(input("Digite el primer numero: "));
        n2 = int(input("Digite el segundo numero: "));
        n3 = int(input("Digite el tercer numero: "));
        prom = int((n1 + n2 + n3)) / 3;
        if (prom%2==0):
            print("el porcentaje es par")
        else:
            print("el porcentaje es impar")
        opcion = int(input("\n Menu\n ---------------------------\n\t" +
                           "1.Mayor y menor\n\t2.Tres valores mayor\n\t3.solicitud de tres valores multiplo\n\t4.promedio par e impar\n\t 5.Telefonia\n\t6.Mostrar la tabla de multiplicación de un valor ingresado\n\t 7.Mostrar el listado de números impares de 1 \n\t 8.Mostrar los números múltiplos de un número\n\t9.salir" +
                           "\n favor ingrese una opción :"));
    elif  (opcion==5):
        print("Bienvenido a telefonia")
        nombre = str(input("Digite su nombre: "));

        mn= int(input("Digite la cantidad de minutos consumidos nacionales: "));
        mi = int(input("Digite la cantidad de minutos consumidos internacionales: "));
        tm = mn + mi
        if (tm<=25):
            print(nombre,"tus minutos han sido gratis ¡Felicidades!");
        elif(mn<=25):
            acu=mn-25;
            mi-=acu;
            total=mi*2.5;
        else:
            mn-=25;
            total=(mn*0.5)+(mi*2.5);

            print(nombre, "debes pagar esto ",total)
            opcion = int(input("\n Menu\n ---------------------------\n\t" +
                               "1.Mayor y menor\n\t2.Tres valores mayor\n\t3.solicitud de tres valores multiplo\n\t4.promedio par e impar\n\t 5.Telefonia\n\t6.Mostrar la tabla de multiplicación de un valor ingresado\n\t 7.Mostrar el listado de números impares de 1 \n\t 8.Mostrar los números múltiplos de un número\n\t9.salir" +
                               "\n favor ingrese una opción :"));
    elif(opcion==6):
        num =int(input("Ingrese un numero entero "));
        if (num<0):
            num *= -1;
        star=int(input("ingrese la posicion inicial "));
        fin=int(input("ingrese la posicion final "));
        print("Tabla_______________________de___________________",num);
        for f in range (star,fin+1):
            print(num,"*",f,"=",num * f);
    elif (opcion == 7):
        num=int(input("ingrese un numero entero "));
        print("");

        for i in range (1,num,2):
            print(i);

            opcion = int(input("\n Menu\n ---------------------------\n\t" +
                               "1.Mayor y menor\n\t2.Tres valores mayor\n\t3.solicitud de tres valores multiplo\n\t4.promedio par e impar\n\t 5.Telefonia\n\t6.Mostrar la tabla de multiplicación de un valor ingresado\n\t 7.Mostrar el listado de números impares de 1 \n\t 8.Mostrar los números múltiplos de un número\n\t9.salir" +
                               "\n favor ingrese una opción :"));

    elif (opcion == 8):
        num = int(input("Ingrese un numero entero "));
        c=0
        for i in range(1,100+1):
            if (i % num == 0):
                c += 1
                print(i);



        opcion = int(input("\n Menu\n ---------------------------\n\t" +
                                   "1.Mayor y menor\n\t2.Tres valores mayor\n\t3.solicitud de tres valores multiplo\n\t4.promedio par e impar\n\t 5.Telefonia\n\t6.Mostrar la tabla de multiplicación de un valor ingresado\n\t 7.Mostrar el listado de números impares de 1 \n\t 8.Mostrar los números múltiplos de un número\n\t9.salir" +
                                   "\n favor ingrese una opción :"));

    elif (opcion == 9):

        print("hasta pronto has Dado una opcion incorrecta")
        exit();


    else:
        print("marque una opcion Valida")
















