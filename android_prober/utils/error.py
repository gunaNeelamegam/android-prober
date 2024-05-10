def not_implemented(cls):
    def decorator(*args, **kwargs):
        raise NotImplementedError(f"{cls.__name__} ({key}) Not Supported")
            
    for key, value in vars(cls).items():
        if callable(value):        
            setattr(cls, key, decorator(value))
    return cls