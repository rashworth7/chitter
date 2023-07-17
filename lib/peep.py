class Peep:
    
    def __init__(self, id, message, timestamp, user_id, tags=[]):
       self.id = id
       self.message = message
       self.timestamp = timestamp
       self.user_id = user_id
       self.tags = tags
       

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Peep({self.id}, {self.message}, {self.timestamp}, {self.user_id}, Tags = {', '.join(self.tags)})"