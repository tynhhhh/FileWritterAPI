import datetime
import os
import pwd

def get_creation_time(file_path):
    FILE_TIME_OFFSET = 116444736000000000  # Number of 100-nanosecond intervals between the Windows epoch (Jan 1, 1601) and Unix epoch (Jan 1, 1970)
    creation_time = os.path.getctime(file_path)
    return datetime.datetime.utcfromtimestamp((creation_time - FILE_TIME_OFFSET) * 1e-7)

def get_file_owner(file_path):
    file_stat = os.stat(file_path)
    uid = file_stat.st_uid
    try:
        owner_name = pwd.getpwuid(uid).pw_name
    except KeyError:
        owner_name = f"UID {uid}"
    return owner_name

if __name__ == "__main__":
    test = get_file_owner("./uploaded_files/src.rar")
    print(test)