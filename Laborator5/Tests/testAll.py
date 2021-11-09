from Tests.testCRUD import testAdaugacheltuiala, testStergecheltuiala, testModificacheltuiala, testgetByData, \
    testgetBynrapartament
from Tests.testDomain import testcheltuiala
from Tests.testfunctionalitati import testadunarevalori, testceamaimarecheltuiala, testordonaredescdupasuma, \
    testafisareasumelorlunare, testUNDO


def runAllTests():
    testcheltuiala()
    testAdaugacheltuiala()
    testStergecheltuiala()
    testModificacheltuiala()
    testadunarevalori()
    testceamaimarecheltuiala()
    testgetByData()
    testgetBynrapartament()
    testordonaredescdupasuma()
    testafisareasumelorlunare()
    testUNDO()
    #testREDO()


runAllTests()
