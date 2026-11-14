from scripts_secret_santa_sinistre_sombre.inscriptions import Inscriptions

class TestInscriptions:

    def test_inscriptions(self):
        inscriptions = Inscriptions()
        assert inscriptions.inscriptions == []

    def test_load_data(self):
        inscription_recfile_example = "inscriptions.rec.example"
        inscriptions = Inscriptions()
        inscriptions.load_recfile(inscription_recfile_example)
        assert len(inscriptions.inscriptions) == 3
        assert inscriptions.inscriptions[0]["nom"] == "Lucifer"
        assert inscriptions.inscriptions[0]["adresse"] == "666 Rue de Cerbère, Sixième Cercle, Enfers"
        assert inscriptions.inscriptions[0]["inspiration"] == "Soufre, Fausse idole, Diablotin"
        assert inscriptions.inscriptions[0]["international"]
        assert inscriptions.inscriptions[0]["est_fr"]
        assert inscriptions.inscriptions[0]["notes"] == "Pas de pairing avec l’Archange Michel svp"
        assert inscriptions.inscriptions[1]["nom"] == "Michel"
        assert inscriptions.inscriptions[2]["nom"] == "Père Noël"

    def test_export_to_arcanis(self):
        inscription_recfile_example = "inscriptions.rec.example"
        inscriptions = Inscriptions()
        inscriptions.load_recfile(inscription_recfile_example)
        res = inscriptions.export_to_arcanis()
        validates = """Lucifer (666 Rue de Cerbère, Sixième Cercle, Enfers [Soufre, Fausse idole, Diablotin])
Michel (Jardins florissants, Paradis [Guerrier, pureté, balance]) !Père Noël
Père Noël (Ateliers Noël, Rovaniemi, Finlande [Joie, Neige, Renne])"""
        assert res == validates

    def test_get_non_france_inscriptions(self):
        inscription_recfile_example = "inscriptions.rec.example"
        inscriptions = Inscriptions()
        inscriptions.load_recfile(inscription_recfile_example)
        res = inscriptions._get_non_france_inscriptions()
        assert res == ["Père Noël"]
        
