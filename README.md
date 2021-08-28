# NeoDaysPlus

Expanded version of the CDDA tileset NeoDays, differing terrain tiling planned.

## Additions:
- graffiti/general_graffiti/shelter_graffiti
- protein_bar_evac

## Things to recolour
- iron_pot

## Things to add
- f_rotary_clothesline

## Important ImageMagik commands (Adjust for OG or Plus work)

Split spritesheet: `convert tiles.png -crop 10x10 tile.png`

Define files: `files=$(ls Plus/tile*.png | sort -t '-' -n -k 2 | tr '\n' ' ')`

Montage: `montage $files -tile 16x -background none -geometry +0+0 plus.png`
