#!/bin/bash
<< COMM
python members.py
printf "%s" "user: "
read user
rsync -avz --exclude '.*' --exclude '*.py' --exclude '*.sh' --exclude '*.html.template' --exclude '*.json' --exclude '*.md'  . $user@acm.jhu.edu:/afs/acm.jhu.edu/group/upe/public_html
COMM

python members.py
WEBSITE_ROOT=../upejhu.github.io/
cp -r *.html css images members $WEBSITE_ROOT 
cd $WEBSITE_ROOT
git pull origin master
git commit -am "Website update"
git push origin master
