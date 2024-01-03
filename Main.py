from zipfile import ZipFile
from os import walk

import GuiUtils
import OSUtils
from PackUtils import *
from OSUtils import *

# Constants
DEFAULT_TEXTURES = "textures"
TEXTURES_PATH = "source_textures/"


# Checks the default textures exists
GuiUtils.sectionPrint("Checking Default Textures")
if not os.path.exists(TEXTURES_PATH + DEFAULT_TEXTURES):
    raise Exception("Default textures folder is INVALID")


# Gets all the zip files from within TEXTURES_FOLDER
GuiUtils.sectionPrint("Getting Packs")
texture_zips = OSUtils.getFiles(TEXTURES_PATH)


# Iterate through each zip and extract it to its own folder
GuiUtils.sectionPrint("Extracting Packs")
for zip_name in texture_zips:
    with ZipFile(TEXTURES_PATH + zip_name, 'r') as zip:
        zip.extractall(path=(TEXTURES_PATH + zip_name.strip(".zip")))
        print('Extracted: ' + zip_name)


# Gets all the folders from within TEXTURES_FOLDER
texture_folders = OSUtils.getFolders(TEXTURES_PATH)
texture_folders.remove(DEFAULT_TEXTURES)


# Checks each pack to see if the valid files are present
GuiUtils.sectionPrint("Checking Packs")
valid_packs = []
for pack in texture_folders:
    if checkTexturePack(TEXTURES_PATH, pack):
        valid_packs += [pack]

GuiUtils.sectionPrint("Debug")
print(valid_packs)
# Remove the default textures folder from the list of usable folders


















# def generatemcmeta():
#     resPackName = nameEntry.get()
#     minecraftVersion = versionEntry.get()
#     packmcmeta = open('pack.mcmeta', 'w+')
#     filecontents = '{"pack":{"pack_format":' + minecraftVersion + ',"description":"' + resPackName + '"}}'
#     packmcmeta.write(filecontents)
#     packmcmeta.close()
#     generateStatus.config(text="The file has been generated!", fg="green")