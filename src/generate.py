import os
import nbformat as nbf


def ktx_to_dict(input_file, keystarter="<", commentstarter="#"):
    """Parse keyed text to python dictionary."""
    answer = dict()

    with open(input_file, "r+", encoding="utf-8") as f:
        lines = f.readlines()

    k, val = "", ""
    for line in lines:
        if line.startswith(commentstarter):
            continue

        if line.startswith(keystarter):
            k = line.replace(keystarter, "").strip()
            val = ""
        else:
            val += line

        if k:
            answer[k] = val.strip()

    return answer


def dict_to_ktx(input_dict, output_file, keystarter="<"):
    """Store python dictionary as keyed text."""
    with open(output_file, "w+") as f:
        for k, val in input_dict.items():
            f.write(f"{keystarter} {k}\n")
            f.write(f"{val}\n\n")


HEADERS = ktx_to_dict(os.path.join("src", "data", "headers.ktx"))
QDHA = ktx_to_dict(os.path.join("src", "data", "exercises100.ktx"))


def create_jupyter_notebook(destination_filename="100_polars_exercises.ipynb"):
    """
    Programmatically create jupyter notebook with questions saved in source/.
    """

    # Create cells sequence
    nb = nbf.v4.new_notebook()

    nb["cells"] = []

    # Add header
    nb["cells"].append(nbf.v4.new_markdown_cell(HEADERS["header"]))
    nb["cells"].append(nbf.v4.new_markdown_cell(HEADERS["sub_header"]))
    nb["cells"].append(nbf.v4.new_markdown_cell(HEADERS["jupyter_instruction"]))

    # Add initialisation
    nb["cells"].append(nbf.v4.new_code_cell("%run src/initialise.py"))

    # Add questions and empty spaces for answers
    n = 1
    while f"q{n}" in QDHA:
        nb["cells"].append(nbf.v4.new_markdown_cell(f"#### {n}. " + QDHA[f"q{n}"]))

        if f"d{n}" in QDHA:
            nb["cells"].append(nbf.v4.new_code_cell(QDHA[f"d{n}"]))


        nb["cells"].append(nbf.v4.new_code_cell(""))
        n += 1

    # Delete file if one with the same name is found
    if os.path.exists(destination_filename):
        os.remove(destination_filename)

    # Write sequence to file
    nbf.write(nb, destination_filename)


if __name__ == "__main__":
    create_jupyter_notebook()
