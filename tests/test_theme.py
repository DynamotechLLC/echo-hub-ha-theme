import unittest
from pathlib import Path
import yaml

THEME = Path(__file__).resolve().parents[1] / "themes" / "echo-hub.yaml"
VARS = ["echo-accent", "echo-accent-deep", "echo-heat", "echo-cool", "echo-ok", "echo-warn", "echo-home"]
MODE_VARS = ["echo-tile", "echo-panel", "echo-pill", "lovelace-background", "primary-background-color", "card-background-color"]


class ThemeTest(unittest.TestCase):
    def setUp(self):
        self.doc = yaml.safe_load(THEME.read_text())

    def test_single_theme_named_echo_hub(self):
        self.assertEqual(list(self.doc), ["Echo Hub"])

    def test_shared_vars(self):
        for key in VARS:
            self.assertIn(key, self.doc["Echo Hub"])

    def test_light_and_dark_modes(self):
        modes = self.doc["Echo Hub"]["modes"]
        for mode in ("light", "dark"):
            for key in MODE_VARS:
                self.assertIn(key, modes[mode], mode + ": " + key)

    def test_no_private_references(self):
        text = THEME.read_text()
        for word in ("Tablet", "dashboards/", "2026-10-08"):
            self.assertNotIn(word, text)


if __name__ == "__main__":
    unittest.main()
