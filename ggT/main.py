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

def ggT (num01, num02):
    _min = min(num01, num02)

    div = _min

    while div > 0:
        if num01 % div == 0 and num02 % div == 0:
            return div
        div -= 1

def submit (e):
    result.innerText = ggT(int(num1.value), int(num2.value))

btn.addEventListener('click', create_proxy(submit))






