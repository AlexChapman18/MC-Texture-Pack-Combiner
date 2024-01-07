import os
import json
import shutil

import OSUtils
from EnvVars import *

def checkTexturePack(packs_folder, pack_name):
    FILE_CHECKS = ["pack.mcmeta", "pack.png"]
    FOLDER_CHECKS = ["assets/minecraft/textures"]
    CHECKS = FILE_CHECKS + FOLDER_CHECKS
    pack_path = packs_folder + pack_name

    errors = []
    for check_path in CHECKS:
        if not os.path.exists(pack_path + "/" + check_path):
            errors += ["file/folder: \"" + check_path + "\" is missing"]

    if not errors:
        print("Pack: \"" + pack_name + "\" is OK")
        return True

    else:
        print("Pack: \"" + pack_name + "\" is BAD")
        for error in errors:
            print("\t" + error)
        return False


def createBasePack(outputs_folder, pack_name, pack_json, ):
    pack_path = outputs_folder + pack_name

    if os.path.exists(pack_path):
        return

    # Make the directory structure
    os.mkdir(pack_path)
    os.mkdir(pack_path + "/assets")
    os.mkdir(pack_path + "/assets/minecraft")


    with open(pack_path + "/" + pack_name + ".pckdata", "w") as write_file:
        json.dump(pack_json, write_file)


def readPackData(name):
    pack_path = OUTPUT_PATH + name

    with open(pack_path + "/" + name + ".pckdata", "r") as read_file:
        data = read_file.read()
    return json.loads(data)


def buildPack(pack_name):
    pack_data = readPackData(pack_name)
    pack_path = OUTPUT_PATH + pack_name

    base_pack = pack_data["pckmeta"]["base_pack"]
    if base_pack == "textures":
        OSUtils.copyFolder(TEXTURES_PATH + DEFAULT_TEXTURES, pack_path + PACK_TEXTURES_DIR)
    else:
        OSUtils.copyFolder(TEXTURES_PATH + base_pack + PACK_TEXTURES_DIR, pack_path + PACK_TEXTURES_DIR)

    for type, pack_img in pack_data["texture_data"].items():
        for pack, img in pack_img.items():
            copyTexture(type, pack, pack_name, img)



    # Create a pack PNG of a dirt block for ease
    OSUtils.copyFileNewName(TEXTURES_PATH + DEFAULT_TEXTURES + "/block/dirt.png", pack_path + "/pack.png")

    # create the mcmeta file
    with open(pack_path + "/pack.mcmeta", "w") as write_file:
        json.dump(pack_data["mcmeta"], write_file)

    shutil.make_archive(pack_path, 'zip', pack_path)


def copyTexture(type, src_pack, dst_pack, texture):
    if texture == "*":
        src_path = TEXTURES_PATH + src_pack + PACK_TEXTURES_DIR + type
        dst_path = OUTPUT_PATH + dst_pack + PACK_TEXTURES_DIR + type
        OSUtils.copyFolder(src_path, dst_path)
    else:
        path_end = type + "/" + texture + ".png"
        src_path = TEXTURES_PATH + src_pack + PACK_TEXTURES_DIR + path_end
        dst_path = OUTPUT_PATH + dst_pack + PACK_TEXTURES_DIR + path_end
        OSUtils.copyFile(src_path, dst_path)
