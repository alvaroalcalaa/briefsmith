import unittest

from briefsmith import analyse, render


class BriefsmithTests(unittest.TestCase):
    def test_lower_is_better_can_be_a_win(self):
        finding = analyse({
            "name": "CAC",
            "value": 20,
            "target": 25,
            "previous": 28,
            "unit": " €",
            "lower_is_better": True,
        })
        self.assertEqual(finding["state"], "logro")

    def test_render_has_risk_section(self):
        report = render({
            "period": "Demo",
            "metrics": [{"name": "CTR", "value": 1, "target": 2, "previous": 1.5, "unit": "%"}],
        })
        self.assertIn("RIESGOS", report)
        self.assertIn("CTR", report)


if __name__ == "__main__":
    unittest.main()
