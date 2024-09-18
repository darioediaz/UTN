/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package utnfc.isi.back.banco2;

/**
 *
 * @author philip
 */
public class Prueba
{
    
    public static void main(String args[])
    {
        //CuentaVieja aux = new CuentaVieja(1234, 10000, 1, true, 0);
        Cuenta aux = ((Math.random() >= 0.5)?new CuentaCorriente((int)(Math.random()*8000 + 1000), 10000, true):new CuentaInversion((int)(Math.random()*8000 + 1000), 10000)) ;
        Cliente cli1 = new Cliente(1, "Pepe", aux);
        
        aux = ((Math.random() >= 0.5)? new CuentaCorriente((int)(Math.random()*8000 + 1000), 10000, true):new CuentaInversion((int)(Math.random()*8000 + 1000), 10000));
        Cliente cli2 = new Cliente(2, "juan", aux);
        aux = ((Math.random() >= 0.5)? new CuentaCorriente((int)(Math.random()*8000 + 1000), 10000, true):new CuentaInversion((int)(Math.random()*8000 + 1000), 10000));
        Cliente cli3 = new Cliente(3, "don", aux);
        
        cli1.getCuenta().depositar(1000);
        cli2.getCuenta().depositar(1000);
        cli3.getCuenta().depositar(1000);
        
        cli1.getCuenta().retirar(12000);
        cli2.getCuenta().retirar(12000);
        cli3.getCuenta().retirar(12000);
 
        //Mensual de actualizaciones
        if (cli1.getCuenta().getClass() == CuentaInversion.class)
        //if (cli1.getCuenta() instanceof CuentaInversion)
        {
            ((CuentaInversion)cli1.getCuenta()).actualizar();
            System.out.println("Cli 1 Es de Inversión");
        }
        else
            System.out.println("Cli 1 No es de Inversión");
        
        if (cli2.getCuenta() instanceof CuentaInversion)
        {
            CuentaInversion aux1 = (CuentaInversion)cli2.getCuenta();
            aux1.actualizar();
            System.out.println("Cli 2 Es de Inversión");
        }
        else
            System.out.println("Cli 2 No es de Inversión");
        
        if (cli3.getCuenta() instanceof CuentaInversion)
        {
            ((CuentaInversion)cli3.getCuenta()).actualizar();
            System.out.println("Cli 3 Es de Inversión");
        }
        else
            System.out.println("Cli 3 No es de Inversión");
        
        
        
        
        System.out.println(cli1);
        System.out.println(cli2);
        System.out.println(cli3);
    }
}
