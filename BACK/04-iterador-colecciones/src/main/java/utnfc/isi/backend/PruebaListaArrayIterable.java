package utnfc.isi.backend;

import utnfc.isi.backend.util.generics.ListaArrayIterable;

import java.util.Iterator;

/**
 * Clase para incluir un simple main() de prueba para la clase ListaArregloMejorada parametrizable.
 * 
 * @author philip.
 * @version 2023.
 */
public class PruebaListaArrayIterable
{
    public static void main(String args[])
    {
        // un arreglo auxiliar de nombres...
        String nombres[] = {"Rafa", "Enzo", "Nacho", "Octi", "Kiko", "Nico", "Gero", "Taro",
                            "Simon", "Lorenzo", "Rulo", "Lopez", "Lucho", "Luca", "Juan"};

        // creación de un ArrayList...
        ListaArrayIterable<String> la = new ListaArrayIterable<>(5);
        System.out.println("Lista inicial: " + la);
        
        // inserción de cadenas...
        for (String s : nombres) {
            la.agregar(s);
        }
        System.out.println("Luego de invocar a agregar(): " + la);

        System.out.println("\nContenido usando get: ");
        for (int i = 0; i < la.size(); i++)
        {
            String x = (String) la.get(i);
            System.out.println(x);
        }

        System.out.println("\nContenido usando iterador, ahora iterador formal: ");
        Iterator<String> it = la.iterator();
        while(it.hasNext())
        {
            String x = it.next();
            System.out.println(x);
        }

        System.out.println("\nPero al ser iterable también podemos usar foreach: ");
        for (String x : la) {
            System.out.println(x);
        }


    }
}
