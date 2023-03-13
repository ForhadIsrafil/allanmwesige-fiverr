from glob import glob
import pandas as pd
import json
import os

extensions = ["XML", "xml"]
file_info = {
    'CAMT 53': [],
    'SEPA': [],
    'unsupported standard': []
}

for path in glob("_data_/*"):
    try:
        file_extension = path.split(".")
        # print(file_extension)
    except Exception as e:
        # print(e)
        pass

    with open(path, "r", encoding="ISO-8859-1") as file:
        file_data = file.read()

        # -----------------------------------------------------------------
        if ("xml" in path or "XML" in path) and "camt.053" in file_data:
            # print("camt.053", path)
            file_info['CAMT 53'].append(path.split("\\")[1])
        elif ("xml" in path or "XML" in path) and "pain.001" in file_data:
            # print("pain.001", path)
            file_info['SEPA'].append(path.split("\\")[1])
        # -----------------------------------------------------------------

        # CHANGE FILE EXTENSION START
        elif ("xml" not in path or "XML" not in path) and file_data.startswith("<?xml") and "camt.053" in file_data:
            print("camt.053", path)
            # file_info['CAMT 53'].append(path.split("\\")[1])

            try:
                if len(file_extension) == 1:
                    file.close()
                    new_file_name = file_extension[0] + ".xml"
                    os.rename(path, new_file_name)
                    file_info['CAMT 53'].append(new_file_name.split("\\")[1])

                if len(file_extension) == 2:
                    file.close()
                    new_file_name = file_extension[0] + ".xml"
                    os.rename(path, new_file_name)
                    file_info['CAMT 53'].append(new_file_name.split("\\")[1])

            except Exception as e:
                # print(e)
                pass

        elif ("xml" not in path or "XML" not in path) and file_data.startswith("<?xml") and "pain.001" in file_data:
            print("pain.001", path)
            try:
                if len(file_extension) == 1:
                    file.close()
                    new_file_name = file_extension[0] + ".xml"
                    os.rename(path, new_file_name)
                    file_info['SEPA'].append(new_file_name.split("\\")[1])

                if len(file_extension) == 2:
                    file.close()
                    new_file_name = file_extension[0] + ".xml"
                    os.rename(path, new_file_name)
                    file_info['SEPA'].append(new_file_name.split("\\")[1])

            except Exception as e:
                # print(e)
                pass
        # CHANGE FILE EXTENSION END

        else:
            file_info['unsupported standard'].append(path.split("\\")[1])

print(file_info)

file_info_df = pd.DataFrame.from_dict(file_info)
file_info_df.to_excel("file_information's.xlsx", index=False)
