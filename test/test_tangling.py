from firedrake import *
from movement import *
import unittest


class TestTangling(unittest.TestCase):
    """
    Unit tests for mesh tangling checking.
    """

    def test_tangling_checker_error(self):
        mesh = UnitSquareMesh(3, 3)
        checker = MeshTanglingChecker(mesh, raise_error=True)
        mesh.coordinates.dat.data[3] += 0.2
        with self.assertRaises(ValueError) as cm:
            checker.check()
        msg = "Mesh has 1 tangled elements."
        self.assertEqual(str(cm.exception), msg)

    def test_tangling_checker_warning(self):
        mesh = UnitSquareMesh(3, 3)
        checker = MeshTanglingChecker(mesh, raise_error=False)
        self.assertEqual(checker.check(), 0)
        mesh.coordinates.dat.data[3] += 0.2
        self.assertEqual(checker.check(), 1)
