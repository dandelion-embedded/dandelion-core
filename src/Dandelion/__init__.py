# System
import logging
import sys
import machine
import uos

# lvgl
import lvgl as lv
import lvesp32

# M5Stack drivers
from m5stack import M5Stack
from axpili9342 import *
from ft6336u import ft6336u

# Dandelion imports
from Dandelion.Library.DandelionAppManifest import DandelionAppManifest
from Dandelion.Library.DandelionTheme import DandelionTheme

# Constants
APPPATHS = ["/Dandelion/Applications"]


class Dandelion:
    def __init__(self, disp=None, touch=None) -> None:

        # Log
        self._log = logging.getLogger("Dandelion")

        # Initialize GUI drivers (display + touch + M5Stack)
        lv.init()
        if disp is None:
            self._log.info(
                "Display was not specified. Creating a new display with a new M5Stack."
            )
            self.ms = M5Stack()
            self.disp = ili9342(m5stack=self.ms)
        else:
            self.ms = disp.m5stack

        if touch is None:
            self._log.info("Touch panel was not specified. Creating a new touch panel.")
            self.touch = ft6336u()

        # Init theme
        self.lv_theme = DandelionTheme()

        # Init GUI refresh
        ref_timer = machine.Timer(0)
        ref_timer.init(period=500, mode=machine.Timer.PERIODIC, callback=self.global_refresher)

        # TODO: Show boot screen

        # Get app list
        self.appList = self.discoverApplicationManifests()

        # Find a launcher
        for app in self.appList:
            if app.launcher:
                launcherManifest = app
                self._log.info("Launcher found: %s.", launcherManifest.name)
                break
        else:
            launcherManifest = None
            self._log.critical("No launchers found. Unable to start Dandelion Core.")
            sys.exit()

        # Run launcher
        launcherModule = __import__(launcherManifest.moduleName)
        self.launch_app(launcherModule, launcherManifest)

    def launch_app(self, app_module, app_manifest):
        self.currentApp = app_module.ENTRYPOINT(app_manifest)

    @staticmethod
    def discoverApplicationManifests() -> list[DandelionAppManifest]:
        manifests = []

        for path in APPPATHS:
            # Make path executable
            sys.path.append(path)

            # Scan for manifests
            app_folders = uos.listdir(path)
            for folder in app_folders:
                try:
                    fullPath = path + "/" + folder + "/manifest.json"
                    with open(fullPath) as json:
                        manifest = DandelionAppManifest(json, folder, path + "/" + folder + "/")
                        manifests.append(manifest)
                except OSError:
                    logging.getLogger("Dandelion").error(
                        "Cannot decode manifest file for %s/%s", path, folder
                    )

        return manifests


    def global_refresher(self, _):
        lv.event_send_refresh_recursive(lv.scr_act())
