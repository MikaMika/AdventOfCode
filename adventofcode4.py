def passport_validation(input):
    import re
    valid = 0
    for passport in (input.split("\n\n")):
        req = 0
        for data in (re.split(" |\n", passport)):
            mandatory = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
            if data.split(":")[0] in mandatory:
                req += 1
        if req == 7:
            valid += 1
    return valid


def passport_validation2(input):
    import re
    valid = 0
    for passport in (input.split("\n\n")):
        passportnew = {
            "byr": "",
            "iyr": "",
            "eyr": "",
            "hgt": "",
            "hcl": "",
            "ecl": "",
            "pid": "",
            "cid": ""
        }
        for data in passport.replace('\n', ' ').split():
            passportnew[data.split(":")[0]] = data.split(":")[1]
        if passportnew["byr"] and passportnew["iyr"] and passportnew[
                "eyr"] and passportnew["hgt"] and passportnew[
                    "hcl"] and passportnew["ecl"] and passportnew["pid"]:
            if int(passportnew["byr"]) >= 1920 and int(
                    passportnew["byr"]) <= 2002:
                if int(passportnew["iyr"]) >= 2010 and int(
                        passportnew["iyr"]) <= 2020:
                    if int(passportnew["eyr"]) >= 2020 and int(
                            passportnew["eyr"]) <= 2030:
                        if (passportnew["hgt"][-2:] == "cm"
                                and int(passportnew["hgt"][:-2]) >= 150
                                and int(passportnew["hgt"][:-2]) <= 193) or (
                                    passportnew["hgt"][-2:] == "in"
                                    and int(passportnew["hgt"][:-2]) >= 59
                                    and int(passportnew["hgt"][:-2]) <= 76):
                            if re.findall(r'^#([A-Fa-f0-9]{6})$',
                                          passportnew["hcl"]):
                                if passportnew["ecl"] in ("amb", "blu", "brn",
                                                          "gry", "grn", "hzl",
                                                          "oth"):
                                    if passportnew["pid"].isdigit() and len(
                                            passportnew["pid"]) == 9:
                                        valid += 1
    return (valid)
