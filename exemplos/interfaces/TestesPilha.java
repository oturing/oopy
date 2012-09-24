package br.com.turing;

/**
 * @author Luciano Ramalho
 */

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

import java.util.NoSuchElementException;

public class VetorTest {
    Pilha p;
    @Before
    public void setUp() {
        p = new Pilha();
        vb1 = new Vetor<BigInteger>();
        vb1.Insere(BigInteger.ONE);
        vs3 = new Vetor<String>();
        vs3.Insere("a");
        vs3.Insere("b");
        vs3.Insere("c");
        vs10 = new Vetor<String>(10);
    }

    /**
     * Testes do método Tamanho, classe Vetor.
     */
    @Test
    public void tamanhos() {
        Vetor<Boolean> v = new Vetor<Boolean>();
        assertEquals(0, v.Tamanho());
        assertEquals(0, v0.Tamanho());
        assertEquals(1, vb1.Tamanho());
        assertEquals(3, vs3.Tamanho());
        assertEquals(10, vs10.Tamanho());
    }

    /**
     * Testes do construtor que cria cópia de um Vetor.
     */
    @Test
    public void copia(){
        Vetor<String> v = new Vetor<String>(vs3);
        assertEquals(vs3.Tamanho(), v.Tamanho());
        assertEquals(vs3.get(0), v.get(0));
        assertEquals(vs3.get(1), v.get(1));
        assertEquals(vs3.get(2), v.get(2));
    }
    @Test
    public void copiaVazio(){
        Vetor<Object> v = new Vetor<Object>(v0);
        assertEquals(v0.Tamanho(), v.Tamanho());
    }

    /**
     * Testes do método público Insere(t), classe Vetor.
     */
    @Test
    public void insereNoVazio() {
        Integer i = 42;
        Vetor<Integer> v = new Vetor<Integer>();
        v.Insere(i);
        assertEquals(1, v.Tamanho());
        assertEquals(i, v.get(0));
    }
    @Test
    public void insereVarios() {
        Vetor<String> v = new Vetor<String>();
        v.Insere("abacaxi");
        v.Insere("banana");
        assertEquals(2, v.Tamanho());
        assertEquals("abacaxi", v.get(0));
        assertEquals("banana", v.get(1));
    }
    @Test
    public void insereTrecos() {
        Vetor<Treco> v = new Vetor<Treco>();
        v.Insere(new Treco("gizmo"));
        v.Insere(new Treco("rebimboca"));
        v.Insere(new Treco("noete"));
        assertEquals(3, v.Tamanho());
        assertEquals("noete", v.get(2).getNome());
    }

    /**
     * Testes do método get, classe Vetor.
     */
    @Test
    public void getDentro() {
        assertEquals("a", vs3.get(0));
        assertEquals("b", vs3.get(1));
        assertEquals("c", vs3.get(2));
        assertEquals(BigInteger.ONE, vb1.get(0));
        assertNull(vs10.get(0));
        assertNull(vs10.get(9));
    }

    @Test(expected=IndexOutOfBoundsException.class)
    public void getNegativo() {
        String s = vs3.get(-1);
    }
    @Test(expected=IndexOutOfBoundsException.class)
    public void getFora() {
        String s = vs3.get(3);
    }

    @Test(expected=IndexOutOfBoundsException.class)
    public void getNoVazio() {
        Object nada = v0.get(0);
    }

    /**
     * Testes do método get, classe Vetor.
     */
    @Test
    public void setDentro() {
        vs3.set(1, "x");
        assertEquals("x", vs3.get(1));
        vs10.set(9, "casa");
        assertEquals("casa", vs10.get(9));
    }
    @Test(expected=IndexOutOfBoundsException.class)
    public void setSentinela() {
        vs3.set(-1, "z");
    }
    @Test(expected=IndexOutOfBoundsException.class)
    public void setNegativo() {
        vs3.set(-2, "z");
    }
    @Test(expected=IndexOutOfBoundsException.class)
    public void setFora() {
        vs3.set(3, "z");
    }

    @Test(expected=IndexOutOfBoundsException.class)
    public void setNoVazio() {
        v0.set(0, new Object());
    }
    /**
     * Testes do método público Insere(t, index), classe Vetor.
     */
    @Test
    public void insereDentro() {
        vs3.Insere("#", 0);
        assertEquals(4, vs3.Tamanho());
        assertEquals("#", vs3.get(0));
        assertEquals("a", vs3.get(1));
        assertEquals("b", vs3.get(2));
        vs3.Insere("%", 2);
        assertEquals(5, vs3.Tamanho());
        assertEquals("a", vs3.get(1));
        assertEquals("%", vs3.get(2));
        assertEquals("b", vs3.get(3));
        vs3.Insere("!", 4);
        assertEquals(6, vs3.Tamanho());
        assertEquals("b", vs3.get(3));
        assertEquals("!", vs3.get(4));
        assertEquals("c", vs3.get(5));
    }
    @Test(expected=IndexOutOfBoundsException.class)
    public void insereFora() {
        vb1.Insere(BigInteger.ONE, 1);
    }

