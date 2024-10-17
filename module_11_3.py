def introspection_info(obj):
    info = {'type': str(type(obj)),'attributes': [],
        'methods': [],'module': '','other_properties': {}}

    if hasattr(obj, '__module__'):
        info['module'] = obj.__module__

    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    info['attributes'] = attributes

    metods = [metod for metod in dir(obj) if callable(getattr(obj, metod)) and not metod.startswith("__")]
    info['metods'] = metods

    if isinstance(obj, (int, float)):
        info['other_properties']['is_number'] = True
    elif isinstance(obj, str):
        info['other_properties']['is_string'] = True
    elif isinstance(obj, list):
        info['other_properties']['length'] = len(obj)

    return info


class ExamplClass:
    def __init__(self):
        self.attribute1 = "value1"
        self.attribute2 =15

    def metod1(self):
        pass

    def metod2(self, param):
        return param


example_instance = ExamplClass()

example_info = introspection_info(example_instance)
print(example_info)

number_info = introspection_info(15)
print(number_info)
