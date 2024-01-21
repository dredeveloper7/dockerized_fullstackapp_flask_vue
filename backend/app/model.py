from modelomapper import ui_element
GMD = dict()

def main(model_document):
    GMD = model_document
    result = sum(3,4)
    return None

@ui_element(GMD, pointer="sum_results")
def sum(a, b):
    result = a + b
    return result


