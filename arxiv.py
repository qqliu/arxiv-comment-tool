#author: Quanquan C. Liu

import argparse, re, os

ADDITIONAL_IF = ['\iffalse']

ADDITIONAL_COMMANDS = ['\\todo']

removing = False
removing_command = False

def removeComments(s):
    news = re.sub(re.compile("%.*?\n"), "", s)
    num_comments = s.split("%")

    if "%" in s and num_comments[0].strip() != "":
        return re.sub(re.compile("%.*?\n"), "\n", s)
    elif "%" in s and num_comments[0].strip() == "":
        return ""
    return news

def removeCommentTags(line, tags):
    global removing

    if "\\fi" in str(line):
        if removing:
            removing = False
            return ""

    words = line.split()
    for w in words:
        if w in tags:
            removing = True
            return ""

    if removing:
        return ""

    return line

def remove_command(line, command):
    global removing_command
    r = line.split(command)
    for i in range(1, len(r)):
        for j in range(len(r[i])):
            if r[i][j] == "}":
                removing_command = False
                return r[i][j+1:len(r[i])] + ''.join(r[i+1:len(r)])
    return ""

def removeCommands(line, commands):
    global removing_command
    if removing_command and len(line) > 0:
        s = remove_command(line, "")
        return removeCommands(s, commands)

    for command in commands:
        if command in line and "\\newcommand" not in line:
            removing_command = True
            s = remove_command(line, command)
            if len(s) > 0:
                return line.split(command)[0] + removeCommands(s, commands)
    return line

def process(line):
    c = removeComments(line)
    c = removeCommentTags(c, ADDITIONAL_IF)
    c = removeCommands(c, ADDITIONAL_COMMANDS)
    return c

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', help = 'files', nargs='+')
    parser.add_argument('--folder', help = 'folders')

    parser.add_argument('--encoding', '-e', default='utf-8')

    args = parser.parse_args()
    folder = args.folder
    if not os.path.exists(folder):
        os.mkdir(folder)

    for arg in args.filename:
        if not arg == '--filename':
            with open(arg, "r") as f:
                newf = open(folder + "/" + arg, "w")

                line = f.readline()

                while line:
                    processed = process(line)
                    if not processed == "":
                        newf.write(processed)
                    line = f.readline()

if __name__ == '__main__':
    main()
