import unittest
import apiFunctions as app


class TestMain(unittest.TestCase):
    manilaLagunaKML = app.fetchData('Manila', 'Laguna', "Kilometers", "Liters")
    manilaLagunaML = app.fetchData('Manila', 'Laguna', "Miles", "Liters")
    manilaLagunaMG = app.fetchData('Manila', 'Laguna', "Miles", "Gallons")
    manilaLagunaKMG = app.fetchData(
        'Manila', 'Laguna', "Kilometers", "Gallons")

    def test_fetchData(self):
        # print(TestMain.manilaLagunaKML)
        self.assertIsNotNone(TestMain.manilaLagunaKML)
        self.assertIsNotNone(TestMain.manilaLagunaML)
        self.assertIsNotNone(TestMain.manilaLagunaMG)
        self.assertIsNotNone(TestMain.manilaLagunaKMG)

    def test_KM(self):
        # print(TestMain.manilaLagunaKML)
        self.assertRegex(TestMain.manilaLagunaKML, "Kilometers")
        self.assertRegex(TestMain.manilaLagunaKMG, "Kilometers")

    def test_Miles(self):
        # print(TestMain.manilaLagunaKML)
        self.assertRegex(TestMain.manilaLagunaML, "Miles")
        self.assertRegex(TestMain.manilaLagunaMG, "Miles")

    def test_Gallons(self):
        # print(TestMain.manilaLagunaKML)
        self.assertRegex(TestMain.manilaLagunaMG, "Gal")
        self.assertRegex(TestMain.manilaLagunaKMG, "Gal")

    def test_L(self):
        # print(TestMain.manilaLagunaKML)
        self.assertRegex(TestMain.manilaLagunaML, "Ltr")
        self.assertRegex(TestMain.manilaLagunaKML, "Ltr")


if __name__ == "__main__":
    unittest.main()
