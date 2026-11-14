"""
This is what is launched when the module is ran directly, and not imported.
This is a script.
"""
import os
from scripts_secret_santa_sinistre_sombre.inscriptions import Inscriptions

inscriptions = Inscriptions()
inscriptions.load_recfile(os.environ["INSCRIPTIONS_RECFILE"])
print(inscriptions.export_to_arcanis())

