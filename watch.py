def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        line = s.find('src="')
        line = line + 5
        qpos = s.find('"', line)
        final = s[line:qpos]
        rev1 = final.replace('embed/','')
        rev2 = rev1.replace('be','')
        rev3 = rev2.replace('.com','.be')
        rev4 = rev3.replace('www.','')
        rev5 = rev4.replace('http','https')
        rev6 = rev5.replace('httpss','https')
        if not 'yout' in rev6:
            return None
        elif not 'https' in rev6:
            return None
        return rev6
    except:
        return None




if __name__ == "__main__":
    main()
