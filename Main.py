from zipfile import ZipFile
import os

import GuiUtils
import PackUtils
import OSUtils
from EnvVars import *
from Pack import Pack

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
    if PackUtils.checkTexturePack(TEXTURES_PATH, pack):
        valid_packs += [pack]




GuiUtils.sectionPrint("Debug")
pack_name = "MyPack1"
pack_base = "textures"
pack_format = 22
pack_description = "My first texture pack"
newPack = Pack(pack_name, pack_base, pack_format, pack_description)
newPack.assignTexture("block", "VanillaXBR - 1.20.4", "activator_rail")
newPack.assignTexture("item", "VanillaXBR - 1.20.4", "*")


PackUtils.createBasePack(OUTPUT_PATH, pack_name, newPack.getJson())


PackUtils.buildPack(pack_name)

print("Done")
# Remove the default textures folder from the list of usable folders


















# def generatemcmeta():
#     resPackName = nameEntry.get()
#     minecraftVersion = versionEntry.get()
#     packmcmeta = open('pack.mcmeta', 'w+')
#     filecontents = '{"pack":{"pack_format":' + minecraftVersion + ',"description":"' + resPackName + '"}}'
#     packmcmeta.write(filecontents)
#     packmcmeta.close()
#     generateStatus.config(text="The file has been generated!", fg="green")