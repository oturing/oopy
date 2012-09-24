import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

import java.util.EmptyStackException;

public class PilhaTest {
    PilhaSimples<String> pVazia;
    PilhaSimples<Integer> p;
    @Before
    public void setUp() {
        pVazia = new PilhaSimples<String>();
        p = new PilhaSimples<Integer>();
        p.colocar(10);
        p.colocar(20);
        p.colocar(30);
    }

    @Test
    public void retiradas() {
        assertEquals((Integer)30, p.retirar());
        assertEquals((Integer)20, p.retirar());
        assertEquals((Integer)10, p.retirar());
    }

    @Test
    public void colocadoRetirado() {
        pVazia.colocar("alfa");
        assertEquals("alfa", pVazia.retirar());
    }

    @Test
    public void colocadosRetirado() {
        pVazia.colocar("alfa");
        pVazia.colocar("beta");
        assertEquals("beta", pVazia.retirar());
    }

    @Test(expected=EmptyStackException.class)
    public void retiradaInvalida() {
        String o = pVazia.retirar();
    }

    public static void main(String args[]) {
      org.junit.runner.JUnitCore.main("PilhaTest");
    }
}

