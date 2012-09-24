import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

import java.util.EmptyStackException;

public class PilhaErradaTest {
    PilhaErrada<String> pVazia;
    PilhaErrada<Integer> p;
    @Before
    public void setUp() {
        pVazia = new PilhaErrada<String>();
        p = new PilhaErrada<Integer>();
        p.colocar(10);
        p.colocar(20);
        p.colocar(30);
    }

    @Test
    public void retiradas() {
        // a PilhaErrada é FIFO, e não LIFO como deveria ser uma pilha
        assertEquals((Integer)10, p.retirar());
        assertEquals((Integer)20, p.retirar());
        assertEquals((Integer)30, p.retirar());
    }

    @Test
    public void colocadoRetirado() {
        pVazia.colocar("alfa");
        assertEquals("alfa", pVazia.retirar());
    }

    @Test
    public void colocadosRetirado() {
        // a PilhaErrada é FIFO, e não LIFO como deveria ser uma pilha
        pVazia.colocar("alfa");
        pVazia.colocar("beta");
        assertEquals("alfa", pVazia.retirar());
    }

    @Test(expected=EmptyStackException.class)
    public void retiradaInvalida() {
        String o = pVazia.retirar();
    }

    public static void main(String args[]) {
      org.junit.runner.JUnitCore.main("PilhaErradaTest");
    }
}

