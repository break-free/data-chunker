DEF_PREFIXES = ['def ', 'async def ', 'class ']
NEWLINE = '\n'

def get_until_no_space(all_lines, i):
    """
    Get all lines until a line outside the function definition is found.
    """
    ret = [all_lines[i]]
    for j in range(i + 1, len(all_lines)):
        if len(all_lines[j]) == 0 or all_lines[j][0] in [' ', '\t', ')']:
            ret.append(all_lines[j])
        else:
            break
    return NEWLINE.join(ret)


def get_functions(filepath):
    """
    Get all functions in a Python file.
    """
    with open(filepath, 'r') as file:
        all_lines = file.read().replace('\r', NEWLINE).split(NEWLINE)
        for i, l in enumerate(all_lines):
            for prefix in DEF_PREFIXES:
                if l.startswith(prefix):
                    code = get_until_no_space(all_lines, i)
                    yield code
                    break


def python_code(file_list) -> list[str]:
    """
    Extract all .py functions from the repository.
    Returns a list of strings split by all functions and classes.
    """

    num_files = len(file_list)
    print(f'Total number of .py files: {num_files}')

    if num_files == 0:
        print('Verify code repo exists and code_root is set correctly.')
        return None

    chunks = [
        func
        for code_file in file_list
        for func in get_functions(str(code_file))
    ]

    num_funcs = len(chunks)
    print(f'Total number of functions extracted: {num_funcs}')

    return chunks