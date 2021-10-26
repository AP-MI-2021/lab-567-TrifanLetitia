from Tests.testCRUD import testAdaugacheltuiala, testStergecheltuiala, testModificacheltuiala, testgetByData, \
    testgetBynrapartament
from Tests.testDomain import testcheltuiala
from Tests.testfunctionalitati import testadunarevalori, testceamaimarevaloare


def runAllTests():
    testcheltuiala()
    testAdaugacheltuiala()
    testStergecheltuiala()
    testModificacheltuiala()
    testadunarevalori()
    testceamaimarevaloare()
    testgetByData()
    testgetBynrapartament()

runAllTests()
