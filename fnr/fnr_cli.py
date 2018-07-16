import argparse
from .context_loader.file_loader import file_loader

def parse_cla():
    parser = argparse.ArgumentParser()
    parser.add_argument("patient", help="Filename - The original input file containing the content that we would like to find and replace", type=str)
    parser.add_argument("context_file", help="Filename - An input file containing set of key value pairs to find & replace. The placeholder keywords you're looking to replace should have curly braces {} around it", type=str)
    parser.add_argument("--in-place", help="Use if you would not like a new file to be generated and you want to just replace the text in the original file", action="store_true")

    return parser.parse_args()

def main():
    print('Hello, fnr!')
    args = parse_cla()

    print('Loading the context variables from {} now...'.format(args.context_file))
    context_file = file_loader(args.context_file)
    context_file.show()
    context_dict = context_file.get_context_vars()
    print(context_dict)

    # Read in
    template = ''
    with open(args.patient, 'r') as in_file:
        template = in_file.read()

    # Write out
    out_file = (args.patient if args.in_place else 'newfile.out')
    with open(out_file, 'w') as out:
        out.write(template.format(**context_dict))

if __name__ == '__main__':
    main()
