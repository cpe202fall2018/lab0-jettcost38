# Name: Jett Costibolo
# Student ID: jcostibo
# Date: 21 September 2018
#
# Lab 0
# Section 15
# Purpose of Lab: To introduce and become familiar with GitHub and Python Syntax

def weight_on_planets():
    pounds = float(input("What do you weigh on earth? "))
    mars_pounds = pounds * 0.38
    jupiter_pounds = pounds * 2.34
    print("\nOn Mars you would weigh %.2f pounds.\nOn Jupiter you would weigh %.2f pounds. " % (mars_pounds, jupiter_pounds))


if __name__ == '__main__':
    weight_on_planets()