"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    items= list(map(str, items))
    for i in items:
      i=str(i)
      num=items.count(i)
      frequencies.update({i: num})
    return frequencies
