from person import Person

class Telemarketing(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def give_sales_pitch(self):
        return f"{self.get_name()} pressiona os outros a comprar coisas."

    def annoy(self):
        return f"{self.get_name()} irrita ao dar um discurso de vendas"
