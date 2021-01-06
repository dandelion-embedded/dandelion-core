import utime

import lvgl as lv
from Dandelion.Library.DandelionAppManifest import DandelionAppManifest

TOP_BAR_HEIGHT = 32


class DandelionApp:
    def __init__(self, manifest: DandelionAppManifest):

        self.manifest = manifest

        self.scr = lv.obj()

        # Top bar base
        self.top_bar = lv.cont(self.scr)
        self.top_bar.set_style_local_bg_color(
            lv.cont.PART.MAIN, lv.STATE.DEFAULT, lv.color_hex(0x0)
        )
        self.top_bar.set_width(lv.scr_act().get_width())
        self.top_bar.set_height(TOP_BAR_HEIGHT)
        self.top_bar.align(self.scr, lv.ALIGN.IN_TOP_MID, 0, 0)
        self.top_bar.set_event_cb(self.top_bar_event_cb)

        # Top bar content

        # App name (if not launcher), static, does not update
        if not self.manifest.launcher:
            self.title_label = lv.label(self.top_bar)
            self.title_label.set_text(self.manifest.name)
            self.title_label.align(self.top_bar, lv.ALIGN.CENTER, 0, 0)

        # Time label, value set in refresh, align based on title presence
        self.clock_label = lv.label(self.top_bar)

        # App container
        self.app_container = lv.cont(self.scr)
        self.app_container.set_width(lv.scr_act().get_width())
        self.app_container.set_height(lv.scr_act().get_height() - self.top_bar.get_height())
        self.app_container.align(self.top_bar, lv.ALIGN.OUT_BOTTOM_MID, 0, 0)

    def start(self):
        lv.event_send_refresh_recursive(self.scr)
        lv.scr_load(self.scr)

    def get_container(self):
        return self.app_container

    def top_bar_event_cb(self, tbar, event):
        if event == lv.EVENT.REFRESH:

            # Clock data
            ltime = utime.localtime()
            self.clock_label.set_text("{:0>2}:{:0>2}".format(ltime[3], ltime[4]))

            # Clock realign
            if self.manifest.launcher:
                self.clock_label.align(self.top_bar, lv.ALIGN.CENTER, 0, 0)
            else:
                self.clock_label.align(self.top_bar, lv.ALIGN.IN_LEFT_MID, 8, 0)
