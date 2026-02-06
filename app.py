import streamlit as st
from reportlab.pdfgen import canvas
import datetime

st.title("HISTORIAL CLINICO")

nombre = st.text_input("Nombre")
observacion = st.text_input("Observación")
diagnostico = st.text_input("Diagnóstico")
antecedentes = st.text_input("Antecedentes médicos")

peso = st.number_input("Peso (kg)", min_value=1.0)
altura = st.number_input("Altura (m)", min_value=0.5)

if st.button("Generar reporte"):

    imc = peso / (altura ** 2)

    if imc < 18.5:
        estado = "Bajo peso"
        guia = "Comer más calorías saludables."
    elif imc < 25:
        estado = "Normal"
        guia = "Mantener dieta balanceada."
    elif imc < 30:
        estado = "Sobrepeso"
        guia = "Reducir azúcares y fritos."
    else:
        estado = "Obesidad"
        guia = "Dieta baja en calorías."

    st.write(f"IMC: {imc:.2f}")
    st.write(f"Estado: {estado}")
    st.write(f"Guía: {guia}")

    pdf = f"reporte_{nombre}.pdf"
    c = canvas.Canvas(pdf)

    y = 800
    c.drawString(100, y, "HISTORIAL CLINICO")

    y -= 30
    c.drawString(100, y, f"Nombre: {nombre}")

    y -= 20
    c.drawString(100, y, f"Observación: {observacion}")

    y -= 20
    c.drawString(100, y, f"Diagnóstico: {diagnostico}")

    y -= 20
    c.drawString(100, y, f"Antecedentes: {antecedentes}")

    y -= 30
    c.drawString(100, y, f"IMC: {imc:.2f}")

    y -= 20
    c.drawString(100, y, f"Estado: {estado}")

    y -= 20
    c.drawString(100, y, f"Guía: {guia}")

    y -= 20
    c.drawString(100, y, str(datetime.date.today()))

    c.save()

    with open(pdf, "rb") as f:
        st.download_button("Descargar PDF", f, file_name=pdf)
