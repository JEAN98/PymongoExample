
class Problem:
    def __init__(self,id,description):
        self.id = id
        self.description = description

    def toDBCollection(self):
        return {
            "id":self.id,
            "description":self.description
        }

    def __str__(self):
        return "id: %i - description: %s" \
               %(self.id,self.description)