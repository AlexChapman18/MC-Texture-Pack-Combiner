import json

PACK_JSON_TEMPLATE = """
{
    "pckmeta": {
        "version": 1,
        "name": "null"
    },
    "texture_data": {},
    "mcmeta": {
        "pack": {
            "pack_format": -1,
            "description": "null"
        }
    }
}
"""


class Pack:
    def __init__(self, pack_name, pack_base, pack_format, pack_description, types):
        self.pack_json = json.loads(PACK_JSON_TEMPLATE)
        self.pack_json["pckmeta"]["name"] = pack_name
        self.pack_json["pckmeta"]["base_pack"] = pack_base
        self.pack_json["mcmeta"]["pack"]["pack_format"] = pack_format
        self.pack_json["mcmeta"]["pack"]["description"] = pack_description
        for type in types:
            self.pack_json["texture_data"][type] = {}
            self.pack_json["texture_data"][type+"_base"] = pack_base

    def assignTexture(self, type, pack, name):
        self.pack_json["texture_data"][type].update({pack: name})

    def assignTextures(self, type, pack):
        self.pack_json["texture_data"][type] += {pack: "*"}

    def getJson(self):
        return self.pack_json

    def changeTypeBase(self, type, base):
        self.pack_json["texture_data"][type + "_base"] = base
