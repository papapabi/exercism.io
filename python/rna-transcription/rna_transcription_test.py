import unittest

from rna_transcription import to_rna


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0

class RnaTranscriptionTest(unittest.TestCase):

    def test_transcribes_cytosine_to_guanine(self):
        self.assertEqual(to_rna('C'), 'G')

    def test_transcribes_guanine_to_cytosine(self):
        self.assertEqual(to_rna('G'), 'C')

    def test_transcribes_thymine_to_adenine(self):
        self.assertEqual(to_rna('T'), 'A')

    def test_transcribes_adenine_to_uracil(self):
        self.assertEqual(to_rna('A'), 'U')

    def test_transcribes_all_occurrences(self):
        self.assertEqual(to_rna('ACGTGGTCTTAA'), 'UGCACCAGAAUU')

    def test_does_not_transcribe_empty_string(self):
        with self.assertRaisesWithMessage(ValueError):
            to_rna('')

    def test_does_not_transcribe_blank_string(self):
        with self.assertRaisesWithMessage(ValueError):
            to_rna('            ')

    def test_does_not_transcribe_if_dna_contains_invalids(self):
        with self.assertRaisesWithMessage(ValueError):
            to_rna('XCTGPABIXXYQ')

    def test_does_not_transcribe_if_dna_is_broken_even_with_only_valids(self):
        with self.assertRaisesWithMessage(ValueError):
            to_rna('GTCA    GTCA')

    def test_does_not_transcribe_if_dna_has_trailing_whitespace(self):
        with self.assertRaisesWithMessage(ValueError):
            to_rna("""GCTA            
                   """)

    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == '__main__':
    unittest.main()
