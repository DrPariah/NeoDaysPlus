# Contribution Guide
So you want to help grow the NeoDaysPlus tileset? Thank you, you're awesome! 

Here is a guide to getting started:

## Pre-Requisites:
- Git
- Python3 & pip
- Pillow
    - `python3 -m pip install --upgrade Pillow` - if missing

## 1. Checkout the source
- Clone the `main` repository branch (will be the most up to date compared to the source code in 'Releases')
- My suggestion is to not put it directly into the Cataclysm gfx folder to give yourself a clean, safe workspace

## 2. Create a branch
- Wanting to have credit up front, and keep things "organised", please create a branch using the following naming conventions:
    - `Username/code/code-change-short-description` - For any additions/improvements/optimizations you want to make to the scripts
        - eg. `v3rv41n/code/faster-spritesheet-gen`
    - `Username/feature/feature-name` - For changes to existing tiles that make them more complex (ones that include auto/multi-tiling, seasonal changes, etc)
        - eg. `v3rv41n/feature/autotiled-asphalt`
    - `Username/tiles/tile-kind` - For adding one or more tiles of a specific kind/theme, 
        - eg. `v3rv41n/tiles/zombie-cow`, or if the set is of multiple themes, please use `misc-tiles`

## 3. Create a/some tile(s)
- Have names be descriptive (`id` value *heavily* preferred - covered in next step)
    - eg. `mon_zow.png`
- For large tiles, the tile dimension is `20x20px`
- For small tiles, the tile dimension is `10x10px`
- When in doubt about sizing/spacing/styling of your tile(s), you can always use an existing tile as a template
- Export image for web as `.png`, this strips all unnecessary data from the image, and if it's not a `.png`, the scripts won't work properly

## 4. Create the json file for the tile(s)
- Using `tile_template.json` as well... a template, replace `NAME_OF_ASSOCIATED_TILE` with the created tile image name (without .png)
    - eg. Created tile `mon_zow.png` would be represented in json as `mon_zow`
- replace `ID_FROM_CDDA_DATA_JSON` with the `id` from the `CDDA/Data/json`
    - Open the `CDDA/Data/json` folder in a text editor for easy searching (I have a copy of this folder saved off for ease of access and protection from accidental saves)
    - Do a project-wide search for the missing tile using the name that appears in-game
    - Copy (don't cut) the corresponding `id` value to the template json file's `id` value (the display name in-game sometimes isn't the same as the `id`)
- Save as a new json file using the same filename as the associated tile png (`id` value *heavily* preferred)
    - eg. `mon_zow.json`

## 5. Move new files to appropriate tile size folder
- Large tiles --> `Large_20x20/`
- Small tiles --> `Small_10x10/`
- They are no folders outside of size to worry about as the scripts just sort alphabetically (and why "organized" was in quotes earier)

## 6. Combine and make tileset
- In the terminal, `cd` to the `NeoDaysPlus` directory
- Commands to make the scripts executable:
    - `chmod +x Combine.py` - Script for combining all of the tiles together in their size-appropriate spritesheet pngs and builds tile_config.json from all the separate json files
    - `chmod +x MakeNDP.sh` - Creates a NeoDaysPlus tileset folder in the current directory
- Run `./Combine.py`
- Run `./MakeNDP.sh`

## 7. Move the newly created tileset folder to the Cataclysm gfx folder

## 8. Test your tiles in-game
- Take screenshots (and crop them) of newly-added working tiles

## 9. Create a PR
- More than likely, the auto-generated name for the PR will be sufficient
- In the description of the PR, please list any added tiles by their `id` value, and  the description of any additions/features/improvements/optimizations
- Add cropped screenshots from testing
- Smash that `Create Pull Request` button

## 10. Pat yourself on the back
- Congrats! Once reviewed and merged into the `main` branch, shout-outs for your additions will be made in the following version's release notes, and you will have my eternal gratitude
