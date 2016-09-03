_prefix = 'nnlib.model.'

def get(module_name, class_name = None):
	if class_name is None:
		class_name = module_name

	class_model = __import__(_prefix + module_name, fromlist=['']).__dict__['Model']
	return class_model()