     /**
     * Testes do método Remove(indice), classe Vetor.
     */
    @Test
    public void removeDoMeio() {
        vs3.Remove(1);
        assertEquals(2, vs3.Tamanho());
        assertEquals("a", vs3.get(0));
        assertEquals("c", vs3.get(1));
    }
    @Test
    public void removeDoInício() {
        vs3.Remove(0);
        assertEquals(2, vs3.Tamanho());
        assertEquals("b", vs3.get(0));
        assertEquals("c", vs3.get(1));
    }
    @Test(expected=IndexOutOfBoundsException.class)
    public void removeDoFim() {
        vs3.Remove(2);
        assertEquals(2, vs3.Tamanho());
        assertEquals("a", vs3.get(0));
        assertEquals("b", vs3.get(1));
        String s = vs3.get(2);
    }
    @Test
    public void removeÚnico() {
        vb1.Remove(0);
        assertEquals(0, vb1.Tamanho());
    }

     /**
     * Testes do método Remove(t), classe Vetor.
     */
    @Test
    public void removeQual() {
        vs3.Remove("b");
        assertEquals(2, vs3.Tamanho());
        assertEquals("a", vs3.get(0));
        assertEquals("c", vs3.get(1));
        vb1.Remove(BigInteger.ONE);
        assertEquals(0, vb1.Tamanho());
        vs10.Remove(null);
        assertEquals(9, vs10.Tamanho());
        vs10.Remove(null);
        assertEquals(8, vs10.Tamanho());
    }

    @Test(expected=NoSuchElementException.class)
    public void removeInexistente() {
        vs3.Remove("z");
    }

    /**
     * Testes do método RemoveTodos, classe Vetor.
     */
    @Test
    public void removeTodosUm() {
        vs3.RemoveTodos("a");
        assertEquals("b", vs3.get(0));
        assertEquals("c", vs3.get(1));
        assertEquals(2, vs3.Tamanho());
    }
    @Test
    public void removeTodosVários() {
        Vetor<Integer> v = new Vetor<Integer>();
        v.Insere(1);
        v.Insere(2);
        v.Insere(1);
        v.Insere(3);
        v.Insere(1);
        assertEquals(5, v.Tamanho());
        v.RemoveTodos(1);
        assertEquals(2, v.Tamanho());
    }
    @Test(expected=NoSuchElementException.class)
    public void removeTodosInexistente() {
        vs3.RemoveTodos("z");
    }

    /* testes em Vetor carregado de nulls */
    @Test(expected=NoSuchElementException.class)
    public void removeTodosInexistente2() {
        vs10.RemoveTodos("z");
    }

    @Test
    public void removeTodosVáriosNulls() {
        vs10.RemoveTodos(null);
        assertEquals(0, vs10.Tamanho());
    }

    /**
     * Testes do método BuscaBinaria, classe Vetor.
     */
    @Test(expected=UnsupportedOperationException.class)
    public void nãoPodeBuscaBináriaEmNãoOrdenado() {
        Vetor<String> v = new Vetor<String>();
        v.Insere("B");
        v.Insere("A");
        v.BuscaBinaria("A");
    }
    @Test(expected=ClassCastException.class)
    public void nãoPodeBuscaBináriaEmVetorComNulls() {
        vs10.BuscaBinaria("a");
    }
    @Test
    public void buscaBináriaResultadoImediato() {
        assertEquals(1, vs3.BuscaBinaria("b"));
    }
    @Test
    public void buscasBinárias() {
        assertEquals(0, vs3.BuscaBinaria("a"));
        assertEquals(2, vs3.BuscaBinaria("c"));
        assertEquals(-1, vs3.BuscaBinaria("z"));
    }
    @Test
    public void maisBuscasBinárias() {
        Vetor<String> v = new Vetor<String>();
        v.Insere("");
        v.Insere("A");
        v.Insere("AA");
        v.Insere("AAA");
        v.Insere("AAAA");
        assertEquals(0, v.BuscaBinaria(""));
        assertEquals(2, v.BuscaBinaria("AA"));
        assertEquals(4, v.BuscaBinaria("AAAA"));
        assertEquals(-1, v.BuscaBinaria("AB"));
    }

    /**
     * Testes do método Ordena, classe Vetor.
     */

    @Test
    public void ordenaDesordenado() {
        Vetor<String> v = new Vetor<String>();
        v.Insere("caqui");
        v.Insere("abacaxi");
        v.Insere("banana");
        v.Ordena();
        assertEquals("abacaxi", v.get(0));
        assertEquals("banana", v.get(1));
        assertEquals("caqui", v.get(2));
    }
    @Test
    public void ordenaDesordenadoOutro() {
        Vetor<String> v = new Vetor<String>();
        v.Insere("caqui");
        v.Insere("banana");
        v.Insere("abacaxi");
        v.Ordena();
        assertEquals("abacaxi", v.get(0));
        assertEquals("banana", v.get(1));
        assertEquals("caqui", v.get(2));
    }

    /************************************************************************
     * Testes dos métodos auxiliares da classe Vetor.                       *
     ************************************************************************/

