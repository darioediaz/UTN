package utnfc.isi.backend;

import utnfc.isi.backend.util.ListaArrayBasica;
import utnfc.isi.backend.util.ListaArrayMejorada;

/**
 * Clase para incluir un simple main() de prueba para la clase ListaArregloMejorada.
 * 
 * @author philip.
 * @version 2023.
 */
public class PruebaListaArrayMejorada
{
    public static void main(String args[])
    {
        // un arreglo auxiliar de nombres...
        String nombres[] = {"Rafa", "Enzo", "Nacho", "Octi", "Kiko", "Nico", "Gero", "Taro",
                            "Simon", "Lorenzo", "Rulo", "Lopez", "Lucho", "Luca", "Juan"};

        // creación de un ArrayList...
        ListaArrayMejorada la = new ListaArrayMejorada(5);
        System.out.println("Lista inicial: " + la);
        
        // inserción de cadenas...
        for (String s : nombres) {
            la.agregar(s);
        }
        System.out.println("Luego de invocar a agregar(): " + la);

        System.out.println("Contenido usando get: ");
        for (int i = 0; i < la.size(); i++)
        {
            String x = (String) la.get(i);
            System.out.println(x);
        }

        System.out.println("Contenido usando iterador: ");         
        ListaArrayMejorada.IteradorLineal it = la.iterador();
        while(it.hayMas())
        {
            String x = (String) it.getActual();
            System.out.println(x);
            it.siguiente();
        }

    }
}
