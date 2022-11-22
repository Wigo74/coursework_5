import json

from equipment import EquipmentData

equipment_file = open("./data/equipment.json")
        # with open("./data/equipment.json", 'r') as f:
data = json.load(equipment_file)
equipment_file.close()
equipment_schema = marshmallow_dataclass.class_schema(EquipmentData)
equipment_schema().load(data)
print(data)
