# Script to write the codeblocks from a markdown document into Python and R files

import os
import re
import nbformat

# Python code block pattern:  ```{code-tab} py* ```
# R code block pattern: ```{code-tab} r R * ```

# Book page name
bpname = "logistic-regression"

# Book folder name
fname = "spark-functions"

# Path for markdown file
path_md = "ons-spark\\" + fname + "\\" + bpname + ".md"

# Output paths
path_o = "ons-spark\\raw-notebooks\\" + bpname + "\\"

if(os.path.exists(path_o) == False):
   os.mkdir(path_o)

path_o_py = path_o + bpname + ".ipynb"
path_o_r = path_o + "r_input.R"

# Read in markdown document

if(os.path.exists(path_md)):
    with open(path_md, encoding="utf8") as f:
        md_doc = f.read()
else: 
    raise ValueError("No path exists")

#### Extract Python code blocks and write to notebook

py_regex = r"(?<=\```{code-tab} py)[^\```]+"

py_blocks = re.findall(py_regex, md_doc)

notebook = nbformat.v4.new_notebook()

cells = []

for block in py_blocks:
    cell = nbformat.v4.new_code_cell(block)
    cells.append(cell)

notebook['cells'] = cells

nbformat.write(notebook, path_o_py)

#### Extract R code blocks and write to R file

r_regex = r"(?<=\```{code-tab} r R)[^\```]+"

r_blocks = re.findall(r_regex, md_doc)

with open(path_o_r, "w") as outfile:
    outfile.write('\n'.join(str(block) for block in r_blocks))