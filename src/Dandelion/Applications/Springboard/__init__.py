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
                                                lv.color_hex(0x0A0A0A))

        self.manifests = Dandelion.discoverApplicationManifests()

        # Count apps
        self.numberOfApps = 0
        for m in self.manifests:
            if m.visibleInLauncher:
                self.numberOfApps += 1

        self.numberOfRows = self.container.get_height() // 100
        self.numberOfColumns = self.container.get_width() // 100

        self.numberOfPages = 2  # (len(manifests) / (numberOfColumns * numberOfRows))

        # Tabview
        self.tabview = lv.tabview(self.container)
        self.tabview.set_btns_pos(lv.tabview.TAB_POS.NONE)
        self.tabview.set_size(self.container.get_width(),
                              self.container.get_height())
        self.tabview.align(self.container, lv.ALIGN.IN_TOP_LEFT, 0, 0)
        self.tabview.set_style_local_bg_opa(lv.tabview.PART.BG,
                                            lv.STATE.DEFAULT, lv.OPA._0)

        # Generate pages
        self.pageContainers = []
        for i in range(self.numberOfPages):
            page = self.tabview.add_tab("Page {}".format(i))
            page.set_style_local_pad_all(lv.page.PART.SCROLLABLE,
                                         lv.STATE.DEFAULT, 0)
            c = lv.cont(page)
            c.set_fit(lv.FIT.PARENT)
            c.set_click(False)
            c.set_style_local_bg_opa(lv.tabview.PART.BG, lv.STATE.DEFAULT,
                                     lv.OPA._0)
            c.set_layout(lv.LAYOUT.GRID)

            pad = (c.get_width() -
                   (80 * self.numberOfColumns)) / (self.numberOfColumns + 1)
            c.set_style_local_pad_left(lv.cont.PART.MAIN, lv.STATE.DEFAULT,
                                       int(pad))
            c.set_style_local_pad_right(lv.cont.PART.MAIN, lv.STATE.DEFAULT,
                                        int(pad))
            c.set_style_local_pad_inner(lv.cont.PART.MAIN, lv.STATE.DEFAULT,
                                        int(pad))
            self.pageContainers.append(c)

        # Populate pages
        index = 0
        for m in range(0, 10):
            page: int = index // (self.numberOfRows * self.numberOfColumns)
            current_container = self.pageContainers[page]
            # with open('/Dandelion/Applications/Settings/icon.png' ,'rb') as f:
            # png_data = f.read()

            # png_img_dsc = lv.img_dsc_t({
            # 'data_size': len(png_data),
            # 'data': png_data})

            i = SpringboardIcon(current_container, self.manifests[0])
            index += 1

        super().start()


class SpringboardIcon(lv.cont):
    def __init__(self, parent, manifest: DandelionAppManifest):
        super().__init__(parent)

        gc.collect()

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
                "cf": lv.img.CF.INDEXED_8BIT,
            },
            "data_size": len(icn_data),
            "data": icn_data,
        })

        # self.icon.set_size(64, 64)
        self.icon.set_src(img_dsc)
        self.icon.align(self, lv.ALIGN.IN_TOP_MID, 0, 0)

        self.label = lv.label(self)
        self.label.set_text("Test test")
        self.label.align(self, lv.ALIGN.IN_BOTTOM_MID, 0, 0)


ENTRYPOINT = Springboard
