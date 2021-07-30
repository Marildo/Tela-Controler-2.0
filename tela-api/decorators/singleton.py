def singleton(aclass):
    instances = {}

    def get_class(*args, **kwargs):
        if aclass not in instances:
            instances[aclass] = aclass(*args, **kwargs)
        return instances[aclass]

    return get_class
