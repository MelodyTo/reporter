from reporter import Header

def test_reporter():
    assert True

author = {
    "Firstname" : "Miles",
    "Lastname" : "Davis",
    "date_of_birth" : 1924
}
author2 = {
    "Firstname" : "John",
    "Lastname" : "Coltrane",
    "date_of_birth" : 1933
}
authors = [author, author2]
def test_create_header():
    header_txt = Header.header(authors)
    assert header_txt
    assert "Miles" in header_txt
    assert str(header_txt)


