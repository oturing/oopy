import java.util.Vector;
import java.util.EmptyStackException;

class PilhaSimples<T> implements Pilha<T> {

	Vector<T> itens = new Vector<T>();
	public void colocar(T item) {
		itens.add(item);
	}

    public T retirar() throws EmptyStackException {
    	if (itens.size() > 0)
    		return itens.remove(itens.size()-1);
    	else
    		throw new EmptyStackException();
    }

}
