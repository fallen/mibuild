#
# COPYRIGHT (C) 2013 Yann Sionneau <yann.sionneau@gmail.com>
# License: BSD
#

from mibuild.generic_platform import *
from mibuild.xilinx_ise import XilinxISEPlatform, CRG_SE

_io = [
	("user_led", 0, Pins("U16"), IOStandard("LVCMOS33"), Misc("SLEW=QUIETIO")),
	("user_led", 1, Pins("V16"), IOStandard("LVCMOS33"), Misc("SLEW=QUIETIO")),
	("user_led", 2, Pins("U15"), IOStandard("LVCMOS33"), Misc("SLEW=QUIETIO")),
	("user_led", 3, Pins("V15"), IOStandard("LVCMOS33"), Misc("SLEW=QUIETIO")),
	("user_led", 4, Pins("M11"), IOStandard("LVCMOS33"), Misc("SLEW=QUIETIO")),
	("user_led", 5, Pins("N11"), IOStandard("LVCMOS33"), Misc("SLEW=QUIETIO")),
	("user_led", 6, Pins("R11"), IOStandard("LVCMOS33"), Misc("SLEW=QUIETIO")),
	("user_led", 7, Pins("T11"), IOStandard("LVCMOS33"), Misc("SLEW=QUIETIO")),

	("user_btn", 0, Pins("B8"), IOStandard("LVCMOS33")),
	("user_btn", 1, Pins("A8"), IOStandard("LVCMOS33")),
	("user_btn", 2, Pins("C4"), IOStandard("LVCMOS33")),
	("user_btn", 3, Pins("C9"), IOStandard("LVCMOS33")),
	("user_btn", 4, Pins("D9"), IOStandard("LVCMOS33")),
	
	("clk100", 0, Pins("V10"), IOStandard("LVCMOS33")),

	("flash_rst_n", 0, Pins("T4"), IOStandard("LVCMOS33")),
	("flash_clk", 0, Pins("R10"), IOStandard("LVCMOS33")),

	("flash", 0,
		Subsignal("adr", Pins("K18", "K17", "J18", "J16", "G18", "G16", "H16", "H15", "H14", "H13", "F18", "F17", "K13", "K12", "E18", "E16", "G13", "H12", "D18", "D17", "G14", "F14", "C18", "C17", "F16", "F15")),
		Subsignal("d", Pins("R13", "T14", "V14", "U5", "V5", "R3", "T3", "R5", "N5", "P6", "P12", "U13", "V13", "U10", "R8", "T8")),
		Subsignal("oe_n", Pins("L18")),
		Subsignal("we_n", Pins("M16")),
		Subsignal("ce_n", Pins("L17")),
		Subsignal("adv", Pins("H18")),
		Subsignal("wait", Pins("V4")),
		IOStandard("LVCMOS33"), Misc("SLEW=FAST")
	),
	
	("serial", 0,
		Subsignal("tx", Pins("N18"), IOStandard("LVCMOS33"), Misc("SLEW=SLOW")),
		Subsignal("rx", Pins("N17"), IOStandard("LVCMOS33"))
	),
	

]

class Platform(XilinxISEPlatform):
	def __init__(self):
		XilinxISEPlatform.__init__(self, "xc6slx16-3-csg324", _io,
			lambda p: CRG_SE(p, "clk100", "user_btn", 10.0))
