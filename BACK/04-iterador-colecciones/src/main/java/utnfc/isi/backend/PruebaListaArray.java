package utnfc.isi.backend;

import utnfc.isi.backend.util.ListaArrayBasica;

/**
 * Clase para incluir un simple main() de prueba para la clase ListaArregloBasica.
 * 
 * @author philip.
 * @version 2023.
 */
public class PruebaListaArray
{
    public static void main(String args[])
    {
        // un arreglo auxiliar de nombres...
        String nombres[] = {"Rafa", "Enzo", "Nacho", "Octi", "Kiko", "Nico", "Gero", "Taro",
                            "Simon", "Lorenzo", "Rulo", "Lopez", "Lucho", "Luca", "Juan"};

        // creación de un ArrayList...
        ListaArrayBasica la = new ListaArrayBasica(5);
        System.out.println("Lista inicial: " + la);
        
        // inserción de cadenas...
        for (String s : nombres) {
            la.agregar(s);
        }
        System.out.println("Luego de invocar a agregar(): " + la);
        
        // eliminación de una cadena...
        la.quitar(3);
        System.out.println("Luego de invocar a quitar() una vez: " + la);
        
        // eliminación masiva usando remove():
        while(la.size()>0)
        {
            la.quitar(0);
        }
        System.out.println("Luego de invocar a quitar() muchas veces: " + la);
        
        // regeneración de la lista inicial...
        for (String s : nombres) {
            la.agregar(s);
        }
        System.out.println("Luego de invocar a agregar(): " + la);

        // acceso a un componente individual...
        String nom = (String) la.get(4);
        System.out.println("Nombre recuperado con get(): " + nom);
        
        // cambio de un componente individual...
        la.set(6, "Adriano");
        System.out.println("Contenido luego de usar set(): " + la);
        
        la.insertar(0, "Pancho");
        System.out.println("Luego de insertar en casilla 3: " + la);
        
        int id = la.size();
        la.insertar(id, "Bauty");
        System.out.println("Luego de insertar en casilla " +  id + ": " + la);

        System.out.println("Contenido usando get: ");
        for (int i = 0; i < la.size(); i++)
        {
            String x = (String) la.get(i);
            System.out.println(x);
        }

        System.out.println("Contenido usando iterador: ");         
        la.iniciarIterador();
        while(la.hayMas())
        {
            String x = (String) la.getActual();
            System.out.println(x);
            la.siguiente();
        }
        
        la.clear();
        // regeneración de la lista inicial...
        for(String s : nombres)
        {
            la.agregar(s);
        }
        System.out.println("Luego de invocar a clear() y volver a generarla: " + la);
        
        String nombre = "Nico";
        boolean r = la.contains(nombre);
        System.out.println("El nombre " + nombre + " está en la lista??? " + r);
        
    }
}
