import json

def main():
    f = open("./json_load_test/myu_test/myu_s.json","r")

    json_data = json.load(f)

    print("{}".format(json.dumps(json_data,indent=4)))

if __name__ == "__main__":
    main()
    
