import math

import lvgl as lv
import lodepng as png
import gc

from Dandelion import Dandelion
from Dandelion.Library.DandelionApp import DandelionApp
from Dandelion.Library.DandelionAppManifest import DandelionAppManifest


class Springboard(DandelionApp):
    def __init__(self, manifest: DandelionAppManifest):
        super().__init__(manifest)

        self.container = super().get_container()
        self.container.set_style_local_bg_color(lv.cont.PART.MAIN,
                                                lv.STATE.DEFAULT,
                                                lv.color_hex(0x000000))

        self.manifests = Dandelion.discoverApplicationManifests()

        # Count apps
        self.numberOfApps = 0
        for m in self.manifests:
            if m.visibleInLauncher:
                self.numberOfApps += 1

        self.numberOfColumns = self.container.get_width() // 100

        # Scrollview
        self.scrollview = lv.page(self.container)
        self.scrollview.set_size(self.container.get_width(),
                              self.container.get_height())
        self.scrollview.align(self.container, lv.ALIGN.IN_TOP_LEFT, 0, 0)
        self.scrollview.set_style_local_bg_opa(lv.page.PART.BG,
                                            lv.STATE.DEFAULT, lv.OPA._0)

        # Group
        self.scrollgroup = lv.group_create()

        # Populate pages
        index = 0
        for m in filter(lambda x: (x.visibleInLauncher), self.manifests):

            i = SpringboardIcon(self.scrollview, m)
            self.scrollgroup.add_obj(i)
            index += 1

        super().start()


class SpringboardIcon(lv.cont):
    def __init__(self, parent, manifest: DandelionAppManifest):
        super().__init__(parent)

        self.set_size(80, 80)
        self.set_style_local_bg_opa(self.PART.MAIN, lv.STATE.DEFAULT,
                                    lv.OPA._0)

        self.icon = lv.img(self)

        with open(manifest.appPath + manifest.iconPath, 'rb') as f:
            icn_data = f.read()

        img_dsc = lv.img_dsc_t({
            "header": {
                "always_zero": 0,
                "w": 64,
                "h": 64,
                "cf": lv.img.CF.INDEXED_4BIT,
            },
            "data_size": len(icn_data),
            "data": icn_data,
        })

        self.icon.set_size(64, 64)
        self.icon.align(self, lv.ALIGN.IN_TOP_MID, 0, 0)
        self.icon.set_src(img_dsc)
        self.icon.set_offset_x(-8)

        self.label = lv.label(self)
        self.label.set_text(manifest.name)
        self.label.align(self, lv.ALIGN.IN_BOTTOM_MID, 0, 0)


ENTRYPOINT = Springboard
