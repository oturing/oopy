import java.util.EmptyStackException;

interface Pilha<T> {

    void colocar(T item);

    T retirar() throws EmptyStackException;

}
