import machine
from Dandelion import Dandelion

# Display
from ili9XXX import ili9488
import ili9XXX
import espidf as esp

machine.freq(240000000)

disp = ili9488(
    mosi=13,
    clk=14,
    cs=15,
    dc=2,
    rst=4,
    power=-1,
    backlight=27,
    backlight_on=1,
    rot=ili9XXX.LANDSCAPE | ili9XXX.MADCTL_MX | ili9XXX.MADCTL_MY,
    spihost=esp.HSPI_HOST,
    mhz=40,
    factor=16,
    hybrid=True,
    width=480,
    height=320)

dan = Dandelion(disp=disp)
