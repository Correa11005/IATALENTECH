from processor import clean_id , merge_name
def test_clean_id():
    assert clean_id("cc-75.087.345")=="75087345"
def test_merge_name():
    assert merge_name("Jacobo","Correa")=="Jacobo Correa"


