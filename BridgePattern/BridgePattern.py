from __future__ import annotations
import abc

class RemoteFunction(abc.ABC):
    def __init__(self, name:str, tv_function:TVFunction) -> None:
        super().__init__()
        self.__name = name
        self.__tv_function = tv_function
        
    def __repr__(self) -> str:
        return f"{self.name} Controller with {self.tv_function.__class__.__name__} TV Function"
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
        
    @property
    def tv_function(self):
        return self.__tv_function
    
    @tv_function.setter
    def tv_function(self, value:TVFunction):
        self.__tv_function = value
        
    @abc.abstractmethod
    def on(self):
        """ Implement Method """
        
    @abc.abstractmethod
    def off(self):
        """ Implement Method """
        
    @abc.abstractmethod
    def setChannel(self, channel:int):
        """ Implement Method """
        
class TVFunction(abc.ABC):
    def __init__(self) -> None:
        super().__init__()
        
    @abc.abstractmethod
    def on(self):
        """ Implement Method """
        
    @abc.abstractmethod
    def off(self):
        """ Implement Method """
        
    @abc.abstractmethod
    def setChannel(self, channel:int):
        """ Implement Method """

class SonyTVFunction(TVFunction):
    def __init__(self) -> None:
        super().__init__()
        
    def on(self):
        return super().on()
    
    def off(self):
        return super().off()
    
    def setChannel(self, channel: int):
        return super().setChannel(channel)
    
class LGTVFunction(TVFunction):
    def __init__(self) -> None:
        super().__init__()
        
    def on(self):
        return super().on()
    
    def off(self):
        return super().off()
    
    def setChannel(self, channel: int):
        return super().setChannel(channel)
        
class ConcreteRemoteFunction(RemoteFunction):
    def __init__(self, name, tv_function:TVFunction) -> None:
        super().__init__(name, tv_function)

    def on(self):
        return self.tv_function.on()
    
    def off(self):
        return self.tv_function.off()
    
    def setChannel(self, channel: int):
        return self.tv_function.setChannel(channel)
    
if __name__ == "__main__":
    remote_controller = ConcreteRemoteFunction("living_room",SonyTVFunction())
    print (remote_controller) # living_room Controller with SonyTVFunction TV Function
    remote_controller.tv_function = LGTVFunction()
    print (remote_controller) # living_room Controller with LGTVFunction TV Function