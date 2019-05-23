import platform
if platform.system() == "Java":
    import JUI
    mUI = JUI
else:
    import CUI
    mUI = CUI

QnA = mUI.QnA
WA = mUI.wordAdder
dD = mUI.dispDict
hub = mUI.hub