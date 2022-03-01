**No longer maintained. See #2**

---

# Cobra
My own programming written in Python (now you see why it's called Cobra).

## Requirments
Right now, no external modules are needed. You just need the Python programming language.

## Usage
### How to run
All you have to do is:
```shell
python execute.py <name-of-cobra-file>
```
You also have 2 other options:
#### Windows
```batch
cobra <name-of-cobra-file>
```
#### Mac or Linux
```bash
./cobra.sh <name-of-cobra-file>
```

I have an `example.cobra` file in the root directory of this repository.
You can run it by running the following command in your terminal:
```shell
python execute.py example.cobra
```
or by using the other two options above: [Windows](#windows), [Mac or Linux](#mac-or-linux).

### Syntax
The basic syntax for a Cobra program is: `name of function any arguments to be passed in to the function`. That's a bit confusing. So for example, if you type `say Hello, World!`, `say` is the function and `Hello, World!` is the argument. To create a comment, use the # sign. For example: `# This is a comment. It will be ignored by Cobra`.

### Functions
The current functions for Cobra are:
#### say
Description: Print to the console
<br>
Arguments:
- text: Text to print out to the console.

Example: `say Hello, World!`

#### create_var
Description: Creates a variable
<br>
Arguments:
- name: Variable name
- value: Variable value. Can be an existing variable or string.

Example: `create_var test "This is a test"`

#### create_function
Description: Creates a function
<br>
Arguments:
- name: Function name

Example:
```
create_function say_hello:
    say "hello"
```

To execute a function:
```
# You just type the function's name
say_hello
```

#### import
Description: Imports a file into your current executing program.
<br>
Arguments:
- filename: The name of the file you want to import. Can end with .cobra or not.

Example: `import helloworld`

Inside helloworld.cobra, there is a function called `testing_func`. To run it, just type it in like usual.
```
import helloworld
testing_func
```
The `import` function will always import everything as of this commit.

#### run_python
Description: Runs a line of Python code in the Cobra environment.
<br>
Arguments:
- query: The query that you want to run.

Example: `run_python "print('Hello World!')"`

This is meant for compatibility with Python.

For examples of all of these functions, consult the `example.cobra` file.
