>>> x.age # Но извлечение атрибута проверяет также классы
>>> x. __ diet __ [ ’ age 1 ] # Индексирование словаря не производит поиск в иерархии наследования
>>> х. __ class __ # Связь экземпляра с классом
>>> гес. __ bases __ # Связь с суперклассами
# Fetching all methds/properties - use __class__ and then ___dict__, then __dict__ against all __bases__ 
# OR use dir(obj)
>>> len(dir(bob) )
32
>>> list (name for name in dir (bob) if not name, start s with (' __ '))
['gatherAttrs', 'giveRaise', 'job', 'lastName', 'name', 'pay']
# __some_method - pseudo-closed attributes of a class
class AttrDisplay:
    def gatherAttrs(self):
        attrs = []
        for key in sorted (self.__dict__):
            attrs.append('{} = {}'.format(key, getattr(self,key)))
        return ', '.join(attrs)
    def __repr__ (self) :
        return '[{}: {}]'.format(self.__class__.__name__, self.gatherAttrs())