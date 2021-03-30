def setup_module(module):
    print('setup module!')

def teardown_module(module):
    print('teardown module!')

def setup_function(function):
    if function == test1:
        print('setting up test1!')
    elif function == test2:
        print('setting up test2!')
    else:
        print('Setting up the unknown test!')


def teardown_function(function):
    if function == test1:
        print('tearing down test1!')
    elif function == test2:
        print('tearing down test2!')
    else:
        print('tearing down the unknown test!')


def test1():
    print('execution test1!')
    assert True

def test2():
    print('execution test1!')
    assert True

class TestClass:
    @classmethod
    def setup_class(cls):
        print('setup test class!')

    @classmethod
    def teardown_class(cls):
        print('tearing down test class!')

    def setup_method(self, method):
        if method == self.test1:
            print('setting up test 1!')
        elif method == self.test2:
            print('setting up test 2!')
        else:
            print('setting up the unknown test!')

    def teardown_method(self, method):
        if method == self.test1:
            print('tearing down test 1!')
        elif method == self.test2:
            print('tearing down test 2!')
        else:
            print('tearing down the unknown test!')

    def test1(self):
        print('executing test1!')
        assert True

    def test2(self):
        print('executing test2!')
        assert True