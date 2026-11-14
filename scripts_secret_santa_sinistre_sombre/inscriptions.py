from recutils import parse_file

class Inscriptions:
    """
    This class handles inscriptions
    """

    def __init__(self):
        self.inscriptions : list[dict] = []

    def load_recfile(self, recfile: str):
        """
        Load data from a recfile
        """
        with open(recfile, "r") as f:
            rec_data = parse_file(f)
        for rs in rec_data:
            print(rs)
            if rs.descriptor.record_type != "Inscrit":
                continue
            for record in rs.records:
                inscription = {
                    "nom": record.get_field("Nom"),
                    "adresse": record.get_field("Adresse"),
                    "international": record.get_field("International") == "Oui",
                    "est_fr": record.get_field("Est_Fr") == "Oui",
                }
                for field in ["Inspiration", "Notes"]:
                    if record.has_field(field):
                        inscription[field.lower()] = record.get_field(field)
                self.inscriptions.append(inscription)

    def export_to_arcanis(self) -> str:
        """
        This exports the inscriptions to the text format taken by Secret Santa by Arcanis/Maël
        Example line : toto (3 rue toto, [lieutenant, space, marine]) !tata !tutu
        """
        lines = []
        for inscription in self.inscriptions:
            lines.append(f"{inscription["nom"]} ({inscription["adresse"]} [{inscription["inspiration"]}])")
            if not inscription["international"]:
                lines[-1] = lines[-1] + f" {" ".join(["!"+nom for nom in self._get_non_france_inscriptions()])}"
        return "\n".join(lines)

    def _get_non_france_inscriptions(self) -> list[str]:
        """
        Returns a list of the names of every inscriptions not located in france
        """
        return [i["nom"] for i in filter(lambda ins: not ins["est_fr"], self.inscriptions)]

