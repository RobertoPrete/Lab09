import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_analizza_aeroporti(self, e):
        self._model.buildGraph()
        self._view.txt_result.controls.clear()
        numero_vertici = self._model.getNumNodes()
        self._view.txt_result.controls.append(ft.Text(f"Numero vertici del grafo: {numero_vertici}"))
        numero_archi = self._model.getNumEdges()
        self._view.txt_result.controls.append(ft.Text(f"Numero archi del grafo: {numero_archi}"))
        archi = self._model.getAllEdges()
        for u, v, data in archi(data=True):
            self._view.txt_result.controls.append(ft.Text(f"Archi: {u} - {v} con distanza: {data} "))
        self._view.update_page()
