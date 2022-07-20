from xml.dom.minidom import Element
from js import console, document
from pyodide import create_proxy

# shorthand for document.queryselector(query)
def query (query):
    return document.querySelector(query)

num1 = query('#num1')
num2 = query('#num2')
btn = query('#submit')
result = query('#out')

def kgV (num01, num02):
    _min = min(num01, num02)
    _max = max(num01, num02)

    fac = _max

    while fac <= _max * _min:
        if fac % _min == 0:
            return fac

        fac += _max

def submit (e):
    result.innerText = kgV(int(num1.value), int(num2.value))

btn.addEventListener('click', create_proxy(submit))






