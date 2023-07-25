class Repository:
    def __init__(self, entities_list):
        """
        Constructor for Repository class
        :param entities_list: list of entities (list)
        """
        self.__entities_list = entities_list

    def find_position(self, entity):
        """
        Returns the position of an entity from a list of entities
        :param entity: entity's position to be found
        :return: the index if the entity exists in the list, None otherwise
        """
        for index in range(len(self.__entities_list)):
            if self.__entities_list[index] == entity:
                return index
        return None

    def add(self, entity):
        """
        Adds an entity to the list of entities if it doesn't exist already
        :param entity: entity to add
        :return:
        """
        position = self.find_position(entity)

        if position is not None:
            raise Exception("Entity already exists!")

        self.__entities_list.append(entity)

    def update(self, entity, new_entity):
        """
        Updates the entity with a new one if it exists
        :param entity: entity to be changed
        :param new_entity: new entity
        :return:
        """
        position = self.find_position(entity)

        if position is None:
            raise Exception("Entity does not exist!")

        self.__entities_list[position] = new_entity

    def delete(self, entity):
        """
        Removes an entity from the list of entities
        :param entity: entity to be removed
        :return:
        """
        position = self.find_position(entity)

        if position is None:
            raise Exception("Entity does not exist!")

        del self.__entities_list[position]

    def get_all(self):
        """
        Returns the list of entities
        :return: list of entities (list)
        """
        return self.__entities_list
