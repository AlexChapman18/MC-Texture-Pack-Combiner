import os

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
