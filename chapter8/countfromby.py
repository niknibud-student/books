class CountFromBy:
    
    def __init__(self, val: int=0, incr: int=1) -> None:
        self.value = val
        self.increment = incr
        
    def increase(self) -> None:
        self.value += self.increment
    
    def __repr__(self) -> str:
        return str(self.value)