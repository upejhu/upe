python members.py
printf "%s" "user: "
read user
rsync -avz --exclude '.*' --exclude '*.py' --exclude '*.sh' --exclude '*.html.template' --exclude '*.json' --exclude '*.md'  . $user@egg.acm.jhu.edu:/afs/acm.jhu.edu/group/upe/public_html
