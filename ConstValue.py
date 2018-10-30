from enum import Enum

class ConstValue(object):
    class ConstError(TypeError):
        pass
    class ConstCaseError(ConstError):
        pass
    def __setter__(self, name, value):
        if self.__dict__.has_key(name):
            raise (self.ConstError, 'Not allowed change const.{value}'.format(value=name))
        if not name.isupper():
            raise (self.ConstCaseError, "Const's name is not all uppercase")
        self.__dict__[name] = value


class ALIGNX(Enum):
    center = 1
    left = 2
    right = 3


class ALIGNY(Enum):
    center = 1
    top = 2
    bottom = 3


#使用
# ConstValue.GOOGLE = 100
# ALIGNX = Enum('ALIGNX', ('center', 'left', 'right'))
# ALIGNY = Enum('ALIGNX', ('center', 'top', 'bottom'))
# ALIGNY = ('center', 'top', 'bottom')
