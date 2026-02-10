def stop_heater(temperature): 
    if temperature > 25: 
        print("heater stopped")
        return False 
    return True 