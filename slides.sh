#!/bin/zsh
autoload -U zmv

find . -name '*.ipynb' -exec  jupyter nbconvert {} --to slides \;
find . -name '*.slides.html' -exec sed -i 's/simple\.css/sky.css/;s/\.ipynb/.html/g' {} \;
zmv -f '(*).slides.html' '$1.html'
zmv -f '2-tutorial/(*).slides.html' '2-tutorial/$1.html'
zmv -f '3-solution/(*).slides.html' '3-solution/$1.html'
