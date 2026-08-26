import modules.printing_functions

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

modules.printing_functions.print_models(unprinted_designs, completed_models)
modules.printing_functions.show_completed_models(completed_models)