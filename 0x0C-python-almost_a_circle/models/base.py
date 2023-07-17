#!/usr/bin/python3

"""define Base models class"""
import json
import csv
import turtle


class Base:

    """Base model of represents the Base for other classes in this project

    Private Class Attributes:  __nb_object int: number of instant bases"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init new Base
        Args: iD int: The identity of new Base """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return the JSON serial of list of dicts
        Args: list_dictionaries List: list of dictionari"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write the JSON serial of list of object to file
        Args:
            list_objs list: list of inherit Base instance """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserial of JSON str
        Args: json_string (str): JSON str represent of a list of dicr
        Returns:
            If json_string is None or Empty = an empty list
            Otherwise - the Python list represent by json_string"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instant from dictionary of the attribute
        Args: Dictionary dict: Key or value pair of attributes to initz"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                update = cls(1, 1)
            else:
                update = cls(1)
            update.update(**dictionary)
            return update

    @classmethod
    def load_from_file(cls):
        """Return list of classe instant from file of JSON strings
        Reads from class.__name__ json
        Returns:
            if the file does not exist = an empty list
            Otherwise a list of instant classe """
        FileName = str(cls.__name__) + ".json"
        try:
            with open(FileName, "r") as jsonfile:
                List_Dic = Base.from_json_string(jsonfile.read())
                return [cls.create(**dictionary) for dictionary in List_Dic]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the csv serial of a list of object to file
        Args: list_objs list: list of inherit Base instance """
        FileName = cls.__name__ + ".csv"
        with open(FileName, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classe instant from  csv file
        read from  cls.__name__ .csv
        Returns: if the file does not exist then an empty list
            Otherwise a list of instantiated classe """
        FileName = cls.__name__ + ".csv"
        try:
            with open(FileName, "r", n="") as csvfile:
                if cls.__name__ == "Rectangle":
                    Files_Names = ["id", "width", "height", "x", "y"]
                else:
                    Files_Names = ["id", "size", "x", "y"]
                list_dic = csv.DictReader(csvfile, Files_Names=Files_Names)
                list_dic = [dict([y, int(x)] for y, x in i.items())
                              for i in list_dic]
                return [cls.create(**i) for i in list_dic]
        except IOError:
            return []
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """write the csv serial of the list of object to file
        Args: list_objs list: list of inherit Base instance """
        FileName = cls.__name__ + ".csv"
        with open(FileName, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())
    @staticmethod
    def draw(list_rectangles, list_squares):
        """draw rectangle and Square using the turtle module
        Args: list_rectangles list: list of Rectangle object to draw
            list_squares list: A list of Square object to draw"""
        turtle = turtle.Turtle()
        turtle.screen.bgcolor("#b7312c")
        turtle.pensize(3)
        turtle.shape("turtle")

        turtle.color("#ffffff")
        for rect in list_rectangles:
            turtle.showturtle()
            turtle.up()
            turtle.goto(rect.x, rect.y)
            turtle.down()
            for y in range(2):
                turtle.forward(rect.width)
                turtle.left(90)
                turtle.forward(rect.height)
                turtle.left(90)
            turtle.hideturtle()

        turtle.color("#b5e3d8")
        for sq in list_squares:
            turtle.showturtle()
            turtle.up()
            turtle.goto(sq.x, sq.y)
            turtle.down()
            for y in range(2):
                turtle.forward(sq.width)
                turtle.left(90)
                turtle.forward(sq.height)
                turtle.left(90)
            turtle.hideturtle()

        turtle.exitonclick()
