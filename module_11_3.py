def introspection_info(obj):
    obj_info = {
        'Type': type(obj),
        'Attributes': [],
        'Methods': [],
        'Module': None,
    }

    if hasattr(obj, '__module__'):
        obj_info['Module'] = obj.__module__

    for attribute_name in dir(obj):
        attribute = getattr(obj, attribute_name)
        if callable(attribute):
            obj_info['Methods'].append(attribute_name)
        else:
            obj_info['Attributes'].append(attribute_name)

    if isinstance(obj, type):
        obj_info['Base Classes'] = obj.__bases__

    return obj_info


number_info = introspection_info(42)
print(number_info)
