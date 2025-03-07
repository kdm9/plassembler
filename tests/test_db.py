"""
Unit tests for plassembler.

Usage: pytest

"""

import shutil
import sys

# import
import unittest
from pathlib import Path

import pytest
from loguru import logger

# import functions
from src.plassembler.utils.db import check_db_installation, get_database_zenodo

# data
test_data = Path("tests/test_data")
db_path = Path(f"{test_data}/Plassembler_Test_DB")
val_data = Path(f"{test_data}/validation")
tmp_db_path = Path(f"{test_data}/Plassembler_Test_DB_test")


# make fake tempdir for testing
@pytest.fixture(scope="session")
def tmp_dir(tmpdir_factory):
    return tmpdir_factory.mktemp("tmp")


# to ensure sys exit on logger error
logger.add(lambda _: sys.exit(1), level="ERROR")


class test_install(unittest.TestCase):
    """Test for db"""

    # for plassembler run
    def test_check_db_installation_good(self):
        check_db_installation(db_path, False)

    # for plassembler download
    def test_check_db_installation_good_d(self):
        check_db_installation(db_path, True)

    def test_check_db_installation_bad(self):
        with self.assertRaises(SystemExit):
            check_db_installation(val_data, False)

    def test_get_database_zenodo(self):
        expected_return = True
        get_database_zenodo(tmp_db_path)
        # remove it after downloading
        shutil.rmtree(tmp_db_path)
        self.assertEqual(expected_return, True)
