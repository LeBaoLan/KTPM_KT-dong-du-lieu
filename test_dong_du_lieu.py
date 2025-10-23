import pytest


def hienmau(age, bpressure, weight):
    if age < 18 or age > 65 or bpressure < 100 or bpressure > 140 or weight < 50:
        return "Khong hien mau"
    if age <= 30 and weight >= 70 and 110 <= bpressure <= 130:
        return "Hien 450ml mau"
    if age <= 45 and weight >= 60:
        return "Hien 400ml mau"
    return "Hien 350ml mau"


@pytest.mark.dataflow
@pytest.mark.parametrize("age,bpressure,weight,expected", [
    (60, 120, 60, "Hien 350ml mau"),

])
def test_hienmau(age, bpressure, weight, expected):
    assert hienmau(age, bpressure, weight) == expected


# pytest: chay tat ca test
