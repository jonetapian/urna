class CodigoUrna:
    def __init__(self, codigo_u):
        self.__codigo_u = codigo_u
    @property
    def codigo_u(self):
        return self.__codigo_u

    @codigo_u.setter
    def codigo_u(self, codigo_u):
        self.__codigo_u = codigo_u