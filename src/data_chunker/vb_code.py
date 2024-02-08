# Defines sections of vb code to be split into chunks
object_types = tuple(['Module ', "Public Class ", "Partial Class ", "Namespace "])
object_types_end = tuple(['End Module', "End Class", "End Namespace"])

def vb_code(file_list) -> list[str]:
    """
    Extract all .vb code from the repository.
    Returns a list of strings.
    """
    chunks = []  # List to store code chunks for each module
    codeString = ""

    for file in file_list:
        with open(file, 'r') as file:
            for line in file:

                if line.startswith(object_types):
                    capture = True
                    codeString = codeString + line
                
                elif capture:
                    codeString = codeString + line

                    if line.startswith(object_types_end):
                        chunks.append(codeString)
                        capture = False
                        codeString = ""
    
    return chunks