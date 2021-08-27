#!/usr/bin/env python
# coding: utf-8

# In[2]:


def sub(Q):
    Q1 = Q.replace("OR" ,"gates.OR")
    Q2 = Q1.replace("AND" ,"gates.AND")
    Q3 = Q2.replace("NOT" ,"gates.NOT")
    Q4 = Q3.replace("NAD" ,"gates.NAD")
    Q5 = Q4.replace("NR" ,"gates.NR")
    Q6 = Q5.replace("XR" ,"gates.XR")
    Q7 = Q6.replace("XNR" ,"gates.XNR")
    
def OR(A,B):
    if A == 0 and B ==0:
        return 0
    else:
        return 1
def AND(A,B):
    if A == 1 and B ==1:
        return 1
    else:
        return 0
def NOT (A):
    if A == 0 :
        return 1 
    else :
        return 0
def NAD(A,B):
    if A == 1 and B ==1:
        return 0
    else:
        return 1
def NR(A,B):
    if A == 0 and B ==0 :
        return 1 
    else :
        return 0
def XR(A,B):
    if A == B :
        return 0
    else :
        return 1
def XNR(A,B):
    if A == B :
        return 1
    else :
        return 0

