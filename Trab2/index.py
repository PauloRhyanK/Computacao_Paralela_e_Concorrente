import threading
import queue
import time

position_queue = queue.Queue()

# Corpos Celestes usados
planets = {
    'Mercúrio': 88,
    'Vênus': 225,
    'Terra': 365,
    'Marte': 687,
    'Júpiter': 4333,
}

# Definindo a velocidade angular em graus/dia
angular_speed = {planet: 360 / period for planet,period in planets.items()}

# Movendo o planeta
def planet_motion(name, speed):
    day = 0
    while True:
        angle = (speed * day) % 360
        position_queue.put((name, angle, day))
        day += 1
        if day > 3:
            time.sleep(0.0001)
        
# Executando uma thread por planeta     
for planet,speed in angular_speed.items():
    threading.Thread(target=planet_motion, args=(planet, speed), daemon=True).start()
    
current_positions = {planet: 0.0 for planet in planets}

# Verificando alinhamento
def check_aligment():
    # Andando para o programa nao alinhar o ponto 0
    _, _, _ = position_queue.get()
    while True:
        planet, angle, day = position_queue.get()
        current_positions[planet] = angle
        
        aligned = True
        angles = list(current_positions.values())
        for i in range(len(angles)):
            for j in range(i+1, len(angles)):
                diff = abs(angles[i] - angles[j])
                diff = min(diff, 360 - diff)
                if diff > 1:
                    aligned = False
                    break
        
        if aligned:
            print(f"\n Aligned found in {day} days! \n")
            for p, ang in current_positions.items():
                print(f"{p}: {ang:.2f}°")
            break
        
check_aligment()
        
    
    
    