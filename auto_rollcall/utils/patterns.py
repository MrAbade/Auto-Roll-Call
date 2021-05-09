class Singleton(type):
    _mapper_class_instance = dict()

    def __call__(cls, *args, **kwds):
        if not cls in cls._mapper_class_instance:
            new_instance = super().__call__(*args, **kwds)
            cls._mapper_class_instance[cls] = new_instance
        return cls._mapper_class_instance[cls]
