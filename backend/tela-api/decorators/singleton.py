def singleton(aclass):
    instances = {}

    def decorator(*args, **kwargs):
        if aclass not in instances:
            instances[aclass] = aclass(*args, **kwargs)
        return instances[aclass]

    return decorator
