hugo
FILES=$(find public -type f -name '*.html')
for f in $FILES; do
  cat $f >> public/temp
done
sed -i 's/<script type="text\/javascript" src="\/js\/navbar-hamburger.min.js"><\/script>//g' public/temp
sed -i 's/<script type="text\/javascript" src="\/js\/toggle-theme.min.js"><\/script>//g' public/temp
mkdir static/css
uncss --stylesheets css/light.css public/temp > static/css/light.min.css
sed -i 's/"has-text-dark"/"has-text-grey"/g' public/temp
uncss --stylesheets css/dark.css public/temp > static/css/dark.min.css
