import pytest

from temperature_conversion import TemperatureConversion as tc

## test kelvin to celsius functions
def test_kelvin_to_celsius_zero():
    """ test zero kelvin """
    tc_obj = tc()
    assert tc_obj.kelvin_to_celsius(0) == -273.15

def test_kelvin_to_celsius_positive_float():
    """ test a positive kelvin float """
    tc_obj = tc()
    assert tc_obj.kelvin_to_celsius(15.43) == -257.72

def test_kelvin_to_celsius_positive_integer():
    """ test a positive kelvin integer """
    tc_obj = tc()
    assert tc_obj.kelvin_to_celsius(20) == -253.15

def test_kelvin_to_celsius_negative_float():
    """ test a positive kelvin float """
    tc_obj = tc()
    assert tc_obj.kelvin_to_celsius(-154.43) == -427.58

def test_kelvin_to_celsius_negative_integer():
    """ test a positive kelvin integer """
    tc_obj = tc()
    assert tc_obj.kelvin_to_celsius(-120) == -393.15

## test kelvin to fahrenheit functions
def test_kelvin_to_fahrenheit_zero():
    """ test zero kelvin """
    tc_obj = tc()
    assert tc_obj.kelvin_to_celsius(0) == -273.15

def test_kelvin_to_fahrenheit_postive_float():
    """ test a positive kelvin """
    tc_obj = tc()
    assert tc_obj.kelvin_to_celsius(1.5) == -271.65

def test_kelvin_to_fahrenheit_postive_integer():
    """ test a positive kelvin """
    tc_obj = tc()
    assert tc_obj.kelvin_to_celsius(1) == -272.15

def test_kelvin_to_fahrenheit_negative_float():
    """ test a positive kelvin """
    tc_obj = tc()
    assert tc_obj.kelvin_to_celsius(-1.5) == -274.65

def test_kelvin_to_fahrenheit_negative_integer():
    """ test a positive kelvin """
    tc_obj = tc()
    assert tc_obj.kelvin_to_celsius(-1) == -274.15

## test kelvin to rankine functions
def test_kelvin_to_rankine_zero():
    """ test zero kelvin """
    tc_obj = tc()
    assert tc_obj.kelvin_to_rankine(0) == 0

def test_kelvin_to_rankine_positive_float():
    """ test a positive float kelvin """
    tc_obj = tc()
    assert tc_obj.kelvin_to_rankine(5.45) == 9.81

def test_kelvin_to_rankine_positive_integer():
    """ test a positive integer kelvin """
    tc_obj = tc()
    assert tc_obj.kelvin_to_rankine(5) == 9

def test_kelvin_to_rankine_negative_float():
    """ test a positive float kelvin """
    tc_obj = tc()
    assert tc_obj.kelvin_to_rankine(-5.45) == -9.81

def test_kelvin_to_rankine_negative_integer():
    """ test a positive integer kelvin """
    tc_obj = tc()
    assert tc_obj.kelvin_to_rankine(-5) == -9

## test celsius to kelvin functions
def test_celsius_to_kelvin_zero():
    """ test zero celsius """
    tc_obj = tc()
    assert tc_obj.celsius_to_kelvin(0) == 273.15

def test_celsius_to_kelvin_positive_float():
    """ test positive celsius float"""
    tc_obj = tc()
    assert tc_obj.celsius_to_kelvin(25.54) == 298.69

def test_celsius_to_kelvin_positive_integer():
    """ test positive celsius integer """
    tc_obj = tc()
    assert tc_obj.celsius_to_kelvin(25) == 298.15

def test_celsius_to_kelvin_negative_float():
    """ test negative celsius float"""
    tc_obj = tc()
    assert tc_obj.celsius_to_kelvin(-25.54) == 247.61

def test_celsius_to_kelvin_negative_integer():
    """ test negative celsius integer """
    tc_obj = tc()
    assert tc_obj.celsius_to_kelvin(-25) == 248.15

## test celsius to fahrenheit functions
def test_celsius_to_fahrenheit_zero():
    """ test zero celsius """
    tc_obj = tc()
    assert tc_obj.celsius_to_fahrenheit(0) == 32

def test_celsius_to_fahrenheit_positive_float():
    """ test positive celsius float """
    tc_obj = tc()
    assert tc_obj.celsius_to_fahrenheit(63.5) == 146.3

def test_celsius_to_fahrenheit_positive_integer():
    """ test positive celsius integer """
    tc_obj = tc()
    assert tc_obj.celsius_to_fahrenheit(63) == 145.4

