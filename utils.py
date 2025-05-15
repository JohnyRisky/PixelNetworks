class Base:
    """Parent class for A and B classes"""
    def value(self):
        return self._a


class Error(Exception):
    """Custom Error class"""
    def __str__(self):
        return "error one"
    

class UndefinedError(Exception):
    """Custom Error class"""
    def __str__(self):
        return "None prohibited"
    
    def message(self, digit: int = None):
        """Processes custom error cases"""
        match digit:
            case 1: return 'error message one'
            case 2: return 'error message two'
            case _: return 'error message'