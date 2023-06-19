
from google.colab import files
uploaded = files.upload()


import pygltflib
import math
import time

class AssetKit:
    def __init__(self, gltf_file):
        self.gltf_file = gltf_file
        self.model = pygltflib.GLTF2().load(gltf_file)
        self.root = self.model.nodes[0]
        self.parts = []
        for part in self.model.meshes:
            part_node = self.root.children[part.name]
            part_mesh = part.mesh
            part_instance = pygltflib.Instance(mesh=part_mesh)
            part_instance.matrix = part_node.matrix
            self.parts.append(part_instance)

    def render(self):
        for part in self.parts:
            part.render()

    def drag_and_drop(self, x, y):
        for part in self.parts:
            if part.intersects(x, y):
                part.position = [x, y, part.position[2]]

    def snap(self, factor):
        for part in self.parts:
            part.position = [round(part.position[0] / factor) * factor,
                             round(part.position[1] / factor) * factor,
                             part.position[2]]

    def keyboard_shortcuts(self, key):
        if key == ord('1'):
            self.bring_up_asset_kit()
        elif key == ord('5'):
            self.factor = 1
        elif key == ord('6'):
            self.factor = 0.1
        elif key == ord('7'):
            self.factor = 0.01
        elif key == ord('8'):
            self.factor = 0.001
        elif key == ord('9'):
            self.factor = 0.0001

    def bring_up_asset_kit(self):
        self.asset_kit = pygltflib.GLTF2().load("asset_kit.gltf")
        self.asset_kit_root = self.asset_kit.nodes[0]

    def main(self):
        window = pygltflib.Window()
        while not window.should_close():
            window.clear()
            self.render()
            self.drag_and_drop(window.mouse_x, window.mouse_y)
            self.snap(self.factor)
            self.keyboard_shortcuts(window.key)
            window.update()


class Phone:
    def __init__(self, gltf_file):
        self.gltf_file = gltf_file
        self.model = pygltflib.GLTF2().load(gltf_file)
        self.root = self.model.nodes[0]
        self.parts = []
        for part in self.model.meshes:
            part_node = self.root.children[part.name]
            part_mesh = part.mesh
            part_instance = pygltflib.Instance(mesh=part_mesh)
            part_instance.matrix = part_node.matrix
            self.parts.append(part_instance)

    def render(self):
        for part in self.parts:
            part.render()

    def drag_and_drop(self, x, y):
        for part in self.parts:
            if part.intersects(x, y):
                part.position = [x, y, part.position[2]]

    def snap(self, factor):
        for part in self.parts:
            part.position = [round(part.position[0] / factor) * factor,
                             round(part.position[1] / factor) * factor,
                             part.position[2]]

    def keyboard_shortcuts(self, key):
        if key == ord('1'):
            self.bring_up_asset_kit()
        elif key == ord('5'):
            self.factor = 1
        elif key == ord('6'):
            self.factor = 0.1
        elif key == ord('7'):
            self.factor = 0.01
        elif key == ord('8'):
            self.factor = 0.001
        elif key == ord('9'):
            self.factor = 0.0001

    def bring_up_asset_kit(self):
        self.asset_kit = AssetKit("asset_kit.gltf")
        self.asset_kit_root = self.asset_kit.root

    def main(self):
        window = pygltflib.Window()
        while not window.should_close():
            window.clear()
            self.render()
            self.drag_and_drop(window.mouse_x, window.mouse_y)
            self.snap(self.factor)
            self.keyboard_shortcuts(window.key)
            window.update()


if __name__ == "__main__":
    phone = Phone("phone.gltf")
    phone.main()
