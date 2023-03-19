

def read():
    global last_id, all_data
    with open(file_base, "r",encoding="utf-8") as f:
        all_data = [i.strip() for i in f]



# -------------------------правки-------------------
def read():

    global all_data, last_id

    with open(filename, "r", encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])

            return all_data
    
