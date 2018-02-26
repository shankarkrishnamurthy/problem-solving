def compareVersion(version1, version2):
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """
    v1 = version1.split('.')
    v2 = version2.split('.')
    v1_maj = int(v1[0])
    v2_maj = int(v2[0])
    v1_min = int(v1[1]) if len(v1)>1 else 0
    v2_min = int(v2[1]) if len(v2)>1 else 0
    v1_min_2 = int(v1[2]) if len(v1)>2 else 0
    v2_min_2 = int(v2[2]) if len(v2)>2 else 0
    v1_min_3 = int(v1[3]) if len(v1)>3 else 0
    v2_min_3 = int(v2[3]) if len(v2)>3 else 0

    if v1_maj==v2_maj:
        if v1_min == v2_min:
            if v1_min_2 == v2_min_2:
                if v1_min_3 == v2_min_3:
                    return 0
                elif v1_min_3 < v2_min_3:
                    return -1
                else:
                    return 1
            elif v1_min_2 < v2_min_2:
                return -1
            else:
                return 1
        elif v1_min < v2_min:
            return -1
        else:
            return 1
    elif v1_maj < v2_maj:
        return -1
    else:
        return 1

print compareVersion("1.2", "2.1")
print compareVersion("1.12", "2.1")
print compareVersion("1.13", "1.1")
print compareVersion("1.20", "1.2")
print compareVersion("3.1", "2.1")
print compareVersion("1.0", "1.0")
print compareVersion("2", "0")
print compareVersion("01", "1")
print compareVersion("1.1", "1")
print compareVersion("2", "2.0")
print compareVersion("1", "1.0.1")
print compareVersion("1.0.0", "1")
print compareVersion("3.0.4.10", "3.0.4.2")
