def calculate_hash(string, d=256, q=1000000007):
    """
    Calculates the hash of a string.

    Args:
        string (str): The text to hash
        d (int) : The size of alphabet (at most 256))
        q (int) : The prime modulos (at most 3.5*10**16 )

    Returns:
        int: The hash value
    """
    # horner's schema
    h = 0
    for char in string:
        h = (h*d + ord(char)) % q
    return h


def pattern_match(pattern, text, count_occurences=0,  q = 1000000007):
    """
    Implements the Rabin-Karp string matching algorithm using a Rolling Hash.

    Args:
        pattern (str): The substring to search for.
        text (str): The main string to search within.
        count_occurences (int, optional): A flag to control search behavior.
            - If 0 (False): Stops after the first match and returns 1.
            - If > 0 (True): Scans the entire text and returns total count of matches.
            Defaults to 0.
        q (int, optional): A large prime number used for modulo arithmetic to 
            prevent integer overflow and minimize hash collisions. 
            Defaults to 1,000,000,007.

    """
    occurences = 0
    d = 256 #base
    m = len(pattern)
    patterns_hash = calculate_hash(pattern)
    current_hash = calculate_hash(text[:m])
    
    for k in range(len(text)-m):
        if current_hash==patterns_hash:
            occurences +=1
            if not count_occurences:
                return occurences
        current_hash = (d * (current_hash - (d**(m-1) % q) * ord(text[k])) + ord(text[k+m])) % q
                
    return occurences
