hugo
FILES=$(find public -type f -name '*.html')
for f in $FILES; do
  cat $f >> public/temp
done
sed -i 's/<script type="text\/javascript" src="\/js\/navbar-hamburger.min.js"><\/script>//g' public/temp
sed -i 's/<script type="text\/javascript" src="\/js\/toggle-theme.min.js"><\/script>//g' public/temp
sed -i '0,/<a role="button" class="navbar-burger burger" aria-label="menu" aria-expanded="false" data-target="navContent">/{s/<a role="button" class="navbar-burger burger" aria-label="menu" aria-expanded="false" data-target="navContent">/<a role="button" class="navbar-burger burger is-active" aria-label="menu" aria-expanded="false" data-target="navContent">/}' public/temp
sed -i '0,/<div id="navContent" class="navbar-menu">/{s/<div id="navContent" class="navbar-menu">/<div id="navContent" class="navbar-menu is-active">/}' public/temp
mkdir static/css
uncss --stylesheets css/style.css public/temp > static/css/style.min.css
# sed -i 's/"has-text-dark"/"has-text-grey"/g' public/temp
# uncss --stylesheets css/dark.css public/temp > static/css/dark.min.css
