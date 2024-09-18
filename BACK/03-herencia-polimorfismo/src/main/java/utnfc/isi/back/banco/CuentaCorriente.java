/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package utnfc.isi.back.banco;

/**
 *
 * @author philip
 */
public class CuentaCorriente extends Cuenta
{
    private boolean mDesc;

    public CuentaCorriente(int pNro, double pSaldo, boolean pDesc)
    {
        super(pNro, pSaldo); //invocar el constructor de la clase base
        mDesc = pDesc;

    }
    
    public CuentaCorriente(int pNro, double pSaldo)
    {
       this(pNro, pSaldo, false);
       
    }
    
    public boolean isDesc()
    {
        return mDesc;
    }

    public void setDesc(boolean mDesc)
    {
        this.mDesc = mDesc;
    }

    public boolean retirar(double pMonto)
    {
        boolean wRes = false;
        //Es Cuenta Corriente evaluar descubierto...
        if (mDesc || pMonto <= mSaldo)
        {
            mSaldo -= pMonto;
            wRes = true;
        }

        return wRes;
    }
   
    
    public String toString()
    {
        StringBuilder wRes = new StringBuilder();
        wRes.append(super.toString())
            .append("\n\tTipo:\tCorriente")
            .append("\n\tDescubierto:\t");
        if (mDesc)
            wRes.append("Si");
        else
            wRes.append("No");
        return wRes.toString();
    }
    
}
