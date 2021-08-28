# NeoDays+
Expanded version of the CDDA tileset NeoDays, differing terrain tiling planned.

## Things to recolour
- iron_pot
- rake
- rock_large

## Things to add
- f_rotary_clothesline
- graffiti (including):
  - shelter_graffiti
  - general_graffiti


## Important ImageMagik commands
Split spritesheet: `convert tiles.png -crop 10x10 tile.png`
Define files: `files=$(ls Exploded/tile*.png | sort -t '-' -n -k 2 | tr '\n' ' ')`
Montage: `montage $files -tile 16x -background none -geometry +0+0 tiles.png`
