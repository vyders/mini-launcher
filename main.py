import os
import decky

from settings import LauncherStore


class Plugin:
    async def get_launchers(self):
        """
        Return all saved launchers.
        """
        return LauncherStore.load()

    async def save_launchers(self, launchers):
        """
        Save launcher list.
        """
        LauncherStore.save(launchers)
        return True

    async def open_launcher(self, url: str):
        """
        Open launcher URL.

        (Implementation will be added in the next sprint.)
        """
        decky.logger.info(f"Open launcher requested: {url}")
        return True

    async def _main(self):
        decky.logger.info("Mini Launcher started")

    async def _unload(self):
        decky.logger.info("Mini Launcher stopped")

    async def _uninstall(self):
        decky.logger.info("Mini Launcher uninstalled")

    async def _migration(self):
        decky.logger.info("Migrating Mini Launcher")

        decky.migrate_logs(
            os.path.join(
                decky.DECKY_USER_HOME,
                ".config",
                "mini-launcher",
                "mini-launcher.log",
            )
        )

        decky.migrate_settings(
            os.path.join(
                decky.DECKY_HOME,
                "settings",
                "launchers.json",
            ),
            os.path.join(
                decky.DECKY_USER_HOME,
                ".config",
                "mini-launcher",
            ),
        )

        decky.migrate_runtime(
            os.path.join(
                decky.DECKY_HOME,
                "mini-launcher",
            ),
            os.path.join(
                decky.DECKY_USER_HOME,
                ".local",
                "share",
                "mini-launcher",
            ),
        )
