import seasons as s
import pytest
import datetime


def main():
    test_validate_date()
    test_format_date()


def test_validate_date():
    with pytest.raises(ValueError):
        s.validate_date("2020-15-09")
    with pytest.raises(ValueError):
        s.validate_date("2019/08/07")
    with pytest.raises(ValueError):
        s.validate_date("2018.12.01")
    with pytest.raises(ValueError):
        s.validate_date("2021-01-32")

def test_format_date():
    assert s.format_date(str(datetime.date.today())) == "Zero"


if __name__ == "__main__":
    main()