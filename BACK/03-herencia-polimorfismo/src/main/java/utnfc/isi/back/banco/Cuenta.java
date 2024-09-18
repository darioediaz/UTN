/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package utnfc.isi.back.banco;

/**
 *
 * @author philip
 */
public class Cuenta
{

    private int mNro;
    protected double mSaldo;

    public Cuenta()
    {}
    
    public Cuenta(int pNro, double pSaldo)
    {
        mNro = pNro;
        mSaldo = pSaldo;
        
    }
    
    public double consultarSaldo()
    {
        return mSaldo;
    }

    public void depositar(double pMonto)
    {
        if (pMonto > 0)
            mSaldo += pMonto;
    }

    public int getNro()
    {
        return mNro;
    }
    
    public String toString()
    {
        StringBuffer wRes = new StringBuffer();
        
        wRes.append("\tNro:\t" + mNro);
        wRes.append("\n\tSaldo:\t" + mSaldo);
      
        return wRes.toString();
     }
     
    public boolean retirar (double monto)
    {
        return false;
    }
    
     
    
}
