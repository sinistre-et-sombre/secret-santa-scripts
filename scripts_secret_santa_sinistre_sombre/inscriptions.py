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
                    "international": record.get_field("International") == "Oui"
                }
                for field in ["Inspiration", "Notes"]:
                    if record.has_field(field):
                        inscription[field.lower()] = record.get_field(field)
                self.inscriptions.append(inscription)

    def save_data(self, recfile:str, data: dict):
        pass


