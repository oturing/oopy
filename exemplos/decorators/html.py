

def faznegrito(fn):
    def decorada(name = 'world'):
        return "<b>" + fn(name) + "</b>"
    return decorada

@faznegrito
def hello(name = 'world'):
    return "hello "+name

print hello()
print hello('Juca')

hello = faznegrito(hello)

print hello('Fulano')
