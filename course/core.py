import os, requests, sys, json
from datetime import datetime as dt


original_filename = "cautrucmonhoc.json"
new_filename = "cautrucmonhoc_new.json"


def export_file():
    if os.path.exists(original_filename):
        hcmut_courses = "hcmut_courses"
        if not os.path.exists(hcmut_courses):
            os.makedirs(hcmut_courses)
        with open(original_filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        for course in data:
            msmh = course["msmh"]
            file_name = f"{msmh}.json"
            file_path = os.path.join(hcmut_courses, file_name)
            with open(file_path, "w", encoding="utf-8") as output_file:
                json.dump(course, output_file, ensure_ascii=False, indent=4)
        print("Files have been created.")
    else:
        print(f"Cannot found cautrucmonhoc.json")
        print(f"The programme is exiting...")
        sys.exit(0)


def overwrite_file():
    if os.path.exists(original_filename) and os.path.exists(new_filename):
        os.remove(original_filename)
        os.rename(new_filename, original_filename)
        print(f"'{original_filename}' had been created.")
    elif os.path.exists(new_filename):
        os.rename(new_filename, original_filename)
        print(f"'{original_filename}' had been created.")
    else:
        print("Please check if there is at least file name cautrucmonhoc_new.json.\nOr try run programme again.")
        print("The programme is exiting...")
        sys.exit(0)
#def download_file()
#def compare_modified_date()
#def file_modified_date()
#def website_modified_date()
#def is_file_exist()
#def is_website_alive()