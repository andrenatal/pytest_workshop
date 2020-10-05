# content of test_class.py
class ObjTest:
    def __init__(self):
        self.other_data = "0"

class TestClass:
    def test_one(self):
        x = "this"
        assert "J" in x

    def test_two(self):
        x = ObjTest()
        assert hasattr(x, "data_other")
