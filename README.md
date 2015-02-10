## Overview

* `css/` is the folder that contains all css used by this website.
    - Modify `css/custom.css` for any changes to the website's styling.
* `faculty.html` displays the faculty involved with our chapter.
* `images/` contains all images (including member pictures) used by this website.
* `index.html` is the main web page.
* `member.html.template` is the template used for our member pages.  Strings of the form`$KEY$` are dynamically inserted when `members.py` is run.
* `members/` is a dynamically generated folder that contains all the member pages.
	- This folder is deleted and re-created each time `members.py` is run.  Do not touch anything in it; otherwise, you will lose your changes.
* `members.html` displays all of our members (including alumni). The data for this web page is populated by `members.html.template` and `members.py`.
* `members.html.template` is the template used for our members page.  Strings of the form `$KEY$` are dynamically inserted when `members.py` is run.
* `members.json` is the database for our chapter's members. More documentation and a schema will arrive, eventually.
* `members.py` parses `members.json` and builds
	- `members.html`, which displays our chapter's members in a table.
	-`members/$member`, which is $member's personal page.
	- More documentation will be available shortly.
* `requirements.html` displays the requirements for joining our chapter.

## Tech Stack

* HTML5
* CSS3
* Skeleton 2.x
* Python 2.7 (compilation)

Any requests that add complexity to this tech stack will be denied. This website will change hands every year to a new executive staff; it is important to keep it as simple as possible.

KISS.

## Contributions

* Alexander Schiffhauer, President 2014
* Disa Mhembere, Secretary 2014
* Carlo Olcese, Member 2014

Special thanks to members of the ACM that continue to host our website, free of charge.

## License

MIT License