/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package utnfc.isi.back.banco2;

/**
 *
 * @author philip
 */
public abstract class Cuenta
{

    private int mNro;
    protected double mSaldo;

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

    public abstract boolean retirar(double pMonto);
    
}
