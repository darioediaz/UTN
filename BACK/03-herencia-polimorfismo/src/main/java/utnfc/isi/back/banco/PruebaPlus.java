/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package utnfc.isi.back.banco;

/**
 *
 * @author philip
 */
public class PruebaPlus
{
    
    public static void main(String args[])
    {
        Cuenta aux = new CuentaCorriente(1234, 10000, true);
        Cliente cli1 = new Cliente(1, "Pepe", aux);
        aux = new CuentaInversion(4321, 10000);
        Cliente cli2 = new Cliente(2, "juan", aux);
        aux = new CuentaInversion(2435, 10000);
        Cliente cli3 = new Cliente(3, "don", aux);
        
        cli1.getCuenta().depositar(1000);
        cli2.getCuenta().depositar(1000);
        cli3.getCuenta().depositar(1000);
 
        if (cli1.getCuenta().retirar(12000))
            System.out.println("cli1 pudo");
        else
            System.out.println("cli1 No pudo");
        
        if (cli2.getCuenta().retirar(12000))
            System.out.println("cli2 pudo");
        else
            System.out.println("cli2 No pudo");
         
            
            
        if (cli3.getCuenta().retirar(1000))
            System.out.println("cli3 pudo");
        else
            System.out.println("cli3 No pudo");
        
        
        CuentaInversion auxI;
        if (cli1.getCuenta() instanceof CuentaInversion)
        {
            auxI = (CuentaInversion) cli1.getCuenta();
            auxI.actualizar();
            System.out.println("Cli1 Actualiz�");
        }
        else
            System.out.println("Cli1 no es Inversion");
            
        if (cli2.getCuenta() instanceof CuentaInversion)
        {
            ((CuentaInversion)cli2.getCuenta()).actualizar();
                System.out.println("Cli2 Actualiz�");

        }
        else
            System.out.println("Cli2 no es Inversion");
            
        if (cli3.getCuenta() instanceof CuentaInversion)
        {
            ((CuentaInversion)cli3.getCuenta()).actualizar();
            System.out.println("Cli3 Actualiz�");

        }
       else
            System.out.println("Cli3 no es Inversion");
                        
        System.out.println(cli1);
        System.out.println(cli2);
        System.out.println(cli3);
    }
}
