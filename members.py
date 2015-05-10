import json
import os
import shutil
from pprint import pprint

def main():
    clean()
    build()

def clean():
    if os.path.exists("members.html"):
        os.remove("members.html")
    if os.path.exists("members/"):
        shutil.rmtree("members/")

def build():
    if not os.path.exists("members.html.template"):
        raise ValueError("missing file: members.html.template'")

    active_members_table = ""
    alumni_table = ""
    with open("members.json") as data_file:
        data = json.load(data_file)

    # filter malformed data, and raise exception
    yearless_years = [year for year in data["years"] if "year" not in year]
    if len(yearless_years) > 0:
        raise ValueError("malformed members.json: missing 'years' from %s" % str(yearless_years))

    # sort in reverse chronological order
    sorted_years = sorted([group for group in data["years"]],
                          key= lambda group: group["year"], reverse=True)

    for year in sorted_years:

        # filter malformed data, and raise exception
        nameless_members = [member for member in year["members"] if "name" not in member]
        if len(nameless_members) > 0:
            raise ValueError("malformed members.json: missing 'name' from %s" % str(nameless_members))

        # sort in alphabetical order
        sorted_members = sorted([member for member in year["members"]],
                                key = lambda member: member["name"])

        for member in sorted_members:

            notes = name = interests = tutoring = string = ""

            # name is known to be in the member data
            name = member["name"]
            if "interests" in member:
                interests = member["interests"]
            if "tutoring" in member:
                tutoring = member["tutoring"]
            if "notes" in member:
                notes = member["notes"]
            if "year" in year:
                notes += "  (" + str(year["year"]) + ")"
            if "create_profile" in member and member["create_profile"] == True:
                string += ("<tr><td><a href='members/%s.html'>%s</a></td>" + os.linesep) % (name.replace(" ", "_").lower(), name)

                if not os.path.exists("member.html.template"):
                    raise ValueError("missing file: member.html.template'")
                bio = image = academic_standing = languages = hobbies = ""
                if "bio" in member:
                    bio = member["bio"]
                if "image" in member and os.path.exists(member["image"]):
                    image = "../" + member["image"]
                else:
                    image = "../images/no_image_male.png"
                if "academic_standing" in member:
                    academic_standing = member["academic_standing"]
                if "languages" in member:
                    languages = member["languages"]
                if "hobbies" in member:
                    hobbies = member["hobbies"]

                member_template_file = open("member.html.template", "r")
                member_template_data = member_template_file.read().decode("utf-8")
                member_template_file.close()
                if not os.path.exists("members/"):
                    os.makedirs("members")

                member_output_data = member_template_data.replace("$NAME$", name).replace("$BIO$", bio).replace("$IMAGE$", image).replace("$INTERESTS$", interests).replace("$TUTORING$", tutoring).replace("$ACADEMIC_STANDING$", academic_standing).replace("$LANGUAGES$", languages).replace("$HOBBIES$", hobbies).encode("utf-8")
                member_output_file = open("members/%s.html" % name.replace(" ", "_").lower(), "w")
                member_output_file.write(member_output_data)
                member_output_file.close()

            else:
                string += ("<tr><td>%s</td>" + os.linesep) % name
            if "alumni" in member and member["alumni"] == True:
                string += ("<td style='width:100%'> </td>" + os.linesep) + ("<td></td>" + os.linesep) + ("<td>%s</td></tr>" + os.linesep) % notes
                alumni_table += string
            else:
                string += ("<td>%s</td>" + os.linesep) % interests + ("<td>%s</td>" + os.linesep) % tutoring + ("<td>%s</td></tr>" + os.linesep) % notes
                active_members_table += string

    members_template_file = open("members.html.template", "r")
    members_template_data = members_template_file.read().decode("utf-8")
    members_template_file.close()

    members_output_data = members_template_data.replace("$ACTIVE_MEMBERS$", active_members_table).replace("$ALUMNI$", alumni_table).encode("utf-8")
    members_output_file = open("members.html", "w")
    members_output_file.write(members_output_data)
    members_output_file.close()

if __name__ == "__main__":
    main()
