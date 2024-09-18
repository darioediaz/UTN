/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package utnfc.isi.back.banco2;

/**
 *
 * @author philip
 */
public class Cliente
{
    private int mNro;
    private String mNombre;
    private Cuenta mCta;

    public int getNro()
    {
        return mNro;
    }

    public String getNombre()
    {
        return mNombre;
    }

    public void setNombre(String mNombre)
    {
        this.mNombre = mNombre;
    }
    
    public Cuenta getCuenta()
    {
        return mCta;
    }
    
    public Cliente(int pNro, String pNombre, Cuenta pCta)
    {
        this.mNro = pNro;
        this.mNombre = pNombre;
        this.mCta = pCta;
           
    }
    
    public Cliente(int pNro, String pNombre, int pNroCta, double pSaldo)
    {
        this.mNro = pNro;
        this.mNombre = pNombre;
        this.mCta = new CuentaInversion(pNroCta, pSaldo);
    }
    
    public Cliente(int pNro, String pNombre, int pNroCta, double pSaldo, boolean pDesc)
    {
        this.mNro = pNro;
        this.mNombre = pNombre;
        this.mCta = new CuentaCorriente(pNroCta, pSaldo, pDesc);
    }
    
    public String toString()
    {
       StringBuffer wRes = new StringBuffer();
       wRes.append("****************************");
       wRes.append("\nNro:\t" + mNro);
       wRes.append("\nNombre:\t" + mNombre );
       wRes.append("\nCuenta:\n" + mCta);
       
       return wRes.toString();
       
    }
    
    
}
