/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package utnfc.isi.back.banco;

/**
 *
 * @author philip
 */
public class CuentaInversion extends Cuenta
{
    private float mTasa = 0.11F; //(float)0.11;

    public CuentaInversion(int pNro, double pSaldo)
    {
        super(pNro, pSaldo);
        
    }
  
    public float getTasa()
    {
        return mTasa;
    }

    public void setTasa(float mTasa)
    {
        mTasa = mTasa;

    }

    public void actualizar()
    {
        mSaldo += mSaldo * mTasa;

    }
    
    public boolean retirar(double pMonto)
    {
        boolean wRes = false;
        //Es Cuenta Inversion evaluar saldo directamente
        if (pMonto <= mSaldo)
        {
            mSaldo -= pMonto;
            wRes = true;
        }
        return wRes;    
    }
    
    public String toString()
    {
        StringBuffer wRes = new StringBuffer();
        wRes.append(super.toString());
        wRes.append("\n\tTipo:\tInversi�n");
        wRes.append("\n\tTasa:\t").append(mTasa);
      
        return wRes.toString();
    
    }
    
}
