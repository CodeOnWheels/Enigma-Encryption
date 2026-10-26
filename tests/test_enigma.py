import contextlib
import importlib.util
import io
from pathlib import Path
import random
import unittest
from unittest.mock import patch

import enigmaEncrypter as cipher


class CipherTests(unittest.TestCase):
    def test_round_trips(self):
        messages = ["", "hello", "###", "a###b", "#edges#", "#######",
                    "中文\nrobot 🤖", "".join(cipher.alphaNumericList)]
        state = random.getstate()
        try:
            for seed in range(30):
                random.seed(seed)
                for message in messages:
                    for passes in (1, 2, 5):
                        with self.subTest(seed=seed, message=message, passes=passes):
                            encoded = cipher.stackEncrypt(message, passes, 7, -2)
                            self.assertEqual(
                                cipher.stackDecrypt(encoded, passes, 7, -2), message)
        finally:
            random.setstate(state)

    def test_zero_passes(self):
        for function in (cipher.stackEncrypt, cipher.stackDecrypt):
            self.assertEqual(function("unchanged", 0), "unchanged")

    def test_invalid_pass_counts(self):
        for function in (cipher.stackEncrypt, cipher.stackDecrypt):
            for count in (-1, 1.5, True, "2"):
                with self.subTest(function=function.__name__, count=count):
                    with self.assertRaises(ValueError):
                        function("hello", count)

    def test_missing_frame(self):
        with self.assertRaises(ValueError):
            cipher.decrypt("")

    def test_import_is_quiet(self):
        spec = importlib.util.spec_from_file_location(
            "fresh_cipher", Path(cipher.__file__))
        module = importlib.util.module_from_spec(spec)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            spec.loader.exec_module(module)
        self.assertEqual(output.getvalue(), "")

    def test_demo_forwards_parameters(self):
        with patch.object(cipher, "stackEncrypt", return_value="encoded") as enc:
            with patch.object(cipher, "stackDecrypt", return_value="hello") as dec:
                with contextlib.redirect_stdout(io.StringIO()):
                    cipher.runTests("hello", 7, 3)
        enc.assert_called_once_with("hello", 1, 7, 3)
        dec.assert_called_once_with("encoded", 1, 7, 3)


if __name__ == "__main__":
    unittest.main()

