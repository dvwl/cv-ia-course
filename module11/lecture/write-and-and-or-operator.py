# What are 'and' and 'or' operators?
    # You might occasionally want to combine test expressions to evaluate multiple conditions in one if, elif, or else statement. In this case, you'd use the Boolean operators and and or.

#%%
## The or operator
    # You can connect two Boolean, or test, expressions by using the Boolean or operator. For the entire expression to evaluate to True, at least one of the subexpressions must be true. If none of the subexpressions is true, the whole expression evaluates to False. For example, in the following expression, the entire test expression evaluates to True, because one of the conditions in the subexpressions has been met:

a = 23
b = 34
if a == 34 or b == 34:
    print(a + b)

    # If both subexpressions are true, the entire test expression also evaluates to True.

#%%
    # A Boolean expression that uses or has the following syntax:

# Python
# sub-expression1 or sub-expression2

#%%
## The and operator
    # You can also connect two test expressions by using the Boolean and operator. Both conditions in the test expression must be true for the entire test expression to evaluate to True. In any other case, the test expression is False. In the following example, the entire test expression evaluates to False, because only one of the conditions in the subexpressions is true:

a = 23
b = 34
if a == 34 and b == 34:
    print (a + b)

#%%
    # A Boolean expression that uses and has the following syntax:

# Python
# sub-expression1 and sub-expression2

## The difference between and and or
    # To highlight the difference between the two Boolean operators, you can use a truth table. A truth table shows you what the entire test expression evaluates to based on the two subexpressions.

    # AND truth table:
    #   A       B       C
    #   0       0       0
    #   0       1       0
    #   1       0       0
    #   1       1       1
    
    # OR truth table:
    #   A       B       C
    #   0       0       0
    #   0       1       1
    #   1       0       1
    #   1       1       1