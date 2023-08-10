
class Circular:

    #Construtor
    def __init__(self, inicial_data, prev, prox):
        self.data = inicial_data
        self.prev = prev     # inicial essa variavel nao aoontara para ninguem
        self.prox = prox
    
    #obtendo os dados do meu armazenamento
    def get_data(self):
        return self.data
    
    #atualizando os dados do meu armazenamento
    def set_data(self, new_data):
        self.data = new_data 

class Double_List:
    
    #implementa a classe 
    #(lista encadeada nao ordenada)
    def __init__(self):
        """cia nós iniciais e finais"""
        self.header = Circular(None, None, None)
        # foot é o final da minha lista foot == pé
        self.foot = Circular(None, None, None)
        self.header.prox = self.foot
        self.foot.prev = self.header
        self.size = 0
        
    #verifico se a minha lista esta vazia
    def is_empty(self):
        return self.size == 0 
    
    def __len__(self):
        return self.size
    
    #insere um nó "conteiner" em minha lista
    def insert_between(self, item, predecessor, sucessor):
        """aqui eu ja estou passando como minha instancia, os sucessor e o meu predecessor
        a minha logica de alocacao esta aqui. meus dois nos sao as ambas variaveis"""
        newest = Circular(item, predecessor, sucessor)
        predecessor.prox = newest
        sucessor.prev = newest
        self.size += 1
        return newest
    
    def delete_Circular(self, apaga):
        """remove um nó intermediario da lista, header nem foot NUNCA PODERA SER REMOVIDOS"""
        predecessor = Circular.prev
        sucessor = Circular.prox
        predecessor.prox = sucessor
        sucessor.prev = predecessor
        self.size -= 1
        element = Circular.data
        apaga.prev = apaga.prox = apaga.element = None    
        return element
    
    # insere o primeiro elemento "como se fosse o promeiro vagao, 'o maquinista' "
    def insert_first(self, data):
        """nó deve entrar ontre o header e o header.prox,
        mas pode ser mudado para so entrar no header e no foot"""
        self.insert_between(data, self.header, self.header.prox)
        
    #inseri o ultimo valor
    def insert_last(self, data):
        """insere o vagao no ultimo elemento"""
        self.insert_between(data, self.foot, self.foot.prev) #caso der errado a insercao tiarar a porra o prev
        
    #remove o vagao do maquinista
    def delete_first(self):
        if self.is_empty():
            raise Exception('lista vazia!')
        return self.delete_Circular(self.header.prox)
    
    #remove o final 
    def delete_last(self):
        if self.is_empty():
            raise Exception('lista vazia')
        return self.delete_last(self.foot.prev)
    
    #imprime cade elemento da lista
    def print_lista(self):
        """aponta a referencia para a cabeca"""
        temp = self.header.prox
        X = []
        while temp.prox != None:
            X.append(temp.data)
            temp = temp.prox
        return X
    
if __name__ == "__main__":
    """aqui eu ja instanciei e testei tudo para poupar tempo
    codigo pronto e testato"""
    lista_criada = Double_List()
    print(lista_criada.is_empty())
    #inserindo no inicio
    lista_criada.insert_first(1)
    lista_criada.insert_first(2)
    lista_criada.insert_first(3)
    print(lista_criada.print_lista())
    print(len(lista_criada))
    print(lista_criada.is_empty())
    #inserindo no final
    lista_criada.insert_last(4)
    lista_criada.insert_last(5)
    lista_criada.insert_last(6)
    print(lista_criada.print_lista())
    print(len(lista_criada))
    lista_criada.delete_first()
    lista_criada.delete_last()
    print(lista_criada.print_lista())
    print(len(lista_criada))
    