import pandas as pd

def check_csv_columns(csv_file,getList):
    df = pd.read_csv(csv_file)
    # check = df.apply(lambda col: col.isin(["neuro","ENT"]).all())
    # is_matched = any(df['specialization'].str.contains("Neuro", case=False, na=False))
    is_valid = any(df['Specialization'].isin(["Neuro","ENT Surgeon"]))
    
    return is_valid
    # return check

def IsDataThere(text):
    getList = []
    for part in text.split(","):
        getList.extend(part.split(" "))
    
    csv_file = "doctors_data.csv"
    result = check_csv_columns(csv_file,getList)
    print(result,"-----------")
    if all(word in getList for word in ["help", "you"]):
        print("yes, both are there")
    print(getList)
    return {"mesage":"ok"}