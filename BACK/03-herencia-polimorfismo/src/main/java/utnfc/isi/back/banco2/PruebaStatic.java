package utnfc.isi.back.banco2;


public class PruebaStatic
{
    private int a;
    public static int b = 5;
    
    public void setA(int x)
    {
        a = x;
        b = x;
    }
    
    public static void setB(int x)
    {
        b = x;
        //a = x; no compila porque no sabr�a a qu� instancia cambiarle el valor de a
    }
    
    public int getA()
    {
        return a;
    }
    
    public int getB()
    {
        return b;
    }


}