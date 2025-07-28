import pytest

def test_addition():
    assert 2 + 2 == 4, "Addition test failed" #if the addition is not correct
    print("Addition test passed successfully.") #if the addition is correct

def test_hello():
    assert "Hello" == "Hello", "Hello test failed"
    print("Hello test passed successfully.")


@pytest.fixture
def sample_list():
    print("🔧 Setting up sample list")
    yield [1,2,3,4]
    print("🧹 Cleaning up after test!")
    

def test_sample_list(sample_list):
    assert sum(sample_list) == 10, "Sum of sample list should be 10"
    print("Sample list test passed successfully.")
    assert len(sample_list) == 4, "Length of sample list should be 4"
    print("Length of sample list test passed successfully.")

# Multiple tests in a class
class TestMath:
    def test_add(self):
        assert 1 + 1 == 2

    def test_mul(self):
        assert 2 * 3 == 6