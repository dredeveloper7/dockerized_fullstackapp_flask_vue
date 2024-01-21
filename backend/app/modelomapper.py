def ui_element(model_document, pointer):
    def decorator_wrapper(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            model_document[pointer] = result
            return result

        return wrapper
    return decorator_wrapper

if __name__ == "__main__":
    pass