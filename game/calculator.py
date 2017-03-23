#!/usr/bin/env python
# coding=utf-8

# copy from http://blog.chriscabin.com/coding-life/python/python-in-real-world/1101.html
# Thanks
class Stack(object):
    """
    The structure of a Stack.
    The user don't have to know the definition.
    """
    def __init__(self):
        self.__container = list()
    def __is_empty(self):
        """
        Test if the stack is empty or not
        :return: True or False
        """
        return len(self.__container) == 0
    def push(self, element):
        """
        Add a new element to the stack
        :param element: the element you want to add
        :return: None
        """
        self.__container.append(element)
    def top(self):
        """
        Get the top element of the stack
        :return: top element
        """
        if self.__is_empty():
            return None
        return self.__container[-1]
    def pop(self):
        """
        Remove the top element of the stack
        :return: None or the top element of the stack
        """
        return None if self.__is_empty() else self.__container.pop()
    def clear(self):
        """
        We'll make an empty stack
        :return: self
        """
        self.__container.clear()
        return self

class Calculator(object):
    """
    A simple calculator, just for fun
    """
    def __init__(self):
        self.__exp = ''
    def __validate(self):
        """
        We have to make sure the expression is legal.
        1. We only accept the `()` to specify the priority of a sub-expression. Notes: `[ {` and `] }` will be
        replaced by `(` and `)` respectively.
        2. Valid characters should be `+`, `-`, `*`, `/`, `(`, `)` and numbers(int, float)
        - Invalid expression examples, but we can only handle the 4th case. The implementation will
        be much more sophisticated if we want to handle all the possible cases.:
            1. `a+b-+c`
            2. `a+b+-`
            3. `a+(b+c`
            4. `a+(+b-)`
            5. etc
        :return: True or False
        """
        if not isinstance(self.__exp, str):
            print('Error: {}: expression should be a string'.format(self.__exp))
            return False
        # Save the non-space expression
        val_exp = ''
        s = Stack()
        for x in self.__exp:
            # We should ignore the space characters
            if x == ' ':
                continue
            if self.__is_bracket(x) or self.__is_digit(x) or self.__is_operators(x) \
                    or x == '.':
                if x == '(':
                    s.push(x)
                elif x == ')':
                    s.pop()
                val_exp += x
            else:
                print('Error: {}: invalid character: {}'.format(self.__exp, x))
                return False
        if s.top():
            print('Error: {}: missing ")", please check your expression'.format(self.__exp))
            return False
        self.__exp = val_exp
        return True
    def __convert2postfix_exp(self):
        """
        Convert the infix expression to a postfix expression
        :return: the converted expression
        """
        # highest priority: ()
        # middle: * /
        # lowest: + -
        converted_exp = ''
        stk = Stack()
        for x in self.__exp:
            if self.__is_digit(x) or x == '.':
                converted_exp += x
            elif self.__is_operators(x):
                converted_exp += ' '
                tp = stk.top()
                if tp:
                    if tp == '(':
                        stk.push(x)
                        continue
                    x_pri = self.__get_priority(x)
                    tp_pri = self.__get_priority(tp)
                    if x_pri > tp_pri:
                        stk.push(x)
                    elif x_pri == tp_pri:
                        converted_exp += stk.pop() + ' '
                        stk.push(x)
                    else:
                        while stk.top():
                            if self.__get_priority(stk.top()) != x_pri:
                                converted_exp += stk.pop() + ' '
                            else:
                                break
                        stk.push(x)
                else:
                    stk.push(x)
            elif self.__is_bracket(x):
                converted_exp += ' '
                if x == '(':
                    stk.push(x)
                else:
                    while stk.top() and stk.top() != '(':
                        converted_exp += stk.pop() + ' '
                    stk.pop()
        # pop all the operators
        while stk.top():
            converted_exp += ' ' + stk.pop() + ' '
        return converted_exp
    def __get_result(self, operand_2, operand_1, operator):
        if operator == '+':
            return operand_1 + operand_2
        elif operator == '-':
            return operand_1 - operand_2
        elif operator == '*':
            return operand_1 * operand_2
        elif operator == '/':
            if operand_2 != 0:
                return operand_1 / operand_2
            else:
                print('Error: {}: divisor cannot be zero'.format(self.__exp))
                return None
    def __calc_postfix_exp(self, exp):
        """
        Get the result from a converted postfix expression
        e.g. 6 5 2 3 + 8 * + 3 + *
        :return: result
        """
        assert isinstance(exp, str)
        stk = Stack()
        exp_split = exp.strip().split()
        for x in exp_split:
            if self.__is_operators(x):
                # pop two top numbers in the stack
                r = self.__get_result(stk.pop(), stk.pop(), x)
                if r is None:
                    return None
                else:
                    stk.push(r)
            else:
                # push the converted number to the stack
                stk.push(float(x))
        return stk.pop()
    def __calc(self):
        """
        Try to get the result of the expression
        :return: None or result
        """
        # Validate
        if self.__validate():
            # Convert, then run the algorithm to get the result
            return self.__calc_postfix_exp(self.__convert2postfix_exp())
        else:
            return None
    def get_result(self, expression):
        """
        Get the result of an expression
        Suppose we have got a valid expression
        :return: None or result
        """
        self.__exp = expression.strip()
        return self.__calc()
    """
    Utilities
    """
    @staticmethod
    def __is_operators(x):
        return x in ['+', '-', '*', '/']
    @staticmethod
    def __is_bracket(x):
        return x in ['(', ')']
    @staticmethod
    def __is_digit(x):
        return x.isdigit()
    @staticmethod
    def __get_priority(op):
        if op in ['+', '-']:
            return 0
        elif op in ['*', '/']:
            return 1

# usage
c = Calculator()
print('result: {:f}'.format(c.get_result('8+10/2')))
print(int(c.get_result('8+10')))
# output:
result: 0.666000
