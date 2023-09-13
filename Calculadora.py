from datetime import datetime, timedelta

def calculadoraHoras(inicio, fim, intervalo):
    try:
        formato = "%H:%M"
        horaInicio = datetime.strptime(inicio, formato)
        horaFim = datetime.strptime(fim, formato)
        intervalo = datetime.strptime(intervalo, formato)

        diferenca = horaFim - horaInicio

        if diferenca.total_seconds() < 0:
            diferenca += timedelta(days=1)

        horas = diferenca.seconds // 3600
        minutos = (diferenca.seconds // 60) % 60

        intervaloSegundos = intervalo.hour * 3600 + intervalo.minute * 60
        diferencaSegundos = diferenca.total_seconds() - intervaloSegundos
        if diferencaSegundos < 0:
            diferencaSegundos += 24 * 3600

        horasResultado = int(diferencaSegundos // 3600)
        minutosResultado = int((diferencaSegundos % 3600) // 60)

        resultadoFormatado = "{:02d}:{:02d}".format(horasResultado, minutosResultado)
        return resultadoFormatado

    except ValueError:
        return "Formato de hora inválido. Use HH:mm."

if __name__ == "__main__":
    horaInicio = input("Informe a hora de início (HH:mm): ")
    horaFim = input("Informe a hora de término (HH:mm): ")
    intervalo = input("Informe o intervalo (HH:mm): ")

    resultado = calculadoraHoras(horaInicio, horaFim, intervalo)
    print("Diferença de horas trabalhadas após subtrair o intervalo:", resultado)
