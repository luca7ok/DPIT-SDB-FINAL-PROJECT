class Repository:
    def __init__(self, entities_list):
        self.__entities_list = entities_list

    def find_position(self, entity):
        for index in range(len(self.__entities_list)):
            if self.__entities_list[index] == entity:
                return index
        return None

    def add(self, entity):
        position = self.find_position(entity)

        if position is not None:
            raise Exception("Entity already exists!")

        self.__entities_list.append(entity)

    def update(self, entity, new_entity):
        position = self.find_position(entity)

        if position is None:
            raise Exception("Entity does not exist!")

        self.__entities_list[position] = new_entity

    def delete(self, entity):
        position = self.find_position(entity)

        if position is None:
            raise Exception("Entity does not exist!")

        del self.__entities_list[position]

    def get_all(self):
        return self.__entities_list
