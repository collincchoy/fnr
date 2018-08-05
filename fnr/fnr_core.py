from .context_loaders import file_loader

def load_keywords_to_be_replaced(args):
    print('Loading the context variables from {} now...'.format(args.context_file))
    context_file = file_loader(args.context_file)
    context_file.show()
    return context_file.get_context_vars()

def find_and_replace(context, template):
    return template.format(**context)