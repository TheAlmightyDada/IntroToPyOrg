def maskify(cc):
    msk = str(cc)
    final_string =[]
    hidden_info =[]
    to_be_hidden = msk[:-4]
    seen_info = msk[-4:]
    seperator = ''

    for n in range(0,len(to_be_hidden)):
        n = '#'
        hidden_info.append(n)
    
    for i in hidden_info:
        final_string.append(i)
    
    for i in seen_info:
        final_string.append(i)

    return(seperator.join(final_string))
    
maskify('danger')