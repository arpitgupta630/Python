import requests
import hashlib
import sys

def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f"Error Fetching Data: <Response [{response.status_code}]>, check URL")
    return response

def leak_count(hases, hash_to_check):
    hases_tuple = (lines.split(":") for lines in hases.text.splitlines())
    
    for api_hash, hash_leak_count in hases_tuple:
        if api_hash == hash_to_check:
            return hash_leak_count
    return 0

def pwned_api_check(password):
    # Check password if it exist in API response
    
    # Encoding Password in UTF-8 (Before hashing unicode object must be encoded)
    encoded_password = password.encode("utf-8")
    
    # Converting encoded password into Hash Code object and through hexdigest() convert object to hexadecimal digit
    hash_obj = hashlib.sha1(encoded_password).hexdigest()
    
    # Proper hash code always in capital
    sha1_password = hash_obj.upper()
    
    first5_char, tail = sha1_password[:5], sha1_password[5:]    
    response = request_api_data(first5_char)
    return leak_count(response, tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times pwned in data breach ... You should Probably Change your Password\n')
        else:
            print(f'{password} NOT found in data breach\n')
    return 'DONE!!!'

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))