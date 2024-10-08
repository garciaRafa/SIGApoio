import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from app.models import Horario
def generate_schedule():
    schedule = []
    time_slots = {
        'M': {'start': '07:00', 'interval': 50, 'count': 6},
        'T': {'start': '13:00', 'interval': 50, 'count': 6},
        'N': {'start': '18:40', 'interval': 50, 'count': 4},
    }
    days = [2, 3, 4, 5, 6]  # Representa de segunda a sexta
    
    for day in days:
        for shift in time_slots:
            start_time = time_slots[shift]['start']
            interval = time_slots[shift]['interval']
            count = time_slots[shift]['count']
            
            for i in range(1, count + 1):
                id = f"{day}{shift}{i}"
                start_hour, start_minute = map(int, start_time.split(':'))
                if i % 2 == 1 and i != 1:
                    start_minute = start_minute + 10 # Adicionando intervalo
                end_hour = start_hour
                end_minute = start_minute + interval
                if end_minute >= 60:
                    end_hour += end_minute // 60
                    end_minute = end_minute % 60
                
                start_time = f"{start_hour:02}:{start_minute:02}"
                end_time = f"{end_hour:02}:{end_minute:02}"
                schedule.append({
                    'id': id,
                    'dia': day - 1, ## no Models, o day começa no domingo, e no ID o day começa no sábado
                    'horaInicio': start_time,
                    'horaFim': end_time
                })
                
                start_time = end_time  # O próximo horário começa quando esse termina
    
    return schedule

def criar_horarios():
    # Gerar horários
    horarios = generate_schedule()

    # Inserir ou atualizar registros
    for horario in horarios:
        Horario.objects.get_or_create(
            id=horario['id'],
            defaults={
                'dia': horario['dia'],
                'horaInicio': horario['horaInicio'],
                'horaFim': horario['horaFim']
            }
        )

criar_horarios()