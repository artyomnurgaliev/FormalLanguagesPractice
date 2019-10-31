import solution


def test_calculation_of_result(capfd):
    solution.calc_result('a', 'a')
    out, err = capfd.readouterr()
    assert out == "1\n"

    solution.calc_result('aa.', 'a')
    out, err = capfd.readouterr()
    assert out == "1\n"

    solution.calc_result('.', 'a')
    out, err = capfd.readouterr()
    assert out == "ERROR\n"

    solution.calc_result('*', 'a')
    out, err = capfd.readouterr()
    assert out == "ERROR\n"

    solution.calc_result('ab+', 'a')
    out, err = capfd.readouterr()
    assert out == "1\n"

    solution.calc_result('++', 'a')
    out, err = capfd.readouterr()
    assert out == "ERROR\n"

    solution.calc_result('ab+c.aba.*.bac.+.+*', 'babc')
    out, err = capfd.readouterr()
    assert out == "2\n"

    solution.calc_result('acb..bab.c.*.ab.ba.+.+*a.', 'cbaa')
    out, err = capfd.readouterr()
    assert out == "4\n"

    solution.calc_result('a1+', 'a')
    out, err = capfd.readouterr()
    assert out == "1\n"

    solution.calc_result('%^^%^', 'a')
    out, err = capfd.readouterr()
    assert out == "ERROR\n"