    @Test
    public void getCelulas() {
        assertSame(v0.getSentinela(), v0.getCelula(-1));
        assertSame(vs3.getSentinela(), vs3.getCelula(-1));
        assertSame(BigInteger.ONE, vb1.getCelula(0).carga);
        assertEquals("a", vs3.getCelula(0).carga);
        assertEquals("b", vs3.getCelula(1).carga);
        assertEquals("c", vs3.getCelula(2).carga);
    }
    @Test(expected=IndexOutOfBoundsException.class)
    public void getCelulaInexistente() {
            vs3.getCelula(3);
    }
    @Test(expected=IndexOutOfBoundsException.class)
    public void getCelulaInexistenteÍndiceNegativo() {
            v0.getCelula(-2);
    }
    @Test
    public void buscarCelulasExistentes() {
        assertEquals("a", vs3.buscarCelula("a").carga);
        assertEquals("c", vs3.buscarCelula("c").carga);
        assertSame(BigInteger.ONE, vb1.buscarCelula(BigInteger.ONE).carga);
    }
    @Test
    public void buscarCelulaPrimeiraOcorrência() {
        Vetor<String> v = new Vetor<String>();
        v.Insere("bola");
        v.Insere("bola");
        assertSame(v.getSentinela().próxima, v.buscarCelula("bola"));
    }
    @Test
    public void buscarCelulaPrimeiraOcorrênciaNull() {
        assertSame(vs10.getSentinela().próxima, vs10.buscarCelula(null));
    }
    @Test
    public void buscarCelulasInexistentes() {
        assertNull(vs3.buscarCelula("#"));
        assertNull(vb1.buscarCelula(null));
        assertNull(vs10.buscarCelula("zebra"));
        assertNull(v0.buscarCelula("zebra"));
    }
    @Test
    public void buscarCelulasAnterioresExistentes() {
        assertEquals("a", vs3.buscarCelulaAnterior("b").carga);
        assertSame(vs3.getSentinela(), vs3.buscarCelulaAnterior("a"));
        assertSame(vb1.getSentinela(), vb1.buscarCelulaAnterior(BigInteger.ONE));
    }
    @Test
    public void buscarCelulasAnterioresInexistentes() {
        assertNull(vs3.buscarCelulaAnterior("#"));
        assertNull(vb1.buscarCelulaAnterior(null));
        assertNull(vs10.buscarCelulaAnterior("zebra"));
        assertNull(v0.buscarCelulaAnterior("zebra"));
    }

    /**
     * Testes do método ordenado, classe Vetor.
     */
    @Test
    public void ordenadoUmOuMenos() {
        assertTrue(v0.ordenado());
        assertTrue(vb1.ordenado());
        Vetor<String> v = new Vetor<String>();
        v.Insere("zebra");
        assertTrue(v.ordenado());
        Vetor<String> vazio = new Vetor<String>();
        assertTrue(vazio.ordenado());
    }
    @Test
    public void ordenadoVários() {
        assertTrue(vs3.ordenado());
        Vetor<String> v = new Vetor<String>();
        v.Insere("abacaxi");
        v.Insere("zebra");
        assertTrue(v.ordenado());
    }
    @Test
    public void nãoOrdenado() {
        Vetor<String> v = new Vetor<String>();
        v.Insere("banana");
        v.Insere("abacaxi");
        assertFalse(v.ordenado());
    }
    @Test(expected=ClassCastException.class)
    public void nãoPodeOrdenarComNull() {
        boolean b = vs10.ordenado();
    }
    @Test(expected=ClassCastException.class)
    public void nãoPodeOrdenarComNulleNãoNull() {
        Vetor<String> v = new Vetor<String>();
        v.Insere(null);
        v.Insere("A");
        boolean b = v.ordenado();
    }
    @Test(expected=ClassCastException.class)
    public void nãoPodeOrdenarComTrecosNãoComparable() {
        Vetor<Treco> v = new Vetor<Treco>();
        v.Insere(new Treco("gizmo"));
        v.Insere(new Treco("rebimboca"));
        v.Insere(new Treco("noete"));
        boolean b = v.ordenado();
    }
    @Test
    public void valorMínimo() {
        assertEquals("a", vs3.valorMínimo(0));
        assertEquals("b", vs3.valorMínimo(1));
        assertEquals("c", vs3.valorMínimo(2));
        assertEquals(BigInteger.ONE, vb1.valorMínimo(0));
    }
    @Test
    public void valorMínimoEmVetorDesordenado() {
        Vetor<String> v = new Vetor<String>();
        v.Insere("uva");        // 0
        v.Insere("banana");     // 1
        v.Insere("rato");       // 2
        v.Insere("bicicleta");  // 3
        v.Insere("zebra");      // 4
        assertEquals("banana", v.valorMínimo(0));
        assertEquals("banana", v.valorMínimo(1));
        assertEquals("bicicleta", v.valorMínimo(2));
        assertEquals("bicicleta", v.valorMínimo(3));
        assertEquals("zebra", v.valorMínimo(4));
    }
}

