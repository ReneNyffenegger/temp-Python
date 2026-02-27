# Collection of simple python code snippets

## Goal

 - Maintain a _simple_ collection of simple python code snippets that demonstrate how the language or 3rd party modules can be used
 - Typically, a python script should demonstrate one particular usage (but there can be exceptions)

## Code Guidelines

 - Each .py file must begin with `# vim: foldmethod=marker foldmarker={{{,}}}` on the first line.
   If the file has a shebang, put the vim modeline on the 2nd line instead.

 - Use vim fold markers for functions: place `# {{{` on the same line as `def`, and
   `# }}}` after the function's final line.

 - Use the same fold markers for other syntactic structures such as `if` or `for` statements
   if they span more than say five lines.

 - Use camelCase for all variables and function names, except prompted otherwise. (TODO Rene: think about again because this seems to be very controversial)

 - Generally, indentation should be done with three spaces (but I deviate from this rule myself)

 - The code deliberately violates PEP 8 because I think it does no good for demonstration purposes.

 - Avoid `if __name__ == "__main__":` guards in simple example scripts

 - Reduce error handling and other not strictly necessary clutter in the code so that the viewer can
   focus on the one concept presented.
