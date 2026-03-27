def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665

    horas_completas = (total_segundos // 60) // 60
    print(horas_completas)
    minutos_completas = (total_segundos - horas_completas *60 *60) // 60
    print(minutos_completas)
    segundos_restantes= (total_segundos - minutos_completas *60 - horas_completas *60*60)
    print(segundos_restantes)

time()