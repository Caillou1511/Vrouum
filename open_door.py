import can

def send_can_message(can_id, data, interface='vcan0'):
    # Créer une instance de bus CAN
    bus = can.interface.Bus(interface, bustype='socketcan')

    # Créer une trame CAN
    message = can.Message(arbitration_id=can_id, data=data, is_extended_id=False)

    try:
        # Envoyer la trame CAN
        bus.send(message)
        print(f"Message CAN envoyé : ID = {hex(can_id)}, Data = {data.hex()}")
    except can.CanError:
        print("Erreur lors de l'envoi du message CAN.")

if __name__ == "__main__":
    # ID CAN pour ouvrir les portes 
    can_id = 0x19B 

    # Données associées à la trame (remplacez par les données que vous avez)
    data = bytearray([0x00, 0x00, 0x00, 0x00])  # Exemple de données

    # Envoyer la trame sur vcan0
    send_can_message(can_id, data)


