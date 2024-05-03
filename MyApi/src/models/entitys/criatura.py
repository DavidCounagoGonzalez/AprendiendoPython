class Criatura():
    
    def __init__(self, id, name=None, image=None, description=None, location=None, drops=None) -> None:
        self.id = id
        self.name = name
        self.image = image
        self.description = description
        self.location = location
        self.drops = drops
        
    def to_json(self):
        return{
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'description': self.description,
            'location': self.location,
            'drops': self.drops
        }