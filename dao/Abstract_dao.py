import pickle
from abc import ABC


class Abstract_dao(ABC):
    def __init__(self, datasource='') :
        self.__datasource = datasource
        self.__cache= {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource, 'rb'))

    def add(self, key, obj):
        self.__cache[key] = obj
        self.__dump()

    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            pass

    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.__dump()
        except KeyError:
            pass

    def get_all(self):
        return self.__cache.values()

    @property
    def cache(self):
        return self.__cache
    @cache.setter
    def cache(self, cache): 
        self.__cache = cache