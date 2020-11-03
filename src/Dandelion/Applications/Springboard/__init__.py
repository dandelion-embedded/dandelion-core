import lvgl as lv

from Dandelion.Library.DandelionApp import DandelionApp
from Dandelion.Library.DandelionAppManifest import DandelionAppManifest


class Springboard(DandelionApp):
    def __init__(self, manifest: DandelionAppManifest):
        super().__init__(manifest)

        container = super().get_container()
        container.set_style_local_bg_color(
            lv.cont.PART.MAIN, lv.STATE.DEFAULT, lv.color_hex(0x222222)
        )

        label = lv.label(container)
        label.set_text(manifest.name)
        label.align(container, lv.ALIGN.CENTER, 0, 0)


ENTRYPOINT = Springboard
