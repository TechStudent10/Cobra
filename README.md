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
The basic syntax for a Cobra program is: `name of function any arguments to be passed in to the function` for example: `say Hello, World!`. `say` is the function and `Hello, World!` is the argument.

### Functions
The current functions for Cobra are:
- say: Print to the console
Arguments: text.
