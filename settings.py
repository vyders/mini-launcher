import json
import os

import decky


class LauncherStore:
    SETTINGS_FILE = os.path.join(
        decky.DECKY_SETTINGS_DIR,
        "launchers.json",
    )

    @classmethod
    def load(cls):
        """
        Load all launchers from disk.
        """
        if not os.path.exists(cls.SETTINGS_FILE):
            return []

        try:
            with open(
                cls.SETTINGS_FILE,
                "r",
                encoding="utf-8",
            ) as f:
                return json.load(f)
        except Exception as e:
            decky.logger.error(f"Failed to load launchers: {e}")
            return []

    @classmethod
    def save(cls, launchers):
        """
        Save launcher list to disk.
        """
        os.makedirs(
            decky.DECKY_SETTINGS_DIR,
            exist_ok=True,
        )

        try:
            with open(
                cls.SETTINGS_FILE,
                "w",
                encoding="utf-8",
            ) as f:
                json.dump(
                    launchers,
                    f,
                    indent=4,
                    ensure_ascii=False,
                )
        except Exception as e:
            decky.logger.error(f"Failed to save launchers: {e}")
