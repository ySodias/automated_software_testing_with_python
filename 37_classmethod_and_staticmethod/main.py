class ClassTest:
    def instance_method(self):
        """
        Todas as funções que ficam em uma classe e possuem self como primeiro atributo são chamadas dê:
        Instance Methods

        Caso queria usar o objeto ou criar algo do tipo
        :return:
        """
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        """
        Caso queria um método que usa a Classe para algo, então é recomendado usar class_method

        Usados como fábricas
        :return:
        """
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        """
        Não é um método e sim uma função dentro de uma classe

        Apenas para colocar um método em uma classe
        :return:
        """
        print("Called static_method.")

test = ClassTest()
test.instance_method()
ClassTest.class_method()