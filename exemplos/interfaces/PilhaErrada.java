import java.util.Vector;
import java.util.EmptyStackException;

class PilhaErrada<T> implements Pilha<T> {

	Vector<T> itens = new Vector<T>();
	public void colocar(T item) {
		itens.add(item);
	}

    public T retirar() throws EmptyStackException {
    	if (itens.size() > 0)
    		// BUG: remove sempre o primeiro item, violando a regra do LIFO
    		return itens.remove(0);
    	else
    		throw new EmptyStackException();
    }

    public static void main(String[] args) {
    	PilhaErrada<Integer> p = new PilhaErrada<Integer>();
    	p.colocar(11);
    	p.colocar(22);
    	System.out.println("retirado: " + p.retirar());
    }

}
