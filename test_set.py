import pytest

def compare_sets(set1, set2):
	if not isinstance(set1, set) and not isinstance(set2, set):
		raise TypeError('Please provide a string argument')
	return set1 == set2

def test_set_comparison():
	set1 = set("1308")
	set2 = set("8035")
	assert compare_sets(set1, set2)


def test_object_not_set():
	with pytest.raises(TypeError):
		set1 = set("138")
		set2 = set("813")
		assert compare_sets(set1, set2)