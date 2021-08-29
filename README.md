# NeoDaysPlus
Expanded and continuously developed version of the CDDA tileset NeoDays that's being completed with mostly reused NeoDays references if they makes sense, otherwise creating new sprites for missing items.

[Credit for anything not 100% mine goes to the original NeoDays tileset](https://github.com/I-am-Erk/CDDA-Tilesets)

## Differences
- Terrain autotiling that still retains the "NeoDays feel" but smoothing out some noise
- Removed light-blue open air tile for light-sensitivity.

## Additions:
- graffiti/general_graffiti/shelter_graffiti
- protein_bar_evac

## TODO:
Currently these items are using reused references and if things get too confusing, will revisit these lesser TODOs

### Things to recolour (low priority)
- [ ] iron_pot
- [ ] foodplace_snack_bar
- [ ] foodperson_mask
- [ ] board games

### Sprites to add (low priority)
- [ ] brush
- [ ] adhesive_bandages
- [ ] office_holepunch
- [ ] stapler

#### Mod support (literally no priority)
Currently working through Vanilla completion

#### Important ImageMagik commands
Split spritesheet (if needed): `convert tiles.png -crop 10x10 tile.png`

Define files: `files=$(ls Plus/tile*.png | sort -t '-' -n -k 2 | tr '\n' ' ')`

Montage: `montage $files -tile 16x -background none -geometry +0+0 plus.png`
