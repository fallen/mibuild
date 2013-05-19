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

	("flash", 0,
		Subsignal("adr", Pins("F15", "F16", "C17", "C18", "F14", "G14", "D17",
			"D18", "H12", "G13", "E16", "E18", "K12", "K13", "F17",
			"F18", "H13", "H14", "H15", "H16", "G16", "G18", "J16", "J18",
			"K17", "K18")),
		Subsignal("d", Pins("T8", "R8", "U10", "V13", "U13", "P12", "P6", "N5",
			"R5", "T3", "R3", "V5", "U5", "V14", "T14", "R13")),
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
