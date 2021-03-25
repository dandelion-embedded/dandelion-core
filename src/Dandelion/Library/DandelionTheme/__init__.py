import lvgl as lv


class DefaultContStyle(lv.style_t):
    def __init__(self):
        super().__init__()
        self.set_radius(lv.STATE.DEFAULT, 0)
        self.set_border_width(lv.STATE.DEFAULT, 0)
        self.set_bg_color(lv.STATE.DEFAULT, lv.color_hex(0x333333))

class DefaultPageStyle(lv.style_t):
    def __init__(self):
        super().__init__()
        self.set_radius(lv.STATE.DEFAULT, 0)
        self.set_border_width(lv.STATE.DEFAULT, 0)
        self.set_bg_color(lv.STATE.DEFAULT, lv.color_hex(0x000000))

class DefaultLabelStyle(lv.style_t):
    def __init__(self):
        super().__init__()
        self.set_text_color(lv.STATE.DEFAULT, lv.color_hex(0xFFFFFF))


class DandelionTheme(lv.theme_t):
    def __init__(self):
        super().__init__()
        self.cont_style = DefaultContStyle()
        self.label_style = DefaultLabelStyle()
        self.page_style = DefaultPageStyle()

        # This theme is based on active theme (material)
        base_theme = lv.theme_get_act()
        self.copy(base_theme)

        # This theme will be applied only after base theme is applied
        self.set_base(base_theme)

        # Set the "apply" callback of this theme to our custom callback
        self.set_apply_cb(self.apply)

        # Activate this theme
        self.set_act()

    def apply(self, theme, obj, name):
        if name == lv.THEME.CONT:
            obj.add_style(obj.PART.MAIN, self.cont_style)
        elif name == lv.THEME.LABEL:
            obj.add_style(obj.PART.MAIN, self.label_style)
        elif name == lv.THEME.PAGE:
            obj.add_style(obj.PART.MAIN, self.page_style)
