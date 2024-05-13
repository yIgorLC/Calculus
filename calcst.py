# calculadora streamlit
import streamlit as st

result = 0

st.title(':violet[Calculator]')
st.write("")
st.write("")
st.write("")
st.write("*Welcome to the best :rainbow[CALCULATOR] ever!*")

n1 = st.number_input("Number one", value=None, placeholder="write right here... ")
n2 = st.number_input("Number two", value=None, placeholder="writer right here...")

st.write("")
st.write("")


def soma(n1, n2):
    return n1 + n2


def subt(n1, n2):
    return n1 - n2


def multi(n1, n2):
    return n1 * n2


def divi(n1, n2):
    return n1 / n2


def mód(n1, n2):
    return n1 % n2


def potenc(n1, n2):
    return n1 ** n2


col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Somar", type="primary"):
        result = (soma(n1, n2))

    if st.button("Subtrair", type="primary"):
        result = (subt(n1, n2))
with col2:
    if st.button("Dividir", type="primary"):
        result = (divi(n1, n2))

    if st.button("Multiplicar", type="primary"):
        result = (multi(n1, n2))

with col3:
    if st.button("Potenciação", type="primary"):
        result = (potenc(n1, n2))

    if st.button("Módulo", type="primary"):
        result = (mód(n1, n2))

st.write("")
st.write("")

st.write("The result is equal: ", result)