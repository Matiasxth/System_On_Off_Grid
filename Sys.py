import streamlit as st
import math

def calcular_produccion(panel_potencia, horas_sol, eficiencia, ampliacion):
    return panel_potencia * horas_sol * eficiencia * (1 + ampliacion / 100)

def calcular_baterias(energia_diaria, dias_autonomia, profundidad_descarga, voltaje_bateria, ampliacion):
    capacidad = (energia_diaria * dias_autonomia) / (profundidad_descarga * voltaje_bateria)
    return capacidad * (1 + ampliacion / 100)

def calcular_inversor(potencia_sistema, ampliacion):
    return potencia_sistema * (1 + ampliacion / 100)

def calcular_caida_tension(corriente, longitud, resistencia, area):
    return (2 * corriente * longitud * resistencia) / area

st.title("Sistema de Cálculos On-Grid y Off-Grid")

# Entrada de datos
st.header("Datos de Entrada")

# Datos comunes
panel_potencia = st.number_input("Potencia nominal del panel (Wp):", min_value=0.0, step=10.0, value=400.0)
horas_sol = st.number_input("Horas solares pico (h/día):", min_value=0.0, step=0.1, value=5.0)
eficiencia = st.number_input("Eficiencia total del sistema (%):", min_value=0.0, step=0.1, value=75.0) / 100
ampliacion = st.number_input("Porcentaje de ampliación (%):", min_value=0.0, step=1.0, value=20.0)

# Datos específicos para Off-Grid
st.subheader("Datos para Sistemas Off-Grid")
energia_diaria = st.number_input("Energía diaria requerida (kWh):", min_value=0.0, step=0.1, value=10.0)
dias_autonomia = st.number_input("Días de autonomía requeridos:", min_value=0.0, step=1.0, value=3.0)
profundidad_descarga = st.number_input("Profundidad de descarga de las baterías (%):", min_value=0.0, step=1.0, value=50.0) / 100
voltaje_bateria = st.number_input("Voltaje nominal de las baterías (V):", min_value=0.0, step=1.0, value=12.0)

# Datos específicos para On-Grid
st.subheader("Datos para Sistemas On-Grid")
potencia_sistema = st.number_input("Potencia total del sistema (kW):", min_value=0.0, step=0.1, value=5.0)

# Cálculo de resultados
st.header("Resultados")

# Producción de energía
produccion = calcular_produccion(panel_potencia, horas_sol, eficiencia, ampliacion)
st.write(f"Producción de energía diaria por panel: {produccion:.2f} kWh/día")

# Off-Grid: Dimensionamiento de baterías
capacidad_baterias = calcular_baterias(energia_diaria, dias_autonomia, profundidad_descarga, voltaje_bateria, ampliacion)
st.write(f"Capacidad total de baterías requerida: {capacidad_baterias:.2f} Ah")

# On-Grid: Dimensionamiento del inversor
potencia_inversor = calcular_inversor(potencia_sistema, ampliacion)
st.write(f"Potencia mínima del inversor requerida: {potencia_inversor:.2f} kW")

# Opcional: Cálculo de caída de tensión
st.subheader("Cálculo de Caída de Tensión")
corriente = st.number_input("Corriente (A):", min_value=0.0, step=0.1, value=10.0)
longitud = st.number_input("Longitud del cable (m):", min_value=0.0, step=1.0, value=50.0)
resistencia = st.number_input("Resistencia del conductor (Ohm/m):", min_value=0.0, step=0.01, value=0.017)
area = st.number_input("Área del conductor (mm²):", min_value=0.0, step=0.1, value=2.5)

if corriente > 0 and longitud > 0 and resistencia > 0 and area > 0:
    caida_tension = calcular_caida_tension(corriente, longitud, resistencia, area)
    st.write(f"Caída de tensión: {caida_tension:.2f} V")