def test_celsius_to_fahrenheit_negative_float():
    """ test negative celsius float """
    tc_obj = tc()
    assert tc_obj.celsius_to_fahrenheit(-63.5) == -82.3

def test_celsius_to_fahrenheit_negative_integer():
    """ test negative celsius integer """
    tc_obj = tc()
    assert tc_obj.celsius_to_fahrenheit(-63) == -81.4

## test celsius to rankine functions
def test_celsius_to_rankine_zero():
    """ test zero celsius """
    tc_obj = tc()
    assert tc_obj.celsius_to_rankine(0) == 491.67

def test_celsius_to_rankine_positive_float():
    """ test positive float celsius """
    tc_obj = tc()
    assert tc_obj.celsius_to_rankine(33.33) == 551.66

def test_celsius_to_rankine_positive_integer():
    """ test positive integer celsius """
    tc_obj = tc()
    assert tc_obj.celsius_to_rankine(33) == 551.07

def test_celsius_to_rankine_negative_float():
    """ test negative float celsius """
    tc_obj = tc()
    assert tc_obj.celsius_to_rankine(-33.33) == 431.68

def test_celsius_to_rankine_negative_integer():
    """ test negative integer celsius """
    tc_obj = tc()
    assert tc_obj.celsius_to_rankine(-33) == 432.27

## test fahrenheit to kelvin function
def test_fahrenheit_to_kelvin_zero():
    """ test zero fahrenheit """
    tc_obj = tc()
    assert tc_obj.fahrenheit_to_kelvin(0) == 255.37

def test_fahrenheit_to_kelvin_positive_float():
    """ test positive float fahrenheit  """
    tc_obj = tc()
    assert tc_obj.fahrenheit_to_kelvin(44.54) == 280.12

def test_fahrenheit_to_kelvin_positive_integer():
    """ test positive integer fahrenheit """
    tc_obj = tc()
    assert tc_obj.fahrenheit_to_kelvin(44) == 279.82

def test_fahrenheit_to_kelvin_negative_float():
    """ test negative float fahrenheit  """
    tc_obj = tc()
    assert tc_obj.fahrenheit_to_kelvin(-44.54) == 230.63

def test_fahrenheit_to_kelvin_negative_integer():
    """ test negative integer fahrenheit """
    tc_obj = tc()
    assert tc_obj.fahrenheit_to_kelvin(-44) == 230.93

## test fahrenheit to celsius
def test_fahrenheit_to_celsius_zero():
    """ test zero fahrenheit """
    tc_obj = tc()
    assert tc_obj.fahrenheit_to_celsius(0) == -17.78

def test_fahrenheit_to_celsius_positive_float():
    """ test postive float fahrenheit """
    tc_obj = tc()
    assert tc_obj.fahrenheit_to_celsius(32.45) == .25

def test_fahrenheit_to_celsius_positive_integer():
    """ test positive integer fahrenheit """
    tc_obj = tc()
    assert tc_obj.fahrenheit_to_celsius(32) == 0

def test_fahrenheit_to_celsius_negative_float():
    """ test postive float fahrenheit """
    tc_obj = tc()
    assert tc_obj.fahrenheit_to_celsius(-32.45) == -35.81

def test_fahrenheit_to_celsius_negative_integer():
    """ test positive integer fahrenheit """
    tc_obj = tc()
    assert tc_obj.fahrenheit_to_celsius(-32) == -35.56

## test fahrenheit to rankine
def test_fahrenheit_to_rankine_zero():
    """ test zero fahrenheit """
    tc_obj = tc()
    assert tc_obj.fahrenheit_to_rankine(0) == 459.67

def test_fahrenheit_to_rankine_positive_float():
    """ test postive float fahrenheit """
    tc_obj = tc()
    assert tc_obj.fahrenheit_to_rankine(99.9) == 559.57

def test_fahrenheit_to_rankine_positive_integer():
    """ test postitve integer fahrenheit """
    tc_obj = tc()
    assert tc_obj.fahrenheit_to_rankine(99) == 558.67

def test_fahrenheit_to_rankine_negative_float():
    """ test negative float fahrenheit """
    tc_obj = tc()
    assert tc_obj.fahrenheit_to_rankine(-99.9) == 359.77

def test_fahrenheit_to_rankine_negative_integer():
    """ test negative integer fahrenheit """
    tc_obj = tc()
    assert tc_obj.fahrenheit_to_rankine(-99) == 360.67

## test rankine to kelvin function
def test_rankine_to_kelvin_zero():
    """ test zero rankine """
    tc_obj = tc()
    assert tc_obj.rankine_to_kelvin(0) == 0

