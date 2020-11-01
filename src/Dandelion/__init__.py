# System
import uos
import logging
import sys

# lvgl
import lvgl as lv
import lvesp32

# M5Stack drivers
from m5stack import M5Stack
from axpili9342 import *
from ft6336u import ft6336u

# Dandelion imports
from Dandelion.Library.DandelionApp import DandelionAppManifest

# Constants
APPPATHS = ['/Dandelion/Applications']

class Dandelion:

    def __init__(self, disp=None, touch=None) -> None:

        # Log
        self._log = logging.getLogger('Dandelion')

        # Initialize GUI drivers (display + touch + M5Stack)
        lv.init()
        if disp is None:
            self._log.info(
                'Display was not specified. Creating a new display with a new M5Stack.')
            self.ms = M5Stack()
            self.disp = ili9342(m5stack=self.ms)
        else:
            self.ms = disp.m5stack

        if touch is None:
            self._log.info(
                'Touch panel was not specified. Creating a new touch panel.')
            self.touch = ft6336u()

        # TODO: Show boot screen

        # Get app list
        self.appList = self.discoverApplicationManifests()

        # Find a launcher
        for app in self.appList:
            if app.launcher:
                launcherManifest = app
                self._log.info('Launcher found: %s.', launcherManifest.name)
                break
        else:
            launcherManifest = None
            self._log.critical('No launchers found. Unable to start Dandelion Core.')
            sys.exit()

        # Run launcher
        launcherModule = __import__(launcherManifest.moduleName)
        launcher = launcherModule.ENTRYPOINT()


    def discoverApplicationManifests(self) -> list[DandelionAppManifest]:
        manifests = []

        for path in APPPATHS:
            # Make path executable
            sys.path.append(path)

            # Scan for manifests
            app_folders = uos.listdir(path)
            for folder in app_folders:
                try:
                    mpath = path + '/' + folder + '/manifest.json'
                    with open(mpath) as json:
                        manifest = DandelionAppManifest(json, folder)
                        manifests.append(manifest)
                        self._log.info('Loaded app %s.', manifest.name)
                except OSError:
                    self._log.error(
                        'Cannot decode manifest file for %s/%s', path, folder)

        return manifests