import sys
import pytest

def two():
    return 2

def one():
    return 1

def test1():
    assert one() == 1
    
def test2():
    assert two() == 2
if __name__ == "__main__":
    test1()
    test2()
    
    
