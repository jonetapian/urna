class Urna:
    def __init__(self, codigo_u, estado_federativo, munincipio, zona, secao, turno, data_homologacao, data_encerramento):
        self.__codigo_u = codigo_u
        self.__estado_federativo = estado_federativo
        self.__munincipio = munincipio
        self.__zona = zona
        self.__secao = secao
        self.__turno = turno
        self.__data_homologacao = data_homologacao
        self.__data_encerramento = data_encerramento

    @property
    def codigo_u(self):
        return self.__codigo_u
    
    @codigo_u.setter
    def codigo_u(self,codigo_u):
        self.__codigo_u = codigo_u
    
    @property
    def estado_federativo(self):
        return self.__estado_federativo
    
    @estado_federativo.setter
    def estado_federativo(self,estado_federativo):
        self.__estado_federativo = estado_federativo
    
    @property
    def munincipio(self):
        return self.__munincipio
    
    @munincipio.setter
    def munincipio(self,munincipio):
        self.__munincipio = munincipio
    
    @property
    def zona(self):
        return self.__zona
    
    @zona.setter
    def zona(self,zona):
        self.zona = zona

    @property
    def secao(self):
        return self.__secao

    @secao.setter
    def secao(self, secao):
        self.__secao = secao

    @property
    def turno(self):
        return self.__turno
    
    @turno.setter
    def turno(self,turno):
        self.__turno = turno
   
    @property
    def data_homologacao(self):
        return self.__data_homologacao
    
    @data_homologacao.setter
    def data_homologacao(self,data_homologacao):
        self.__data_homologacao = data_homologacao
    
    @property
    def data_encerramento(self):
        return self.__data_encerramento
    
    @data_encerramento.setter
    def data_encerramento(self, data_encerramento):
        self.__data_encerramento = data_encerramento
