#! python3
# -*- coding: utf-8 -*-
import random
import string

FirstNames    = './files/FirstNames.txt'
MiddleNames   = './files/MiddleNames.txt'
LastNames     = './files/LastNames.txt'
CountyNames   = './files/CountyNames.txt'
PlaceNames    = './files/PlaceNames.txt'
StateNames    = './files/StateNames.txt'
CountryNames  = './files/CountryNames.txt'
CompanyNames  = './files/CompanyNames.txt'



def Number(start=0, end=100000):
    return random.randint(start, end)


def UpperChars(NoOfChars=2):
    _char = ''
    for num in range(NoOfChars):
        _char += random.choice(string.ascii_uppercase)
    return _char


def rawCount(filename):
    with open(filename, 'rb') as f:
        lines = 1
        buf_size = 1024 * 1024
        read_f = f.raw.read

        buf = read_f(buf_size)
        while buf:
            lines += buf.count(b'\n')
            buf = read_f(buf_size)
        return lines


def randomLine(filename):
    num = int(random.uniform(0, rawCount(filename)))
    with open(filename, 'r') as f:
        for i, line in enumerate(f, 1):
            if i == num:
                break
    return line.strip('\n')


def First():
    return randomLine(FirstNames)


def Last():
    return randomLine(LastNames)


def Middle():
    return randomLine(MiddleNames)


def States():
    return randomLine(StateNames)


def Places():
    return randomLine(PlaceNames)


def County():
    return randomLine(CountyNames)


def Company():
    return randomLine(CompanyNames)


def Country():
    _Cc = randomLine(CountryNames)
    _Cc = _Cc.split('|')
    return _Cc[1]


def CountryCode():
    _Cc = randomLine(CountryNames)
    _Cc = _Cc.split('|')
    return _Cc[0]


def StateCode():
    return States().split(', ')[1]


def Full():
    return ' '.join([First(), Last()])


def Address():
    _door = str(Number(11, 99))
    _zip  = str(Number(1000, 9999))
    _adrs = ', '.join([Places(), County(), States(), _zip])
    _adrs = _door + UpperChars(1) + ' - ' + _adrs + '.'
    return _adrs


def ShortAddress():
    _door = str(Number(11, 99))
    _zip  = str(Number(1000, 9999))
    _adrs = ', '.join([County(), States(), _zip])
    _adrs = _door + ' ' + _adrs
    return _adrs


if __name__ == '__main__':
    print('Full name is ',Full(), 'Works at ', Company(), ' Lives at ', Address(), StateCode(), Country())
