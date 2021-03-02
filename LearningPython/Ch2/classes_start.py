#
# Example file for working with classes
#

class MyClass():
    def method1(self):
        print("myClass method1")

    def method2(self, some_string):
        print("myClass method2: " + some_string)

class AnotherClass(MyClass):
    def method1(self):
        MyClass.method1(self)
        print("anotherClass method1")

    def method2(self, some_string):
        print("anotherClass method2")

def main():
    c = MyClass()
    c.method1()
    c.method2("this is a string")

    c2 = AnotherClass()
    c2.method1()
    c2.method2("This is a string")


if __name__ == "__main__":
    main()
