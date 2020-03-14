from datetime import datetime

class Rep:
    def __init__(self, status, datestr):
        self.status = status
        self.datestr = datestr
    
    @property
    def rdate(self):
        return datetime.strptime(self.datestr, '%Y-%m-%d %H:%M:%S')




def get_stats(reports):
    if len(reports) == 0: return (0,0)
    
    def minutes(td): return (td.seconds // 60) % 60
    
    okmin = 0
    nokmin = 0
    lastrep = reports[0]
    for currep in reports:
        if lastrep.status == 'OK': okmin += minutes(currep.rdate - lastrep.rdate)
        else: nokmin += minutes(currep.rdate - lastrep.rdate)
        lastrep = currep
    return (okmin, nokmin)


def test_empty():
    reps = []
    ok, nok = get_stats(reps)
    assert ok == 0
    assert nok == 0


def test_allok():
    reps = [
        Rep('OK', '2020-03-01 08:33:15'),
        Rep('OK', '2020-03-01 08:35:15'),
        Rep('OK', '2020-03-01 08:38:15'),
    ]
    ok, nok = get_stats(reps)
    assert ok == 5
    assert nok == 0


def test_allnok():
    reps = [
        Rep('NOK', '2020-03-01 08:33:15'),
        Rep('NOK', '2020-03-01 08:35:15'),
        Rep('NOK', '2020-03-01 08:38:15'),
    ]
    ok, nok = get_stats(reps)
    assert ok == 0
    assert nok == 5


def test_mixed_v1():
    reps = [
        Rep('OK', '2020-03-01 08:33:15'),
        Rep('NOK', '2020-03-01 08:35:15'),
        Rep('OK', '2020-03-01 08:38:15'),
    ]
    ok, nok = get_stats(reps)
    assert ok == 2
    assert nok == 3


def test_mixed_v2():
    reps = [
        Rep('OK', '2020-03-01 08:33:15'),
        Rep('OK', '2020-03-01 08:35:15'),
        Rep('NOK', '2020-03-01 08:38:15'),
    ]
    ok, nok = get_stats(reps)
    assert ok == 5
    assert nok == 0


def test_mixed_v3():
    reps = [
        Rep('OK', '2020-03-01 08:33:15'),
        Rep('OK', '2020-03-01 08:35:15'),
        Rep('NOK', '2020-03-01 08:38:15'),
        Rep('NOK', '2020-03-01 08:40:15'),
    ]
    ok, nok = get_stats(reps)
    assert ok == 5
    assert nok == 2


def test_mixed_v4():
    reps = [
        Rep('NOK', '2020-03-01 08:33:15'),
        Rep('OK', '2020-03-01 08:35:15'),
        Rep('OK', '2020-03-01 08:38:15'),
        Rep('NOK', '2020-03-01 08:40:15'),
    ]
    ok, nok = get_stats(reps)
    assert ok == 5
    assert nok == 2


def test_mixed_v5():
    reps = [
        Rep('NOK', '2020-03-01 08:33:15'),
        Rep('OK', '2020-03-01 08:35:15'),
        Rep('OK', '2020-03-01 08:38:15'),
        Rep('NOK', '2020-03-01 08:40:15'),
        Rep('NOK', '2020-03-01 08:45:15'),
        Rep('OK', '2020-03-01 08:48:15'),
        Rep('OK', '2020-03-01 08:49:15'),
    ]
    ok, nok = get_stats(reps)
    assert ok == 6
    assert nok == 10
