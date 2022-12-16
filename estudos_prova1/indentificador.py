import abc

class Indentificador(abc.ABC): #uma classe ABStrata não pode ser instanciada !

    @abc.abstractmethod
    def metodo_abstrato(self):
        pass