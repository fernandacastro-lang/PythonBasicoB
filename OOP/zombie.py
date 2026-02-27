from enemigo import * 

class zombie(enemigo):
    def _int_(self, puntos_energia=10, ataque=1):
        super()._init_(tipo_enemigo= 'zombie', puntos_energia=puntos_energia, ataque=1)

        def habla(self):
            print("hummmm...")

            def propagar_enfermedad(self):
                print("el zombie esta tratando de propagar la enfermedad!!")

