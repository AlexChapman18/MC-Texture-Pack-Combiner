import os.path
from zipfile import ZipFile
from os import walk

# Constants
DEFAULT_TEXTURES_FOLDER = "textures"
TEXTURES_PATH = "source_textures/"

# Gets all the zip files from within TEXTURES_FOLDER
texture_zips = []
for (dirpath, dirnames, filenames) in walk(TEXTURES_PATH):
    texture_zips.extend(filenames)
    break

# Iterate through each zip and extract it to its own folder
for zip_name in texture_zips:
    with ZipFile(TEXTURES_PATH + zip_name, 'r') as zip:
        zip.extractall(path=(TEXTURES_PATH + zip_name.strip(".zip")))
        print('Extracted: ' + zip_name)


# Gets all the folders from within TEXTURES_FOLDER
texture_folders = []
for (dirpath, dirnames, filenames) in walk(TEXTURES_PATH):
    texture_folders.extend(dirnames)
    break
texture_folders.remove(DEFAULT_TEXTURES_FOLDER)


def checkFolderIntegrity(path):
    FILE_CHECKS = ["pack.mcmeta", "pack.png"]
    FOLDER_CHECKS = ["assets/minecraft/textures"]
    CHECKS = FILE_CHECKS + FOLDER_CHECKS

    for check_path in CHECKS:
        if not os.path.exists(path + "/" + check_path):
            print("file/folder: \"" + check_path + "\" does not exist!")
            return False
    return True


print(checkFolderIntegrity(TEXTURES_PATH + texture_folders[0]))
# Remove the default textures folder from the list of usable folders



# print(texture_folders)

















# def generatemcmeta():
#     resPackName = nameEntry.get()
#     minecraftVersion = versionEntry.get()
#     packmcmeta = open('pack.mcmeta', 'w+')
#     filecontents = '{"pack":{"pack_format":' + minecraftVersion + ',"description":"' + resPackName + '"}}'
#     packmcmeta.write(filecontents)
#     packmcmeta.close()
#     generateStatus.config(text="The file has been generated!", fg="green")