def test_rankine_to_kelvin_positive_float():
    """ test positive float rankine """
    tc_obj = tc()
    assert tc_obj.rankine_to_kelvin(1.5) == .83

def test_rankine_to_kelvin_positive_integer():
    """ test positive integer rankine """
    tc_obj = tc()
    assert tc_obj.rankine_to_kelvin(1) == .56

def test_rankine_to_kelvin_negative_float():
    """ test positive float rankine """
    tc_obj = tc()
    assert tc_obj.rankine_to_kelvin(-1.5) == -.83

def test_rankine_to_kelvin_negative_integer():
    """ test positive integer rankine """
    tc_obj = tc()
    assert tc_obj.rankine_to_kelvin(-1) == -.56

## test rankine to celsius function
def test_rankine_to_celsius_zero():
    """ test zero rankine """
    tc_obj = tc()
    assert tc_obj.rankine_to_celsius(0) == -273.15

def test_rankine_to_celsius_postive_float():
    """ test postive float rankine """
    tc_obj = tc()
    assert tc_obj.rankine_to_celsius(3.9) == -270.98

def test_rankine_to_celsius_positive_integer():
    """ test positive rankine """
    tc_obj = tc()
    assert tc_obj.rankine_to_celsius(7) == -269.26

def test_rankine_to_celsius_negative_float():
    """ test negative float rankine """
    tc_obj = tc()
    assert tc_obj.rankine_to_celsius(-3.9) == -275.32

def test_rankine_to_celsius_negative_integer():
    """ test negative float rankine """
    tc_obj = tc()
    assert tc_obj.rankine_to_celsius(-7) == -277.04

## test rankine to fahrenheit
def test_rankine_to_fahrenheit_zero():
    """ test zero rankine """
    tc_obj = tc()
    assert tc_obj.rankine_to_fahrenheit(0) == -459.67

def test_rankine_to_fahrenheit_positive_float():
    """ test rankine positive float """
    tc_obj = tc()
    assert tc_obj.rankine_to_fahrenheit(88.8) == -370.87

def test_rankine_to_fahrenheit_positive_integer():
    """ test rankine positive integer """
    tc_obj = tc()
    assert tc_obj.rankine_to_fahrenheit(88) == -371.67

def test_rankine_to_fahrenheit_negative_float():
    """ test rankine positive float """
    tc_obj = tc()
    assert tc_obj.rankine_to_fahrenheit(-88.8) == -548.47

def test_rankine_to_fahrenheit_negative_integer():
    """ test rankine positive integer """
    tc_obj = tc()
    assert tc_obj.rankine_to_fahrenheit(-88) == -547.67

def test_kelvin_to_celsius_string():
    """ test string input """
    tc_obj = tc()
    assert tc_obj.kelvin_to_celsius("abc") == None

def test_kelvin_to_fahrenheit_string():
    """ test string input """
    tc_obj = tc()
    assert tc_obj.kelvin_to_fahrenheit("abc") == None

def test_kelvin_to_rankine_string():
    """ test string input """
    tc_obj = tc()
    assert tc_obj.kelvin_to_rankine("abc") == None

def test_celsius_to_kelvin_string():
    """ test string input """
    tc_obj = tc()
    assert tc_obj.celsius_to_kelvin("abc") == None

def test_celsius_to_fahrenheit_string():
    """ test string input """
    tc_obj = tc()
    assert tc_obj.celsius_to_fahrenheit("abc") == None

def test_celsius_to_rankine_string():
    """ test string input """
    tc_obj = tc()
    assert tc_obj.celsius_to_rankine("abc") == None

def test_fahrenheit_to_kelvin_string():
    """ test string input """
    tc_obj = tc()
    assert tc_obj.fahrenheit_to_kelvin("abc") == None

def test_fahrenheit_to_celsius_string():
    """ test string input """
    tc_obj = tc()
    assert tc_obj.fahrenheit_to_celsius("abc") == None

def test_fahrenheit_to_rankine_string():
    """ test string input """
    tc_obj = tc()
    assert tc_obj.fahrenheit_to_rankine("abc") == None

def test_rankine_to_kelvin_string():
    """ test string input """
    tc_obj = tc()
    assert tc_obj.rankine_to_kelvin("abc") == None

def test_rankine_to_celsius_string():
    """ test string input """
    tc_obj = tc()
    assert tc_obj.rankine_to_celsius("abc") == None

def test_rankine_to_fahrenheit_string():
    """ test string input """
    tc_obj = tc()
    assert tc_obj.rankine_to_fahrenheit("abc") == None
