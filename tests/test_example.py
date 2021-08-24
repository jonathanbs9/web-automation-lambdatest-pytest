from pylenium.driver import Pylenium

def test_google(py: Pylenium):
    py.visit("https://www.google.com.ar") 
    py.get('[name="q"').type('ovejero aleman')
    py.get('[name="btnK"').submit()
    assert py.should().contain_title('ovejero aleman')