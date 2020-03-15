>>> x.age # Но извлечение атрибута проверяет также классы
>>> x. __ diet __ [ ’ age 1 ] # Индексирование словаря не производит поиск в иерархии наследования
>>> х. __ class __ # Связь экземпляра с классом
>>> гес. __ bases __ # Связь с суперклассами
# Fetching all methds/properties - use __class__ and then ___dict__, then __dict__ against all __bases__ 
# OR use dir(obj)
