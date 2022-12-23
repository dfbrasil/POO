import abc

"""interface"""
class Nuisance(abc.ABC):

    """método abstrato"""
    @abc.abstractmethod
    def annoy(): 
        pass 