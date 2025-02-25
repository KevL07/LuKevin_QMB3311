# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Name: 
#
# Date:
# 
##################################################
#
# Sample Script for Midterm Examination: 
# Function Definitions
#
##################################################
"""



"""
##################################################
##################################################
# Note: there should be no printing or calculations
# in this script, aside from function definitions. 
# Save those for another script that would
# execute the scripts (to run the doctests)
# and imports the modules to test the functions.
##################################################
##################################################
"""






##################################################
# Import Required Modules
##################################################

# import name_of_module

##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

#--------------------------------------------------
# Question 1
# Functions from Previous Assignments
#--------------------------------------------------

def CESutility(good_x: float, good_y: float, r: float) -> float:
    utility = (good_x**r + good_y**r)**(1/r)
    return utility

def CESutility_valid(x:float, y:float,r:float) -> float:
    error = False
    if x < 0:
        error = True
        print("x cannot be negative.")
    if y < 0:
        error = True
        print("y cannot be negative.")     
    if r <= 0:
        error = True
        print("r must be positive.")
    if error == True:
        return None
    
    ans = CESutility(x, y, r)
    return ans

def CESutility_in_budget(x:float, y:float, r:float, p_x:float, p_y:float, w:float) -> float:
    if p_x < 0 or p_y < 0:
        print("Price cannot be negative.")
        return None
    if(p_x * x + p_y * y) > w:
        print("The consumer basket of goods cannot cost more than wealth.")
        return None
    
    return CESutility_valid(x, y, r)

#--------------------------------------------------
# Question 2
# New Functions
#--------------------------------------------------

# Exercise 4

def max_CES_util(x_min:float, x_max:float, y_min:float, y_max:float, step:float, r:float, p_x:float, p_y:float, w:float) -> float:
    """
    Calculates max utility given x_min, x_max, y_mn, y_max, r, pr
    
    >>> 
    >>> 
    >>> 


    """
    
     xy_max = max_CES_xy(x_min, x_max, y_min, y_max, step, 
        r, p_x, p_y, w)
    
    Max_util = CESutility_in_budget(xy_max[0], xy_max[1], r, p_x, p_y, w)
    
    return max_util




    

# Only function definitions above this point. 


##################################################
# Test the examples in your docstrings
##################################################


# Question 2: Test using the doctest module. 

if __name__ == "__main__":

    with open("my_CES_midterm.py", "w") as f:
        print(doctest.testmod(verbose = True), file = f)
# Make sure to include examples in your docstrings
# with the proper formatting. 

# Test all functions with three examples each. 

# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 


# The tests are implemented below -- but only
# when the script is run, not when it is imported. 

    






##################################################
# End
##################################################
