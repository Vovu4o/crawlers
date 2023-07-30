from abc import abstractmethod


class BaseCrawler:
    """Abstract crawler implements pattern 'Request - Parse - Save'"""
    @abstractmethod
    def request(self, *args, **kwargs):
        pass 

    @abstractmethod
    def parse(self, *args, **kwargs):
        pass 

    @abstractmethod
    def save(self, *args, **kwargs):
        pass


class BaseRequest:
    """Abstract Request"""

    @abstractmethod
    def get(self, *args, **kwargs):
        pass 

    @abstractmethod
    def post(self, *args, **kwargs):
        pass

    @abstractmethod
    def options(self, *args, **kwargs):
        pass 

    @abstractmethod
    def delete(self, *args, **kwargs):
        pass