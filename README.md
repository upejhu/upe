## UPE

Upsilon Pi Epsilon (UPE): International Honor Society for the Computing and Information Disciplines is the first honor society dedicated to the discipline of computer information systems and computer science.

This repository is The Johns Hopkins University's chapter's [website](https://acm.jhu.edu/~upe "Upsilon Pi Epsilon").  If you're a current member or alumni, please feel free to contribute by making a pull request.

## Documentation

### Adding Members
* Open `members.json`.  Find the `year` in which the member was inducted (or create a new year for a new class).  Fill in appropriate data for the appropriate members, using previous examples as a reference.  Below is a blueprint for a year comprising exactly one hypothetical member:
```json
"year": "1912",
"members": [{
    "alumni": true,
    "create_profile": true,
    "name": "Alan Turing",
    "notes": "Father of Computer Science",
    "interests": "Mathematics, cryptanalysis, computer science, Biology",
    "tutoring": "Modern Cryptography, Automata and Computational Theory",
    "bio": "Alan Turing was a British pioneering computer scientist, mathematician, logician, cryptanalyst, philosopher, mathematical biologist, and marathon and ultra distance runner. ",
    "academic_standing": "PhD, Princeton University",
    "languages": "Automaton",
    "hobbies": "Cracking cryptographic messages",
    "image": "images/alan_turing.jpg"
}]
```
* Running `python members.py` will modify `members.html` such that `members.html` includes references to this new member.  If `create_profile:true` is defined in `members.json`, this script will also create the profile page for this user with the supplied data.

### Changing Members
* Open `members.json` and find the desired member.  Change the appropriate fields and run `python members.py`.

### Removing Members
* Membership to UPE is for life.  However, if you have made an error, simply remove a member from `members.json` and run `python members.py`

### Publishing
* Publishing requires write access to the ACM group UPE.  This is reserved only for the executive branch of our chapter.  To publish changes, `chmod + x publish.sh && ./publish.sh`. 
	- Note that this script will invoke `python members.py` automatically, ensuring the latest changes are pushed.

## File Overview

* `css/` is the folder that contains all css used by this website.
    - Modify `css/custom.css` for any changes to the website's styling.
    - Do not touch `css/skeleeton.css` or `css/normalize.css` as these will be updated without warning.
* `faculty.html` displays the faculty advisors for our chapter.
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
	-`members/$MEMBER`, which is $MEMBER's personal page.
* `publish.sh` is a script that uses rsync to publish changes to the server.  Note that this script will invoke `python members.py` automatically, ensuring the latest changes are pushed.
* `requirements.html` displays the requirements for joining our chapter.

## Tech Stack

* HTML5
* CSS3
* Skeleton 2.x
* Python 2.7 (compilation)

Any requests that add complexity to this tech stack will be denied. This website will change hands every year to a new executive staff; it is important to keep it as simple as possible.

KISS.

## Build/Publish Requirements
* Python 2.7
* rsync
* Write privileges to the UPE group on the ACM servers

## Contributions

* Alexander Schiffhauer, President 2014
* Disa Mhembere, Secretary 2014
* Carlo Olcese, Member 2014
* Jeffrey Dallatezza, President 2013
* Sharon Li, Member 2013

Special thanks to members of the ACM that continue to host our website, free of charge.

## License

MIT License