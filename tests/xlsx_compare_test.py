import unittest
import numpy as np
import numpy.testing as npt
import pandas as pd
import six

import os

class CompareXlsxTestClass(unittest.TestCase):
    def _compare_xlsx(self, file1, file2, rtol=1e-02, atol=1e-03):
#        print("requested compare: {} and {}".format(file1, file2))
        xl1 = pd.ExcelFile(file1)
        xl2 = pd.ExcelFile(file2)
        self.assertEqual(xl1.sheet_names, xl2.sheet_names)
        
        for sheet in xl1.sheet_names:
#            print("Prrocessing sheet {}".format(sheet))
            df1 = xl1.parse(sheet)
            df2 = xl2.parse(sheet)
            columns1 = list(df1)
            columns2 = list(df2)
            self.assertEqual(len(columns1), len(columns2))
            arr1 = df1.values
            arr2 = df2.values

            self.assertEqual(arr1.shape, arr2.shape)
            for x, y in np.ndindex(arr1.shape):
                v1 = arr1[x, y]
                v2 = arr2[x, y]
#                print("{}: ({}, {}): {} vs {}".format(sheet, x, y, v1, v2))
                if isinstance(v1, six.string_types) or isinstance(v2, six.string_types):
                    self.assertEqual(v1, v2)
                else:
                    npt.assert_allclose(v1, v2, rtol=rtol, atol=atol)

    def test_iris(self):
        self._compare_xlsx("tests/data/iris_1.xlsx", "tests/data/iris_2.xlsx")

    def test_boston(self):
        self._compare_xlsx("tests/data/boston_1.xlsx", "tests/data/boston_2.xlsx")

                                           
if __name__ == '__main__':
    unittest.main()
