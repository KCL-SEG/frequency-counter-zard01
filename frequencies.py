"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for i in items:
      i=str(i)
      num=items.count(i)
      frequencies.update({i: num})
    return frequencies
