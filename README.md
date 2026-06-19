# Three Address Code Generator

## Project Description

This project implements a simple Three Address Code (TAC) Generator in Python.

The program accepts arithmetic expressions and converts them into Three Address Code using temporary variables.

## Features

* Expression Tokenization
* Temporary Variable Generation
* Multiplication Support
* Division Support
* Operator Precedence Handling
* Chained Arithmetic Expressions
* Parentheses Handling

## Example 1

Input:

a = b + c * d

Output:

t1 = c * d
t2 = b + t1
a = t2

## Example 2

Input:

a = b + c - d

Output:

t1 = b + c
t2 = t1 - d
a = t2

## Example 3

Input:

a = ( b + c ) * d

Output:

t1 = b + c
t2 = t1 * d
a = t2

## Technologies Used

* Python
* Git
* GitHub

## Author

Mudasir Raza
